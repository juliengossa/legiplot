import re
import sys
import string
import hashlib


class AEArticle:

    word_translator = str.maketrans(string.punctuation, ' '*len(string.punctuation))

    def __init__(self, code, date, version, section = ["Article -1"], PLTC_method = "code"):
        self.code = code
        self.date = date
        self.version = version
        self.section = section
        self.article_full = section[-1].replace("Article ","")
        self.article = self.article_full.replace("*","")

        if PLTC_method == "code":
            [self.partie,self.sous_partie,self.livre,self.titre,self.chapitre] = self.get_PLTC()
        else:
            [self.partie,self.sous_partie,self.livre,self.titre,self.chapitre] = self.get_PLTC_txt()

        self.type_modification = None
        self.type_erreur = None

        self.nb_articles = 1
        self.nb_lignes = 0
        self.nb_mots = 0
        self.nb_modifications = {'Modification':0,'Ajout':0,'Suppression':0}

        self.lignes = ''
        self.digest = None


    @staticmethod
    def get_header(traitement,shrink):
        """ Affiche l'entête selon le traitement
        """
        if traitement == "diff" and shrink > 0 : traitement = "diffstats"

        header = ['code','date','partie','sous_partie','livre','titre','chapitre','article'] #,'version'
        # for i in range(len(header)-1,len(header)-1-shrink,-1):
        #     header[i] = "nb_"+header[i]+"s"
        if ( traitement == "stats" and shrink > 0 ) or traitement == "diffstats":
            header = header[0:-shrink]

        header_spe = {
            'diff': ['type'],
            'check': ['type_erreur'],
            'stats': ['nb_articles','nb_alineas','nb_mots'],
            'diffstats': ['nb_articles','nb_alineas','nb_mots','nb_modifications','nb_ajouts','nb_suppressions']
        }

        return header + header_spe[traitement]

    def get_sections(self):
        return [self.partie,self.sous_partie,self.livre,self.titre,self.chapitre,self.article]

    def get_values(self,traitement,shrink):
        """ Affiche une ligne
        """
        if traitement == "diff" and shrink > 0: traitement = "diffstats"

        values = [self.code, self.date]#self.version,

        sections = self.get_sections()
        if ( traitement == "stats" and shrink > 0 ) or traitement == "diffstats":
            sections = sections[0:-shrink]


        values_spe = {
            'diff': [self.type_modification],
            'check': [self.type_erreur],
            'stats': [self.nb_articles, self.nb_lignes, self.nb_mots],
            'diffstats': [self.nb_articles, self.nb_lignes, self.nb_mots, self.nb_modifications['Modification'],self.nb_modifications['Ajout'],self.nb_modifications['Suppression']]
        }

        return values + sections + values_spe[traitement]


    def is_annex(self):
        """vérifier si un article est dans l'annex ou non
           Quand un article dans l'annex,il y a trois cas:
           1.Il y a le mot Annex dans l'artice
           Exemple: Article Anenex I
           2.Pour les articles pas écrire sa Partie (L ou R ou A) et seulment des numéro
           Exemple: Article 123 /Article 11
           3.Pour les articles ont seulment des numéro Romain (code_de_l'urbanisme)
           Exemple: Article II /Article I
           PS:pour le 2ème cas:
           code_pénal est spéciale,dans sa partie législative,pas de "L" dans le nom des articles
           Exemple: Article L111 est remplcé par Article 111
           return:
           True:C'est un article dans l'annex
           False:ce n'est pas un article dans l'annex
        """
        if self.article.upper().find("ANNEX")!=-1:# or len(self.article)==1:
            return True
        elif self.article[0].isnumeric() and self.code not in ["code_pénal","code_civil"]:
            return True
        #c'est pas numéro romain
        elif self.article[0]=="I" or self.article[0].upper=="V" or self.article[0].upper=="X":
            return True
        else:
            return False

    def get_partie(self):
        #code_pénal est spéciale,dans sa partie législative,pas de "L" dans le nom des articles
        if self.is_annex():
            return "Annexe"
        elif self.article[0] == 'L' or self.article[0].isnumeric():
            return "Législative"
        elif self.article[0] == 'A':
            return "Arrêtés"
        elif self.article[0]=='R' or self.article[0] == 'D':
            return "Réglementaire"
        else:
            return "NA"

    def get_PLTC(self):
        """vérifier le type du nom d'article et extraire les localisations
            cas normal: L111
            Cas spéciaux traités :
            111 : pas de partie
            L10/L10-1 : pas de livre (code_de_justice_administrative 2019-3-25)
            L1/L2/L3 : pas de livre (code_du_travail )
            L3121-3 : sous partie 3, livre 1 (code_du_travail)
            A931-1-1 : (code de la sécurité sociale)
            Cas spéciaux non traités:
            R14-10-2 : livre 1, titre 4, chapitre 10 (code de l'action sociale)
            1874 : livre 3, titre 10 (code civil)
        """
        # Extraire le premier numéro d'article
        # Exemples : Article L621, Article L*612, Article , Article 111, Article L10/L10-,

        P = self.partie = self.get_partie()

        artnumlist = re.sub("[^0-9-]","",self.article).split('-')
        artnum=artnumlist[0]
        if len(artnum) < 3:
            if len(artnumlist)>2:
                if len(artnumlist[1])==2 and len(artnum)==2:
                    return [P,"NA",artnum[0],artnum[1],artnumlist[1]]
                else:
                    return [P,"NA","NA","NA","NA"]
            else:
                return [P,"NA","NA","NA","NA"]
        if len(artnum) == 4:
            souspartie = artnum[0]
            artnum = artnum[1:]
        else:
            souspartie="NA"

        return [P,souspartie,artnum[0],artnum[1],artnum[2]]

    def get_PLTC_txt(self):
        PLTC = ["NA"]*5
        for section in self.section:
            if(section.upper().startswith("PARTIE ")):
                PLTC[0]=section
            elif(section.find("partie : ") != -1) and PLTC[1:] == ["NA"]*4:
                PLTC[1]=section
            elif(section.upper().startswith("LIVRE ")):
                PLTC[2]=section
            elif(section.upper().startswith("TITRE ")):
                PLTC[3]=section
            elif(section.upper().startswith("CHAPITRE ")):
                PLTC[4]=section
        return PLTC

    def normalize_artnum(self):
        an = re.sub("^[^0-9]*","",self.article).replace(" ","-")
        return [ s.zfill(6) for s in an.split('-') ]

    def compare_num(self,other):
        """ Compare les numéros d'articleDe la communauté légale
        return:
            "lt" si self avant other
            "eq" si égal
            "gt" si self après other
            "ew" si les articles sont dans des parties différentes
        """
        if other is None or self.partie == "Annexe" or other.partie == "Annexe": return "ew"
        if self.partie != other.partie: return "ew"
        if self.article == other.article: return "eq"

        s_artnum = self.normalize_artnum()
        o_artnum = other.normalize_artnum()

        try:
            # Gestion L239-1 vs L23-10-1
            if s_artnum[1] == "000010" and o_artnum[0][-1]=="9":
                return "gt"
        except:pass
        try:
            # Gestion L239-1 vs L239-1 A
            if s_artnum == o_artnum[0:-1] and not o_artnum[-1].strip("0").isnumeric():
                return "gt"
        except:pass

        if s_artnum < o_artnum:
            return "lt"
        else: return "gt"

    def finalize(self):
        self.nb_mots = len(self.lignes.translate(self.word_translator).split())
        self.nb_lignes = self.lignes.count('\n')

    def equals(self,article):
        return self.lignes == article.lignes
        # sm = hashlib.sha1()
        # sm.update(self.lignes.encode('utf-8'))
        # om = hashlib.sha1()
        # om.update(article.lignes.encode('utf-8'))
        # return sm.digest() == om.digest()

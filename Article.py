import re

class Article:
    def __init__(self, code, date, version, type, section, PLTC_method = "code"):
        self.code = code
        self.date = date
        self.version = version
        self.type = type
        self.nb_modifications = 0
        self.section = section
        self.article = section[-1].replace("Article ","")
        if PLTC_method == "code":
            self.partie = self.getPartie()
            [self.sous_partie,self.livre,self.titre,self.chapitre] = self.getPLTC()
        else:
            [self.partie, self.sous_partie,self.livre,self.titre,self.chapitre] = self.getPLTC_txt()

    def isAnnex(self):
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
        if self.article.upper().find("ANNEX")!=-1 or len(self.article)==1:
            return True
        elif self.article[0].isnumeric() and self.code not in ["code_pénal","code_civil"]:
            return True
        #c'est pas numéro romain
        elif self.article[0]=="I" or self.article[0].upper=="V" or self.article[0].upper=="X":
            return True
        else:
            return False

    def getPartie(self):
        #code_pénal est spéciale,dans sa partie législative,pas de "L" dans le nom des articles
        if self.isAnnex():
            #Exemple: Article L111 est remplcé par Article 111
            return "Annexe"
        elif self.article[0] == 'L' or self.article[0].isnumeric():
            return "Législative"
        elif self.article[0] == 'A':
            return "Arrêtés"
        elif self.article[0]=='R' or self.article[0] == 'D':
            return "Réglementaire"
        else:
            return "NA"
    
    def getPLTC(self):
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
        artnumlist = re.sub("[^0-9-]","",self.article).split('-')
        artnum=artnumlist[0]
        if len(artnum) < 3:
            if len(artnumlist)>2:
                if len(artnumlist[1])==2 and len(artnum)==2:
                    return ["NA",artnum[0],artnum[1],artnumlist[1]]
                else:
                    return ["NA","NA","NA","NA"]
            else:
                return ["NA","NA","NA","NA"]
        if len(artnum) == 4:
            souspartie = artnum[0]
            artnum = artnum[1:]
        else:
            souspartie="NA"

        return [souspartie,artnum[0],artnum[1],artnum[2]]
        
    def getPLTC_txt(self):
        PLTC = self.section[0:5]
        if len(PLTC) < 5: PLTC.pop()
        while len(PLTC) < 5: PLTC.append("NA")
        return PLTC
    
    def normalizeArtnum(self):
        an = re.sub("^[^0-9]*","",self.article).replace(" ","-")
        return [ s.zfill(6) for s in an.split('-') ]

    def compareNum(self,other):
        """ Compare les numéros d'article
        return:
            "lt" si self avant other
            "eq" si égal
            "gt" si self après other
            "ew" si les articles sont dans des parties différentes
        """
        if other is None or self.partie == "Annexe" or other.partie == "Annexe": return "ew"
        if self.partie != other.partie: return "ew"
        if self.article == other.article: return "eq"

        s_artnum = self.normalizeArtnum()
        o_artnum = other.normalizeArtnum()

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


 
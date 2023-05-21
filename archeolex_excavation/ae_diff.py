


    def get_difflines(self,commit):
        """Obtenir les différences entre cette version et la version précédentes

            Arg:
                commit:Commit(type) numéro de version

            return:
                lines:list des informations différentes
        """
        diff = self.commit.parents[0].diff(self.commit, create_patch=True, unified=100000000).pop()
        cmp = diff.diff.decode('utf-8').splitlines()
        return list(cmp)

    @staticmethod
    def _get_type_line(line):
        if line.startswith('-'):             # -######Article est Supression
            type_line = "Suppression"
        elif line.startswith('+'):           # +######Article est Ajout
            type_line = "Ajout"
        else:
            type_line = None
        return type_line


    def process_diff(self,commit):
        """ Traite un diff entre une version d'un code et sa précédente
            (tel que renvoyé par git diff)

            Arg:
                commit: Commit de version

            return:
                mods:dict qui répresente une modification(un dict)
        """
        #get la version et la date
        date = self.get_date(commit)
        version = self.get_version(commit)
        #get lines in diff
        lines=self.get_difflines(commit)
        if self.verbose:
            tf = tempfile.NamedTemporaryFile(suffix='.csv', prefix=os.path.basename(__file__))
            tf_dir = os.path.dirname(tf.name)

            with open(tf_dir+'/'+self.code+'-'+date+'.txt', 'w',encoding="utf-8") as verbfile:
                verbfile.write('\n'.join(str(line) for line in lines))

        curmod = None # modification courante
        cursec = [] # section courante
        mods = {}

        for num,line in enumerate(lines):
            # Détection du type de la ligne
            type_line = self._get_type_line(line)

            # Si changement de section, enregistrer la nouvelle section
            if (len(line) > 2 and line[1] == '#'):
                level = line.count("#")
                cursec = cursec[:level-1]+[re.sub(".*# ","",line)]

                # Si changement d'article
                if line.find("Article") != -1:
                    # Si une modification a été détectée, l'enregistrer
                    if curmod is not None and curmod.type_modification is not None:
                        if curmod.article in mods:
                            nbm = mods[curmod.article].nb_modifications + curmod.nb_modifications
                            if nbm == 0:
                                del mods[curmod.article]
                            else:
                                mods[curmod.article].type_modification = "Modification"
                                mods[curmod.article].nb_modifications = nbm
                        else:
                            mods[curmod.article] = curmod

                    # Réinitialiser la modification courante
                    curmod = AEArticle(self.code, date, version, cursec, self.PLTC_method)
                    curmod.type_modification = type_line


            # Si pas de changement de section, on vérifie juste s'il n'y a pas de modifications,
            # dans une ligne non vide
            elif type_line is not None and len(line[1:].strip()) > 0 and curmod is not None:
                if curmod.type_modification is None : curmod.type_modification = "Modification"
                curmod.nb_modifications += 1

        if curmod is not None and curmod.type_modification is not None:
            if curmod.article not in mods:
                mods[curmod.article] = curmod

        return mods

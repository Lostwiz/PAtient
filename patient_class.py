class patient:

    def __init__(self, pNoPatient="", pNom="", pPrenom="", pDateNaiss="",
                 pNbVisites=0, pCommentaire=""):
        self.__noPatient = pNoPatient
        self.__Nom = pNom
        self.__Prenom = pPrenom
        self.__dateNaiss = pDateNaiss
        self.__nbVisites = pNbVisites
        self.commentaire = pCommentaire

    def __get__noPatient(self):
        return self.__noPatient

    def __set__noPatient(self,pNumero):
        if pNumero.isnumeric() and pNumero.len == 7 :
            self.__noPatient = pNumero

    noPatient = property(__get__noPatient,__set__noPatient)

    def __get__Nom(self):
        return self.__Nom

    def __set__nom(self,pnom):
        if pnom.isalpha() and pnom <= 30 and pnom.len != 0:
            self.__Nom = pnom

    nom = property(__get__Nom,__set__nom)

    def __get__prenom(self):
        return self.__Prenom

    def __set__prenom(self,pprenom):
        if pprenom.isalpha() and pprenom <= 30:
            self.__Prenom = pprenom

    prenom = property(__get__prenom,__set__prenom)

    def __get__nbVisite(self):
        return self.__nbVisites

    def __set__nbvisite(self,p_nb):
        if p_nb.isalpha():
            self.__nbVisites = int(p_nb)

    NbVisite = property(__get__nbVisite,__set__nbvisite)

    def __get__couriel(self):
        courielle = f"{self.prenom}_{self.nom}@cabinetmedical.ca"
        return courielle

    Courriel = property(__get__couriel)

    def __get__date(self):
        return self.__dateNaiss

    def __set__date(self,date):
        if date > datetime.date.today():
            self.__dateNaiss = date

    Naissance = property(__get__date,__set__date)

    def calculer_age(self):
        import datetime
        Aujourdhui = datetime.date.today()
        return Aujourdhui.year - self.year - ((Aujourdhui.month, Aujourdhui.day)
                                              < (self.Naissance.month,self.Naissance.day))








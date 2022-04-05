import datetime
class patient:

    def __init__(self, pNoPatient="", pNom="erreur!", pPrenom="erreur!", pDateNaiss="",
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
        print("hey")
        if pNumero.isnumeric() and len(pNumero) == 7 :
            self.__noPatient = pNumero

    noPatient = property(__get__noPatient,__set__noPatient)

    def __get__Nom(self):
        return self.__Nom

    def __set__nom(self,pnom):
        print(len(pnom))
        if pnom.isalpha() and len(pnom) <= 30 and len(pnom) > 0:
            self.__Nom = pnom

    nom = property(__get__Nom,__set__nom)

    def __get__prenom(self):
        return self.__Prenom

    def __set__prenom(self,pprenom):
        if pprenom.isalpha() and len(pprenom) <= 30 and len(pprenom) > 0:
            self.__Prenom = pprenom

    prenom = property(__get__prenom,__set__prenom)

    def __get__nbVisite(self):
        return self.__nbVisites

    def __set__nbvisite(self,p_nb):
        print("HEY")
        if p_nb.isnumeric():
            self.__nbVisites = int(p_nb)
        else:
            self.__nbVisites = "INVALIDE"

    NbVisite = property(__get__nbVisite,__set__nbvisite)

    def __get__couriel(self):
        courielle = f"{self.prenom}_{self.nom}@cabinetmedical.ca"
        return courielle

    Courriel = property(__get__couriel)

    def __get__date(self):
        return self.__dateNaiss

    def __set__date(self,date):
        print("hey")
        aujourdhui = datetime.date.today()
        if date < aujourdhui:
            print("why")
            self.__dateNaiss = date

    Naissance = property(__get__date,__set__date)
    def calculer_age(self):
        import datetime
        Aujourdhui = datetime.date.today()
        return Aujourdhui.year - self.year - ((Aujourdhui.month, Aujourdhui.day)
                                              < (self.Naissance.month,self.Naissance.day))
    def calculer_cout_total(self):
        return self.NbVisite * 25









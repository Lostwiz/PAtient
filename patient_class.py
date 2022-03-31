class patient:

    def __init__(self, pNoPatient="", pNom="", pPrenom="", pDateNaiss="",
                 pCourriel="", pNbVisites=0, pCommentaire=""):
        self.__noPatient = pNoPatient
        self.__Nom = pNom
        self.__Prenom = pPrenom
        self.__dateNaiss = pDateNaiss
        self.__courriel = pCourriel
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
        if pnom.isalpha() and pnom <= 30:
            self.__Nom = pnom

    nom = property(__get__Nom,__set__nom)

    def __get__prenom(self):
        return self.__Prenom

    def __set__prenom(self,pprenom):
        if pprenom.isalpha() and pprenom <= 30:
            self.__Prenom = pprenom

    prenom = property(__get__prenom,__set__prenom)







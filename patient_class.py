#importation de datetime et json(serilisation
import json
from datetime import *
class patient:

    # constructeur init class intial
    def __init__(self, pNoPatient="", pNom="erreur!", pPrenom="erreur!", pDateNaiss=datetime.now(),
                 pNbVisites=0, pCommentaire=""):
        self.__noPatient = pNoPatient
        self.__Nom = pNom
        self.__Prenom = pPrenom
        self.__dateNaiss = pDateNaiss
        self.__nbVisites = pNbVisites
        self.__commentaire = pCommentaire
    # get et set pour le numero de patient
    def __get__noPatient(self):
        return self.__noPatient

    def __set__noPatient(self,pNumero):
        print("hey")
        if pNumero.isnumeric() and len(pNumero) == 7 :
            self.__noPatient = pNumero
    #propirité no patient
    noPatient = property(__get__noPatient,__set__noPatient)

    #GET et setter du nom du patient
    def __get__Nom(self):
        return self.__Nom

    def __set__nom(self,pnom):
        # verification nom alphabétique et entre 1 et 30 carcatere
        if pnom.isalpha() and len(pnom) <= 30 and len(pnom) > 0:
            self.__Nom = pnom

    # proprieté nom du patient
    nom = property(__get__Nom,__set__nom)

    #propriété et prenom du patient
    def __get__prenom(self):
        return self.__Prenom

    def __set__prenom(self,pprenom):
        # verification prenom alphabétique et entre 1 et 30 caractere
        if pprenom.isalpha() and len(pprenom) <= 30 and len(pprenom) > 0:
            self.__Prenom = pprenom

    # prropriété prenom du  patient
    prenom = property(__get__prenom,__set__prenom)
    # get et setter du nb de visite
    def __get__nbVisite(self):
        return self.__nbVisites

    def __set__nbvisite(self,p_nb):
        if p_nb.isnumeric():
            self.__nbVisites = int(p_nb)
        else:
            self.__nbVisites = "INVALIDE"
    # propriété nb de visite
    NbVisite = property(__get__nbVisite,__set__nbvisite)
    # mise en place et formatage du courrielle
    def __get__couriel(self):
        courielle = f"{self.prenom}_{self.nom}@cabinetmedical.ca"
        return courielle
    #proriétét courrielle
    Courriel = property(__get__couriel)
    #mise en place de naissance
    def __get__date(self):
        return self.__dateNaiss

    def __set__date(self,dates):
        aujourdhui = date.today()
        if dates < aujourdhui:
            self.__dateNaiss = dates.strftime('%d/%m/%Y')
        else:
            self.__dateNaiss = "broken"

    Naissance = property(__get__date,__set__date)
    #propriét commentair et get et setter
    def __get__commentaire(self):
        return self.__commentaire
    def __set__commentaire(self,p_comment):
        self.__commentaire = p_comment

    Commentaire = property(__get__commentaire,__set__commentaire)
    def __str__(self):
        print(self.Naissance)
        return("*"*90+"\n"+
               f"numero du patient :{self.noPatient:>141}\n"
               f"nom du patient      :  {self.nom:>145}\n"
               f"prenom du patient   : {self.prenom:>145}\n"
               f"courriel            :{self.Courriel:>141}\n"
               f"date de naisance    :{self.Naissance}\n"
               f"commentaire         :{self.Commentaire}")
    # cacule age inspiration :
    # https://fr.acervolima.com/programme-python-pour-calculer-lage-en-annee/#:~:text=Python%20fournit%20un%20module%20datetime,de%20naissance%20et%20l'anniversaire.
    def calculer_age(self):
        Aujourdhui = date.today()
        return Aujourdhui.year - self.Naissance.year- ((Aujourdhui.month, Aujourdhui.day)
                                              < (self.Naissance.month,self.Naissance.day))
    def calculer_cout_total(self):
        return self.NbVisite * 25
    ###  SERIALISATION INSPIRER DE l'exercise class etudiant
    def sauvgarder(self,p_sauv):
        with open(p_sauv,"w") as sauv:
            json.dump(self.__dict__, sauv)
    def ouvrir(self,p_ouvr):
        with open(p_ouvr,"r") as ouvrir
            self.__dict__ = json.load(ouvrir)











import patient_class
import  code_dialogue_box as d
import sys
import code_interface_genere as p
from PyQt5 import QtWidgets, QtCore
import json
import datetime
# CAcher les label de la fentre de serialisation
#def lbl_error_hidden(fenetre):
    #fenetre.lblSerialEchou.setVisible(False)
    #fenetre.lblSerialFonc.setVisible(False)


# cacher les label de fentre principal
def lbl_hidden(fenetre):
    fenetre.lbl_erreurnum.setVisible(False)
    fenetre.lbl_erreur_prenom.setVisible(False)
    fenetre.lbl_erreur_nom.setVisible(False)
    fenetre.lbl_erreurVisite.setVisible(False)
    fenetre.lbl_erreur_naissance.setVisible(False)
    # inspirer de l'exerise class etudiant
# lst client pour garder objet
lstClient = []


class fenetresecon(QtWidgets.QDialog,d.Ui_Dialog):
    def __init__(self, parent=None):
        super(fenetresecon, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("serialisation")

# intial fentre principal
class Fenetreprin(QtWidgets.QMainWindow, p.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Fenetreprin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des patients")
        lbl_hidden(self)
    # code bbouton valider
    @QtCore.pyqtSlot()
    def on_btn_valider_clicked(self):
        objPatient = patient_class.patient()
        lbl_hidden(self)
        # interrupteur pour valeur validation
        valide = True
        # prise dess valeur pour l'objet
        dateNai = self.date_naissance_edit.date()
        num = self.lnedt_num.text()
        str_nom = self.lnedt_nom.text()
        str_prenom = self.lnedt_prenom.text()
        nbVisite = self.lnedt_visite.text()
        objPatient.Commentaire = self.lineEdit.text()
        # utilisation de pydate pour meilleur formatation
        objPatient.Naissance = dateNai.toPyDate()
        # verification que les valeur sont  valide
        if objPatient.Naissance == "broken":
            self.lbl_erreur_naissance.setVisible(True)
            valide = False
        objPatient.noPatient = num
        if objPatient.noPatient != num:
            self.lbl_erreurnum.setVisible(True)
            valide = False
        objPatient.NbVisite = nbVisite
        if objPatient.NbVisite == "INVALIDE":
            self.lbl_erreurVisite.setVisible(True)
        objPatient.nom = str_nom
        if objPatient.nom != str_nom:
            self.lbl_erreur_nom.setVisible(True)
            valide = False
        objPatient.prenom = str_prenom
        if objPatient.prenom != str_prenom:
            self.lbl_erreur_prenom.setVisible(True)
            valide = False
        if valide:
            lstClient.append(objPatient)
        #efface de la liste et renplacement par la nouvelle
        self.txt_patients.clear()
        for patient in lstClient:
            self.txt_patients.append(str(patient))
    # code pour releas du bouton patient
    def on_btn_sauvgarder_released(self):
        for patient in lstClient:
            if patient.noPatient == self.lnedt_num.text():
                nom_fichier = f"Fichierjson/{patient.nom}_{patient.prenom}.json"
                patient.sauvgarder(nom_fichier)
        ui = fenetresecon()
        ui.show()
        ui.exec_()
    def on_btn_ouvrir_released(self):


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Fenetreprin()
    form.show()
    app.exec()
if __name__ == "__main__":
    main()
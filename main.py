import patient_class
import sys
import code_interface_genere as p
from PyQt5 import QtWidgets, QtCore
import datetime

def lbl_hidden(fenetre):
    fenetre.lbl_erreurnum.setVisible(False)
    fenetre.lbl_erreur_prenom.setVisible(False)
    fenetre.lbl_erreur_nom.setVisible(False)
    fenetre.lbl_erreurVisite.setVisible(False)
    fenetre.lbl_erreur_naissance.setVisible(False)

lstClient = []



class Fenetreprin(QtWidgets.QMainWindow, p.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Fenetreprin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des patients")
        lbl_hidden(self)
    @QtCore.pyqtSlot()
    def on_btn_valider_clicked(self):
        objPatient = patient_class.patient()
        lbl_hidden(self)
        valide = True
        dateNai = self.date_naissance_edit.date()
        num = self.lnedt_num.text()
        str_nom = self.lnedt_nom.text()
        str_prenom = self.lnedt_prenom.text()
        nbVisite = self.lnedt_visite.text()
        objPatient.Naissance = dateNai
        if objPatient.Naissance != dateNai :
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
        self.txt_patients.clear()
        for patient in lstClient:
            self.txt_patients.append(str(patient))



        


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Fenetreprin()
    form.show()
    app.exec()
if __name__ == "__main__":
    main()
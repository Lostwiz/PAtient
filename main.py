import patient_class
import sys
import code_interface_genere as p
from PyQt5 import QtWidgets, QtCore

def lbl_hidden(fenetre):
    fenetre.lbl_erreurnum.setVisible(False)
    fenetre.lbl_erreur_prenom.setVisible(False)
    fenetre.lbl_erreur_nom.setVisible(False)
    fenetre.lbl_erreurVisite.setVisible(False)
    fenetre.lbl_erreur_naissance.setVisible(False)



class Fenetreprin(QtWidgets.QMainWindow, p.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Fenetreprin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des patients")
        lbl_hidden(self)
    @QtCore.pyqtSlot()
    def on_btn_valider_clicked(self):
        nom = self.lnedt_nom.text(self)
        num = self.lnedt_num.text(self)
        datenais = self.date_naissance_edit.date()
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Fenetreprin()
    form.show()
    app.exec()
if __name__ == "__main__":
    main()
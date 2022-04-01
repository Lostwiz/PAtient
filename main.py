import patient_class
import sys
import code_interface_genere as p
from PyQt5 import QtWidgets, QtCore

class Fenetreprin(QtWidgets.QMainWindow, p.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Fenetreprin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion des patients")
    def lbl_hidden(self):
        self.lbl_erreurnum.hide()
        self.lbl_erreur_prenom()
        self.lbl_erreur_nom
        self.
    @QtCore.pyqtSlot()
    def on_btn_valider_clicked(self):
        nom = self.lnedt_nom.text()
        num = self.lnedt_num.text()
        datenais = self.date_naissance_edit.date()
        


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = Fenetreprin()
    form.show()
    app.exec()
if __name__ == "__main__":
    main()
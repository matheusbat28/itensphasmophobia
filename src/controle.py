import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from screen.index import Ui_mainWindow
from random import sample

class Index(QMainWindow, Ui_mainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btGerar.clicked.connect(self.randomItems)
        self.btLimpar.clicked.connect(self.limpar)

    def different_items(self, list_items):
        self.limpar()
        playerLucas = sample(list_items, 1)
        playerMarcos = sample(list_items, 1)
        playerIgor = sample(list_items, 1)
        playerMatheus = sample(list_items, 1)

        while True:
            if playerLucas == playerMarcos:
                playerMarcos = sample(list_items, 1)
            elif playerLucas == playerIgor:
                playerIgor = sample(list_items, 1)
            elif playerLucas == playerMatheus:
                playerMatheus = sample(list_items, 1)
            elif playerMarcos == playerIgor:
                playerIgor = sample(list_items, 1)
            elif playerMarcos == playerMatheus:
                playerMatheus = sample(list_items, 1)
            elif playerIgor == playerMatheus:
                playerMatheus = sample(list_items, 1)
            else:
                break

        self.lbIgor.setText(playerIgor[0])
        self.lbLucas.setText(playerLucas[0])
        self.lbMarcos.setText(playerMarcos[0])
        self.lbMatheus.setText(playerMatheus[0])


    def check(self, list_itens):
        list_itens.clear()
        if self.cbEmf.isChecked():
            list_itens.append('emf')
        if self.cbTemperatura.isChecked():
            list_itens.append('temperatura')
        if self.cbUV.isChecked():
            list_itens.append('lanterna uv')
        if self.cbSpirit.isChecked():
            list_itens.append('spirit box')
        if self.cbLivro.isChecked():
            list_itens.append('livro')
        if self.cbCamera.isChecked():
            list_itens.append('camera de video')

    def randomItems(self):
        list_items = []
        self.check(list_items)
        if len(list_items) == 0:
            QMessageBox.critical(self,'ops!! erro', 'nenhum item foi selecionado')
            self.limpar()
        elif len(list_items) < 4:
            QMessageBox.critical(self,'ops!! erro', 'seleciona no minimo 4 itens')
            self.limpar()
        else:
            self.different_items(list_items)

    def limpar(self):
        self.lbIgor.setText('')
        self.lbLucas.setText('')
        self.lbMarcos.setText('')
        self.lbMatheus.setText('')



qt = QApplication(sys.argv)
ig = Index()
ig.show()
qt.exec_()
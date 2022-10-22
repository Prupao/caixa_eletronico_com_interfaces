from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])

interface_do_caixaQt = uic.loadUi("interfaces_do_sistema/interface_do_caixa.ui")
quantidadeDeNotasQt = uic.loadUi("interfaces_do_sistema/quantidadeDeNotas.ui")
popUpQt = uic.loadUi("interfaces_do_sistema/popUpEmFalta.ui")
popUp2Qt = uic.loadUi("interfaces_do_sistema/popUpMultiploDe20.ui")
popUp3Qt = uic.loadUi("interfaces_do_sistema/popUpNewCed.ui")
addCedulaQt = uic.loadUi("interfaces_do_sistema/addCedula.ui")
replenishBankNotesQt = uic.loadUi("interfaces_do_sistema/reporCedulas.ui")


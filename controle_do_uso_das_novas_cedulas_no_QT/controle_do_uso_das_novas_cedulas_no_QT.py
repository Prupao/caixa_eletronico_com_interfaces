from caixa_eletronico.interfaces_e_modulos import *


# A função abaixo analisa qual o valor de cada cédula nova, e envia sua quantidade total para a interface.
def seeTheQtdOfTheNewCedOnQt(newCed: int, qtdnewCed: int) -> str:
    if newCed == 200:
        return quantidadeDeNotasQt.le_qtd200.setText(str(qtdnewCed))
    elif newCed == 20:
        return quantidadeDeNotasQt.le_qtd20.setText(str(qtdnewCed))
    elif newCed == 5:
        return quantidadeDeNotasQt.le_qtd5.setText(str(qtdnewCed))
    elif newCed == 2:
        return quantidadeDeNotasQt.le_qtd2.setText(str(qtdnewCed))


# A função abaixo só mostrará a quantidade de cédulas usadas no saque se as cédulas em questão tiverem sido adicionadas
# pelo Usuário.
def sendQtdOfNewCedUsedOnWithdrawToQT(totcedNew200: int, totcedNew20: int, totcedNew5: int, totcedNew2: int) -> None:
    if interface_do_caixaQt.qtd200LineEdit.hasFrame():
        interface_do_caixaQt.qtd200LineEdit.setText(str(totcedNew200))
    if interface_do_caixaQt.qtd20LineEdit.hasFrame():
        interface_do_caixaQt.qtd20LineEdit.setText(str(totcedNew20))
    if interface_do_caixaQt.qtd5LineEdit.hasFrame():
        interface_do_caixaQt.qtd5LineEdit.setText(str(totcedNew5))
    if interface_do_caixaQt.qtd2LineEdit.hasFrame():
        interface_do_caixaQt.qtd2LineEdit.setText(str(totcedNew2))

from caixa_eletronico.make_new_ced_appear_on_QT.make_new_ced_appear_on_QT import *
from funcoes_de_valores_predefinidos.funcoes_de_valores_predefinidos import *
from controle_do_uso_das_novas_cedulas_no_QT.controle_do_uso_das_novas_cedulas_no_QT import *

# Variaveis abaixo determinam a quantidade de cedulas de 10, 50, 100.
qtdCedTen = 100
qtdCedFifty = 100
qtdCedOneHundred = 100

# O saldo abaixo é formado pela quantidade de cédulas existentes no caixa.
saldo = (qtdCedTen * 10) + (qtdCedFifty * 50) + (qtdCedOneHundred * 100)

# As ações abaixo fazem com que o caixa inicie com a quantidade e o saldo já na interface
quantidadeDeNotasQt.le_qtd10.setText(str(qtdCedTen))
quantidadeDeNotasQt.le_qtd50.setText(str(qtdCedFifty))
quantidadeDeNotasQt.le_qtd100.setText(str(qtdCedOneHundred))
quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))

# As variáveis abaixo contam a quantidade de cédulas utilizadas em cada saque.
totced50 = 0
totced100 = 0
totced10 = 0
totcedNew200 = 0
totcedNew20 = 0
totcedNew5 = 0
totcedNew2 = 0

# Cria variáveis anônimas que virarão ao decorrer do código novas cédulas adicionadas
newCed1 = 0
qtdnewCed1 = 0
newCed2 = 0
qtdnewCed2 = 0
newCed3 = 0
qtdnewCed3 = 0
newCed4 = 0
qtdnewCed4 = 0

# As booleanas a seguir, analisarão se cedulas novas foram adicionadas ao sistema
hasNewCed1 = False
hasNewCed2 = False
hasNewCed3 = False
hasNewCed4 = False


# A função Clean limpa e também dá acesso a parte administrativa do sistema.
def clean() -> None:
    password = interface_do_caixaQt.le_digiteValor.text()
    if password == "gerencia123":
        quantidadeDeNotasQt.show()
    interface_do_caixaQt.le_digiteValor.setText("")
    interface_do_caixaQt.le_qtd10.setText("")
    interface_do_caixaQt.le_qtd50.setText("")
    interface_do_caixaQt.le_qtd100.setText("")
    interface_do_caixaQt.qtd5LineEdit.setText("")
    interface_do_caixaQt.qtd2LineEdit.setText("")
    interface_do_caixaQt.qtd20LineEdit.setText("")
    interface_do_caixaQt.qtd200LineEdit.setText("")
    interface_do_caixaQt.lcd_saldo.display(0)


# A função abaixo adiciona as cédulas ao sistema e a interface, além de delimitar quais poderão ser adicionadas.
def addNovasCedulas() -> None:
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3
    global qtdnewCed4, hasNewCed1, hasNewCed2, hasNewCed3, hasNewCed4
    newBankNote = int(addCedulaQt.le_addCed.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        if newBankNote != 100 and newBankNote != 10 and newBankNote != 50:
            if newBankNote == 200 or newBankNote == 5 or newBankNote == 2 or newBankNote == 20:
                if newCed1 == 0 and newBankNote > 0:
                    newCed1 = newBankNote
                    qtdnewCed1 = 100
                    seeTheQtdOfTheNewCedOnQt(newCed1, qtdnewCed1)
                    makeTheNewCedAppearOnQt(newCed1)
                    saldo = (qtdCedTen * 10) + (qtdCedFifty * 50) + (qtdCedOneHundred * 100) + (newCed1 * qtdnewCed1)
                    quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
                    hasNewCed1 = True
                elif newCed2 == 0 and newBankNote > 0 and newBankNote != newCed1:
                    newCed2 = newBankNote
                    qtdnewCed2 = 100
                    seeTheQtdOfTheNewCedOnQt(newCed2, qtdnewCed2)
                    saldo = (qtdCedTen * 10) + (qtdCedFifty * 50) + (qtdCedOneHundred * 100) + (newCed1 * qtdnewCed1) + (
                                newCed2 * qtdnewCed2)
                    quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
                    makeTheNewCedAppearOnQt(newCed2)
                    hasNewCed2 = True
                elif newCed3 == 0 and newBankNote > 0 and newCed1 != newBankNote != newCed2:
                    newCed3 = newBankNote
                    qtdnewCed3 = 100
                    seeTheQtdOfTheNewCedOnQt(newCed3, qtdnewCed3)
                    saldo = (qtdCedTen * 10) + (qtdCedFifty * 50) + (qtdCedOneHundred * 100) + (newCed1 * qtdnewCed1) + (
                                newCed2 * qtdnewCed2) + (newCed3 * qtdnewCed3)
                    quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
                    makeTheNewCedAppearOnQt(newCed3)
                    hasNewCed3 = True
                elif newCed4 == 0 and newCed2 != newBankNote > 0 and newCed1 != newBankNote != newCed3:
                    newCed4 = newBankNote
                    qtdnewCed4 = 100
                    seeTheQtdOfTheNewCedOnQt(newCed4, qtdnewCed4)
                    saldo = (qtdCedTen * 10) + (qtdCedFifty * 50) + (qtdCedOneHundred * 100) + (newCed1 * qtdnewCed1) + (
                                newCed2 * qtdnewCed2) + (newCed3 * qtdnewCed3) + (newCed4 * qtdnewCed4)
                    quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
                    makeTheNewCedAppearOnQt(newCed4)
                    hasNewCed4 = True
                else:
                    if newCed1 != 0 and newCed2 != 0 and newCed3 != 0 and newCed4 != 0:
                        popUp3Qt.le_aviso.setText("Todas as cédulas existentes estão no caixa!")
                        popUp3Qt.show()
                    else:
                        popUp3Qt.le_aviso.setText("Tente novamente!")
                        popUp3Qt.show()
            else:
                popUp3Qt.le_aviso.setText("Cédula não existe, tente novamente!")
                popUp3Qt.show()
        else:
            popUp3Qt.le_aviso.setText("Cédula já existente no caixa")
            popUp3Qt.show()


# A função Saque controla a quantidade de cédulas utilizadas em cada saque efetuado e avisa se necessário de erros
# na hora do saque.
def saque() -> int:
    global totced10, totced50, totced100, qtdCedTen, qtdCedFifty, qtdCedOneHundred, saldo
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3, qtdnewCed4
    global totcedNew200, totcedNew20, totcedNew5, totcedNew2
    withdrawValue = int(interface_do_caixaQt.le_digiteValor.text())
    total = withdrawValue
    ced100 = 100
    ced10 = 10
    ced50 = 50
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        if total >= 10 and withdrawValue <= saldo:
            while True:
                if total >= newCed1 == 200 and qtdnewCed1 > 0 or total >= newCed2 == 200 and qtdnewCed2 > 0 or total >= newCed3 == 200 and qtdnewCed3 > 0 or total >= newCed4 == 200 and qtdnewCed4 > 0:
                    if newCed1 == 200:
                        total -= newCed1
                        totcedNew200 += 1
                        qtdnewCed1 -= 1
                    elif newCed2 == 200:
                        total -= newCed2
                        totcedNew200 += 1
                        qtdnewCed2 -= 1
                    elif newCed3 == 200:
                        total -= newCed3
                        totcedNew200 += 1
                        qtdnewCed3 -= 1
                    elif newCed4 == 200:
                        total -= newCed4
                        totcedNew200 += 1
                        qtdnewCed4 -= 1
                elif total >= ced100 and qtdCedOneHundred > 0:
                    total -= ced100
                    totced100 += 1
                    qtdCedOneHundred -= 1
                elif total >= ced50 and qtdCedFifty > 0:
                    total -= ced50
                    totced50 += 1
                    qtdCedFifty -= 1
                elif total >= newCed1 == 20 and qtdnewCed1 > 0 or total >= newCed2 == 20 and qtdnewCed2 > 0 or total >= newCed3 == 20 and qtdnewCed3 > 0 or total >= newCed4 == 20 and qtdnewCed4 > 0:
                    if newCed1 == 20:
                        total -= newCed1
                        totcedNew20 += 1
                        qtdnewCed1 -= 1
                    elif newCed2 == 20:
                        total -= newCed2
                        totcedNew20 += 1
                        qtdnewCed2 -= 1
                    elif newCed3 == 20:
                        total -= newCed3
                        totcedNew20 += 1
                        qtdnewCed3 -= 1
                    elif newCed4 == 20:
                        total -= newCed4
                        totcedNew20 += 1
                        qtdnewCed4 -= 1
                elif total >= ced10 and qtdCedTen > 0:
                    total -= ced10
                    totced10 += 1
                    qtdCedTen -= 1
                elif total >= newCed1 == 5 and qtdnewCed1 > 0 or total >= newCed2 == 5 and qtdnewCed2 > 0 or total >= newCed3 == 5 and qtdnewCed3 > 0 or total >= newCed4 == 5 and qtdnewCed4 > 0:
                    if newCed1 == 5:
                        total -= newCed1
                        totcedNew5 += 1
                        qtdnewCed1 -= 1
                    elif newCed2 == 5:
                        total -= newCed2
                        totcedNew5 += 1
                        qtdnewCed2 -= 1
                    elif newCed3 == 5:
                        total -= newCed3
                        totcedNew5 += 1
                        qtdnewCed3 -= 1
                    elif newCed4 == 5:
                        total -= newCed4
                        totcedNew5 += 1
                        qtdnewCed4 -= 1
                elif total >= newCed1 == 2 and qtdnewCed1 > 0 or total >= newCed2 == 2 and qtdnewCed2 > 0 or total >= newCed3 == 2 and qtdnewCed3 > 0 or total >= newCed4 == 2 and qtdnewCed4 > 0:
                    if newCed1 == 2:
                        total -= newCed1
                        totcedNew2 += 1
                        qtdnewCed1 -= 1
                    elif newCed2 == 2:
                        total -= newCed2
                        totcedNew2 += 1
                        qtdnewCed2 -= 1
                    elif newCed3 == 2:
                        total -= newCed3
                        totcedNew2 += 1
                        qtdnewCed3 -= 1
                    elif newCed4 == 2:
                        total -= newCed4
                        totcedNew2 += 1
                        qtdnewCed4 -= 1
                elif total == 0:
                    interface_do_caixaQt.le_qtd10.setText(str(totced10))
                    interface_do_caixaQt.le_qtd50.setText(str(totced50))
                    interface_do_caixaQt.le_qtd100.setText(str(totced100))
                    sendQtdOfNewCedUsedOnWithdrawToQT(totcedNew200, totcedNew20, totcedNew5, totcedNew2)
                    return withdrawValue
                else:
                    if total != 0:
                        popUp2Qt.show()
                        popUp2Qt.le_aviso.setText('Valor indisponível, escreva um multiplo de 10')
                    return 0
        else:
            popUp2Qt.show()
            popUp2Qt.le_aviso.setText('Valor indisponível, tente novamente')
            return 0


# As três funções abaixo fazem os PopUp do sistema, quando as cédulas acabarem(todas, ou individualmente)
# Notifica a falta de uma cédula específica padrão.
def popUpCedPadrao(banknote1: int, banknote2: int, banknote3: int) -> str:
    if banknote1 == 0 and banknote2 == 0 and banknote3 == 0:
        popUpQt.show()
        warning = "Nenhuma cédula contém notas para saque"
        return popUpQt.le_aviso.setText(str(warning))
    elif banknote1 == 0:
        popUpQt.show()
        warning = "O valor 10 está com {} cedulas".format(banknote1)
        return popUpQt.le_aviso.setText(str(warning))
    elif banknote2 == 0:
        popUpQt.show()
        warning = "O valor 50 está com {} cedulas".format(banknote2)
        return popUpQt.le_aviso.setText(str(warning))
    elif banknote3 == 0:
        popUpQt.show()
        warning = "O valor 100 está com {} cedulas".format(banknote3)
        return popUpQt.le_aviso.setText(str(warning))


# Notifica a falta de uma cédula específica nova.
def popUpWarningNewCed(banknote1: int, banknote2: int, banknote3: int, banknote4: int) -> str:
    if banknote1 == 0 and banknote2 == 0 and banknote3 == 0 and banknote4 == 0:
        popUpQt.show()
        warning = "Nenhuma cédula nova contém notas para saque"
        return popUp3Qt.le_aviso.setText(str(warning))
    if qtdnewCed1 == 0 and hasNewCed1 == True:
        popUpWarningIndiv(newCed1, qtdnewCed1)
    if qtdnewCed2 == 0 and hasNewCed2 == True:
        popUpWarningIndiv(newCed2, qtdnewCed2)
    if qtdnewCed3 == 0 and hasNewCed3 == True:
        popUpWarningIndiv(newCed3, qtdnewCed3)
    if qtdnewCed4 == 0 and hasNewCed4 == True:
        popUpWarningIndiv(newCed4, qtdnewCed4)


def popUpWarningIndiv(banknote: int, contNewCed: int) -> str:
    if banknote == 0:
        popUpQt.show()
        warning = "O valor {} está com {} cedulas".format(contNewCed, banknote)
        return popUpQt.le_aviso.setText(str(warning))


# A função abaixo administra quando os PopUp aparecerão na tela
def condicionalToDisplayPopUp() -> None:
    global qtdCedTen, qtdCedFifty, qtdCedOneHundred
    global newCed1, newCed2, newCed3, newCed4
    if qtdnewCed1 == 0 and hasNewCed1 == True or qtdnewCed2 == 0 and hasNewCed2 == True or qtdnewCed3 == 0 and hasNewCed3 == True or qtdnewCed4 == 0 and hasNewCed4 == True:
        popUpWarningNewCed(newCed1, newCed2, newCed3, newCed4)
    if hasNewCed1 == False:
        popUpCedPadrao(qtdCedTen, qtdCedFifty, qtdCedOneHundred)
    elif qtdnewCed1 == 0 and qtdnewCed2 == 0 and qtdnewCed3 == 0 and qtdnewCed4 == 0:
        # Existe as cedulas novas no sistema, mas não existem mais notas da mesma, podendo então rodar o PopUp abaixo
        popUpCedPadrao(qtdCedTen, qtdCedFifty, qtdCedOneHundred)


# Faz o Controle de estoque de cédulas e o modifica na interface sempre que o botão de saque for pressionado
def main() -> None:
    global saldo, qtdCedTen, qtdCedFifty, qtdCedOneHundred, totced10, totced50, totced100
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3, qtdnewCed4
    global totcedNew200, totcedNew20, totcedNew5, totcedNew2
    if qtdCedTen >= 0 and qtdCedFifty >= 0 and qtdCedOneHundred >= 0 and qtdnewCed1 >= 0 and qtdnewCed2 >= 0 and qtdnewCed3 >= 0 and qtdnewCed4 >= 0:
        condicionalToDisplayPopUp()
        withdraw = saque()
        saldo = saldo - withdraw
        if saldo >= 0:
            totced50 = 0
            totced100 = 0
            totced10 = 0
            totcedNew200 = 0
            totcedNew20 = 0
            totcedNew5 = 0
            totcedNew2 = 0
            if 0 < withdraw != 0:
                interface_do_caixaQt.lcd_saldo.display(saldo)
                quantidadeDeNotasQt.le_qtd10.setText(str(qtdCedTen))
                quantidadeDeNotasQt.le_qtd50.setText(str(qtdCedFifty))
                quantidadeDeNotasQt.le_qtd100.setText(str(qtdCedOneHundred))
                quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
                seeTheQtdOfTheNewCedOnQt(newCed1, qtdnewCed1)
                seeTheQtdOfTheNewCedOnQt(newCed2, qtdnewCed2)
                seeTheQtdOfTheNewCedOnQt(newCed3, qtdnewCed3)
                seeTheQtdOfTheNewCedOnQt(newCed4, qtdnewCed4)


# As 7 funções abaixo fazem as reposições das cédulas no sistema.
def replenishTen() -> str:
    global qtdCedTen, saldo
    qtdCedAdd = int(replenishBankNotesQt.le_repor10.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        qtdCedTen = qtdCedTen + qtdCedAdd
        saldo = saldo + (qtdCedAdd * 10)
        quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
        return quantidadeDeNotasQt.le_qtd10.setText(str(qtdCedTen))


def replenishFifty() -> str:
    global qtdCedFifty, saldo
    qtdCedAdd = int(replenishBankNotesQt.le_repor50.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        qtdCedFifty = qtdCedFifty + qtdCedAdd
        saldo = saldo + (qtdCedAdd * 50)
        quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
        return quantidadeDeNotasQt.le_qtd50.setText(str(qtdCedFifty))


def replenishOneHundred() -> str:
    global qtdCedOneHundred, saldo
    qtdCedADD = int(replenishBankNotesQt.le_repor100.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        qtdCedOneHundred = qtdCedOneHundred + qtdCedADD
        saldo = saldo + (qtdCedADD * 100)
        quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
        return quantidadeDeNotasQt.le_qtd100.setText(str(qtdCedOneHundred))


def replenishTwoHundred() -> str:
    global saldo
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3, qtdnewCed4
    qtdCedADD = int(replenishBankNotesQt.le_repor200.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        if newCed1 == 200:
            qtdnewCed1 = qtdnewCed1 + qtdCedADD
            saldo = saldo + (qtdCedADD * 200)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd200.setText(str(qtdnewCed1))
        elif newCed2 == 200:
            qtdnewCed2 = qtdnewCed2 + qtdCedADD
            saldo = saldo + (qtdCedADD * 200)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd200.setText(str(qtdnewCed2))
        elif newCed3 == 200:
            qtdnewCed3 = qtdnewCed3 + qtdCedADD
            saldo = saldo + (qtdCedADD * 200)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd200.setText(str(qtdnewCed3))
        elif newCed4 == 200:
            qtdnewCed4 = qtdnewCed4 + qtdCedADD
            saldo = saldo + (qtdCedADD * 200)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd200.setText(str(qtdnewCed4))


def replenishTwenty() -> str:
    global saldo
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3, qtdnewCed4
    qtdCedADD = int(replenishBankNotesQt.le_repor20.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        if newCed1 == 20:
            qtdnewCed1 = qtdnewCed1 + qtdCedADD
            saldo = saldo + (qtdCedADD * 20)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd20.setText(str(qtdnewCed1))
        elif newCed2 == 20:
            qtdnewCed2 = qtdnewCed2 + qtdCedADD
            saldo = saldo + (qtdCedADD * 20)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd20.setText(str(qtdnewCed2))
        elif newCed3 == 20:
            qtdnewCed3 = qtdnewCed3 + qtdCedADD
            saldo = saldo + (qtdCedADD * 20)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd20.setText(str(qtdnewCed3))
        elif newCed4 == 20:
            qtdnewCed4 = qtdnewCed4 + qtdCedADD
            saldo = saldo + (qtdCedADD * 20)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd20.setText(str(qtdnewCed4))


def replenishTwo() -> str:
    global saldo
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3, qtdnewCed4
    qtdCedADD = int(replenishBankNotesQt.le_repor2.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        if newCed1 == 2:
            qtdnewCed1 = qtdnewCed1 + qtdCedADD
            saldo = saldo + (qtdCedADD * 2)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd2.setText(str(qtdnewCed1))
        elif newCed2 == 2:
            qtdnewCed2 = qtdnewCed2 + qtdCedADD
            saldo = saldo + (qtdCedADD * 2)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd2.setText(str(qtdnewCed2))
        elif newCed3 == 2:
            qtdnewCed3 = qtdnewCed3 + qtdCedADD
            saldo = saldo + (qtdCedADD * 2)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd2.setText(str(qtdnewCed3))
        elif newCed4 == 2:
            qtdnewCed4 = qtdnewCed4 + qtdCedADD
            saldo = saldo + (qtdCedADD * 2)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd2.setText(str(qtdnewCed4))


def replenishFive() -> str:
    global saldo
    global newCed1, newCed2, newCed3, newCed4, saldo, qtdnewCed1, qtdnewCed2, qtdnewCed3, qtdnewCed4
    qtdCedADD = int(replenishBankNotesQt.le_repor5.text())
    isNumeric = str(addCedulaQt.le_addCed.text()).isnumeric()
    if isNumeric:
        if newCed1 == 5:
            qtdnewCed1 = qtdnewCed1 + qtdCedADD
            saldo = saldo + (qtdCedADD * 5)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd5.setText(str(qtdnewCed1))
        elif newCed2 == 5:
            qtdnewCed2 = qtdnewCed2 + qtdCedADD
            saldo = saldo + (qtdCedADD * 5)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd5.setText(str(qtdnewCed2))
        elif newCed3 == 5:
            qtdnewCed3 = qtdnewCed3 + qtdCedADD
            saldo = saldo + (qtdCedADD * 5)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd5.setText(str(qtdnewCed3))
        elif newCed4 == 5:
            qtdnewCed4 = qtdnewCed4 + qtdCedADD
            saldo = saldo + (qtdCedADD * 5)
            quantidadeDeNotasQt.le_totalSaldo.setText(str(saldo))
            return quantidadeDeNotasQt.le_qtd5.setText(str(qtdnewCed4))


# botões de funcionamento e conectados as suas funções.
interface_do_caixaQt.pb_saqueValorDigitado.clicked.connect(main)
interface_do_caixaQt.pb_100reais.clicked.connect(centenas)
interface_do_caixaQt.pb_500reais.clicked.connect(quinhentos)
interface_do_caixaQt.pb_1000reais.clicked.connect(mil)
interface_do_caixaQt.pb_limpar.clicked.connect(clean)
replenishBankNotesQt.pb_addCedula50.clicked.connect(replenishFifty)
quantidadeDeNotasQt.pb_repor.clicked.connect(replenishBankNotesQt.show)
replenishBankNotesQt.pb_addCedula10.clicked.connect(replenishTen)
replenishBankNotesQt.pb_addCedula100.clicked.connect(replenishOneHundred)
replenishBankNotesQt.pb_addCedula200.clicked.connect(replenishTwoHundred)
replenishBankNotesQt.pb_addCedula20.clicked.connect(replenishTwenty)
replenishBankNotesQt.pb_addCedula2.clicked.connect(replenishTwo)
replenishBankNotesQt.pb_addCedula5.clicked.connect(replenishFive)
quantidadeDeNotasQt.pb_addCedula.clicked.connect(addCedulaQt.show)
addCedulaQt.pb_addCed.clicked.connect(addNovasCedulas)

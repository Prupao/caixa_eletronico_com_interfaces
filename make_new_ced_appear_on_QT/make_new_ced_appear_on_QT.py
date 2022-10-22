from caixa_eletronico.interfaces_e_modulos import *


# A função abaixo faz com que as cédulas novas adicionadas apareçam na interface
def makeTheNewCedAppearOnQt(newCed: int) -> None:
    if newCed == 200:
        interface_do_caixaQt.qtd200Label.setText("qtd200")
        interface_do_caixaQt.qtd200LineEdit.setFrame(True)
        interface_do_caixaQt.lb_200reais.setText("200 REAIS")
        quantidadeDeNotasQt.lb_200reais.setText("200 REAIS")
        quantidadeDeNotasQt.le_qtd200.setFrame(True)
        replenishBankNotesQt.lb_200reais.setText("200 REAIS")
        replenishBankNotesQt.le_repor200.setEnabled(True)
        replenishBankNotesQt.le_repor200.setFrame(True)
        replenishBankNotesQt.pb_addCedula200.setFlat(False)
        replenishBankNotesQt.pb_addCedula200.setText("Repor cédula")
    elif newCed == 20:
        interface_do_caixaQt.qtd20Label.setText("qtd20")
        interface_do_caixaQt.qtd20LineEdit.setFrame(True)
        interface_do_caixaQt.lb_20reais.setText("20 REAIS")
        quantidadeDeNotasQt.lb_20reais.setText("20 REAIS")
        quantidadeDeNotasQt.le_qtd20.setFrame(True)
        replenishBankNotesQt.lb_20reais.setText("20 REAIS")
        replenishBankNotesQt.le_repor20.setEnabled(True)
        replenishBankNotesQt.le_repor20.setFrame(True)
        replenishBankNotesQt.pb_addCedula20.setFlat(False)
        replenishBankNotesQt.pb_addCedula20.setText("Repor cédula")
    elif newCed == 5:
        interface_do_caixaQt.qtd5Label.setText("qtd5")
        interface_do_caixaQt.qtd5LineEdit.setFrame(True)
        interface_do_caixaQt.lb_5reais.setText("5 REAIS")
        quantidadeDeNotasQt.lb_5reais.setText("5 REAIS")
        quantidadeDeNotasQt.le_qtd5.setFrame(True)
        replenishBankNotesQt.lb_5reais.setText("5 REAIS")
        replenishBankNotesQt.le_repor5.setEnabled(True)
        replenishBankNotesQt.le_repor5.setFrame(True)
        replenishBankNotesQt.pb_addCedula5.setFlat(False)
        replenishBankNotesQt.pb_addCedula5.setText("Repor cédula")
    elif newCed == 2:
        interface_do_caixaQt.qtd2Label.setText("qtd2")
        interface_do_caixaQt.qtd2LineEdit.setFrame(True)
        interface_do_caixaQt.lb_2reais.setText("2 REAIS")
        quantidadeDeNotasQt.lb_2reais.setText("2 REAIS")
        quantidadeDeNotasQt.le_qtd2.setFrame(True)
        replenishBankNotesQt.lb_2reais.setText("2 REAIS")
        replenishBankNotesQt.le_repor2.setEnabled(True)
        replenishBankNotesQt.le_repor2.setFrame(True)
        replenishBankNotesQt.pb_addCedula2.setFlat(False)
        replenishBankNotesQt.pb_addCedula2.setText("Repor cédula")

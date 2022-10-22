from caixa_eletronico.interfaces_e_modulos import *


def centenas() -> int:
    if interface_do_caixaQt.le_digiteValor.text() == '':
        interface_do_caixaQt.le_digiteValor.setText('100')
    elif interface_do_caixaQt.le_digiteValor.text() != '':
        b = int(interface_do_caixaQt.le_digiteValor.text())
        interface_do_caixaQt.le_digiteValor.setText('100')
        c = int(interface_do_caixaQt.le_digiteValor.text())
        sum = b + c
        return interface_do_caixaQt.le_digiteValor.setText(str(sum))


def quinhentos() -> int:
    if interface_do_caixaQt.le_digiteValor.text() == '':
        interface_do_caixaQt.le_digiteValor.setText('500')
    elif interface_do_caixaQt.le_digiteValor.text() != '':
        b = int(interface_do_caixaQt.le_digiteValor.text())
        interface_do_caixaQt.le_digiteValor.setText('500')
        c = int(interface_do_caixaQt.le_digiteValor.text())
        sum = b + c
        return interface_do_caixaQt.le_digiteValor.setText(str(sum))


def mil() -> int:
    if interface_do_caixaQt.le_digiteValor.text() == '':
        interface_do_caixaQt.le_digiteValor.setText('1000')
    elif interface_do_caixaQt.le_digiteValor.text() != '':
        b = int(interface_do_caixaQt.le_digiteValor.text())
        interface_do_caixaQt.le_digiteValor.setText('1000')
        c = int(interface_do_caixaQt.le_digiteValor.text())
        sum = b + c
        return interface_do_caixaQt.le_digiteValor.setText(str(sum))

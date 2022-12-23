from interfaces_e_modulos import *


def valores(valor: int) -> int:
    valor = str(valor)
    if interface_do_caixaQt.le_digiteValor.text() == '':
        interface_do_caixaQt.le_digiteValor.setText(valor)
    elif interface_do_caixaQt.le_digiteValor.text() != '':
        b = int(interface_do_caixaQt.le_digiteValor.text())
        interface_do_caixaQt.le_digiteValor.setText(valor)
        c = int(interface_do_caixaQt.le_digiteValor.text())
        sum = b + c
        return interface_do_caixaQt.le_digiteValor.setText(str(sum))

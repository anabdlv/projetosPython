from contas import Conta
import datetime


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo, limite):
        Conta.__init__(self, clientes, numero, saldo)
        self.limite = limite


def sacar(self, valor):
    if (self.saldo + self.limite) < valor:
        return False
    else:
        self.saldo -= valor
        return True
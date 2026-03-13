class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo=0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"--- Conta {self.id} criada com sucesso. Saldo atual de {self.saldo:,.2f} ---")

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."
    
    def depositar(self, valor):
        if valor <= 0:
            print(f"- Depósito de R${valor:,.2f} na conta {self.id} \033[1;31mNEGADO\033[m, valor inválido!")
        else:
            self.saldo += valor
            print(f"-> Depósito de R${valor:,.2f}  na conta {self.id} \033[1;32mautorizado\033[m!")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"- Saque de R${valor:,.2f} na conta {self.id} \033[1;31mNEGADO\033[m, saldo insuficiente!")
        else:
            self.saldo -= valor
            print(f"-> Saque de R${valor:,.2f}  na conta {self.id} \033[1;32mautorizado\033[m!")


c1 = ContaBancaria(514144, "Valdir", 3000)
c1.depositar(0)
c1.sacar(2000)
print(c1)

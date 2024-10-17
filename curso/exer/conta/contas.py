import abc

class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractmethod
    def sacar(self, valor): ...
        
    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'foi depositado {valor:.2f}')
        print('--')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'
            
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        
class ContaPoupanca(Conta):
    def sacar(self, valor): 
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'foi sacado {valor:.2f}')
            return self.saldo
        
        print('Saldo insuficiente')
        self.detalhes('Saque negado')
    
    
class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
    def sacar(self, valor): 
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'foi sacado {valor:.2f}')
            return self.saldo
        
        print('Saldo insuficiente')
        print(f'Seu limite é {-self.limite}')
        self.detalhes('Saque negado')
        return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r})'
        return f'{class_name}{attrs}'
    
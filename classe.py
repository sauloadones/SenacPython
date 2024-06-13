import datetime as data
class ContaBancaria:
    def __init__(self):
        self._tempo = data.datetime.now()
        self._tempo = self._tempo.strftime("%I:%M:%S")
        self._ids = []
        self._saldos = []
        self._titulares = []
        self._senhas = []
        self._valores = []
        self._depositos = []
        self._hora = []
        self._horarios = []
    def get_senhas(self):
        return self._senhas

    def get_ids(self):
        return self._ids
        
    def get_saldos(self):
        return self._saldos
    
    def get_titulares(self):
        return self._titulares
    
    def set_id(self, id):
        if not isinstance(id, int):
            raise ValueError("Valor não é inteiro")
        self._ids.append(id)
        
    def set_saldo(self, saldo):
        if not isinstance(saldo, float):
            raise ValueError("Valor não é float")
        self._saldos.append(saldo)
        
    def set_titular(self, titular):
        if not isinstance(titular, str):
            raise ValueError("Valor não é string")
        self._titulares.append(titular)
    def set_senha(self, senha):
        if not isinstance(senha, str):
            raise ValueError('Valor não é string')
        self._senhas.append(senha)
    def depositar(self, id, valor):
        if not isinstance(valor, float):
            raise ValueError("Valor não é float")
        index = self._ids.index(id)
        self._saldos[index] += valor
        self._hora.append(self._tempo)
        self._horarios.insert(index, self._hora)
        self._valores.append(valor)
        self._depositos.insert(index, self._valores)
    
    def sacar(self, id, valor):
        if not isinstance(valor, float):
            raise ValueError("Valor não é float")
        index = self._ids.index(id)
        if self._saldos[index] >= valor:
            self._saldos[index] -= valor
            self._hora.append(self._tempo)
            self._horarios.insert(index, self._hora)
            self._valores.append(valor)
            self._depositos.insert(index, self._valores)
        else:
            raise ValueError("Saldo insuficiente")
    
    def get_saldo_pelo_id(self, id):
        index = self._ids.index(id)
        return self._saldos[index]
    
    def get_titular_pelo_id(self, id):
        index = self._ids.index(id)
        return self._titulares[index]
    
    def get_id_pelo_titular(self, id):
        index = self._titulares.index(id)
        return self._ids[index]
    
    def get_deletar_conta(self, id):
        index = self._ids.index(id)
        self._ids.pop(index)
        self._titulares.pop(index)
        self._saldos.pop(index)
    def get_senha_pelo_id(self, id):
        index = self._ids.index(id)
        return self._senhas[index]
    
    def verificar_senha(self,id, senha):
        index = self._ids.index(id)
        if self._senhas[index] == senha:
            return 1
        else: 
            return 0
    def transferencia(self, id, id2, valor, saldo):
        index1 = self._ids.index(id)
        index2 = self._ids.index(id2)
        self._saldos[index1] -= valor
        self._saldos[index2] -= saldo
        self._hora.append(self._tempo)
        self._horarios.insert(index1, self._hora)
        self._hora.append(self._tempo)
        self._horarios.insert(index2, self._hora)
        self._valores.append(valor)
        self._depositos.insert(index1, self._valores)
        self._valores.append(valor)
        self._depositos.insert(index2, self._valores)
    def historicovalores(self, id):
        index = self._ids._index(id)
        return print(f"{self._depositos[index]}:{self._horarios[index]}")
        
    
    
   
    

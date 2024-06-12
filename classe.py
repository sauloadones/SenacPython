class ContaBancaria:
    def __init__(self):
        self._ids = []
        self._saldos = []
        self._titulares = []

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
    
    def depositar(self, id, valor):
        if not isinstance(valor, float):
            raise ValueError("Valor não é float")
        index = self._ids.index(id)
        self._saldos[index] += valor
    
    def sacar(self, id, valor):
        if not isinstance(valor, float):
            raise ValueError("Valor não é float")
        index = self._ids.index(id)
        if self._saldos[index] >= valor:
            self._saldos[index] -= valor
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
    
   
    

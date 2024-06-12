class ContaBancaria:
    def _init_(bank, id, saldo, titular, depositar, sacar):
       
        bank._id = id
        bank._saldo = saldo
        bank._titular = titular
        bank._depositar = depositar
        bank._sacar = sacar
       
    def get_id(bank):
       
        return bank._id
        
    def get_saldo(bank):
        
        return bank._saldo
    def get_titular(bank):
       
        return bank._titular
    def set_id(bank, id):
       
        if not isinstance(id, int):
            raise ValueError("Valor não é inteiro")
        bank._id = id
        
        
      
       
    def set_saldo(bank, saldo):
        
            if not isinstance(saldo, float):
                raise ValueError("Valor não e float")
            bank._saldo = saldo 
            
      
       
        
    def set_titular(bank, titular):
        
            if not isinstance(titular, str):
                raise ValueError("Valor não é string")
            bank._titular = titular
            
            
        
    def get_depositar(bank):
        
        return bank._depositar
        
    def set_depositar(bank, depositar):
        if not isinstance(depositar, float):
            raise ValueError("Valor não e float")
        bank._depositar = depositar 
        bank._saldo += bank._depositar
    def get_sacar(bank):
        bank._saldo -= bank._sacar
        return bank._sacar
        
    def set_sacar(bank, sacar):
        if not isinstance(sacar, float):
            raise ValueError("Valor não e float")
        bank._sacar = sacar
        bank._saldo -= bank._sacar
    
       




    
   
    

from SenacPython.SenacPython.classe1 import ContaBancaria

conta = ContaBancaria()

conta.set_saldo(0.00)
nomes = []
ids = []
saldos = []

# def depositar():
#    valor =  float(input("Digite o valor para depositar"))
#    x = conta.get_saldo()
#    total = x + valor 
#    conta.set_saldo(total)
# def sacar():
#    valor =  float(input("Digite o valor para depositar"))
#    x = conta.get_saldo()
#    total = x + valor
#    conta.set_saldo(total)
i = 0
while True:
   
   print("1 - Depositar na conta")
   print("2 - Sacar da Conta")
   print("3 - Check saldo da conta")
   print("4 - Adicionar uma conta")
   print("5 - Sair do Menu")
   
   op = input("Digite o numero do menu")

   if op == '1':
       try:
        check = int(input("Digite o id da sua conta"))
        if check in ids:
            valor = float(input("Digite o valor a ser digitado"))
            
            conta.set_depositar(valor)
            consulta = ids.index(check)
            saldos[consulta] = conta.get_saldo()

        else:
           raise ValueError
       except ValueError:
          print("Sua conta não esta cadastrada")
   elif op == '2':
        try:
            check = int(input("Digite o id da sua conta"))
            if check in ids:
                valor = float(input("Digite o valor a ser digitado"))
                consulta = ids.index(check)
                conta.set_sacar(valor)
                saldos[consulta] = conta.get_saldo()
            else:
                raise ValueError
        except ValueError:
          print("Sua conta não esta cadastrada")
       
   elif op == '3':
        try:
            check = int(input("Digite o id da sua conta"))
            if check in ids:
              
              
              consulta = ids.index(check)
              print("Seu saldo é", saldos[consulta])
            else:
                raise ValueError
        except ValueError:
          print("Sua conta não esta cadastrada")
      
   elif op == '4':
      
      try:
        nome = input("Digite seu nome")
        conta.set_titular(nome)
        i += 1
        conta.set_id(i)
        nomes.append(conta.get_titular())
        ids.append(conta.get_id())
        saldos.append(0)
        print("O id da sua conta é", conta.get_id())
        
      except ValueError:
         print("Tu digitou algo errado ai")
    
   elif op == '5':
      break
   
   else:
      print("Valor errado tente novamente")
    

   
   
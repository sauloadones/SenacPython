from classe import ContaBancaria
import os
conta = ContaBancaria()

i = 0
while True:
   print("1 - Depositar na conta")
   print("2 - Sacar da Conta")
   print("3 - Check saldo da conta")
   print("4 - Criar uma conta")
   print("5 - Para deletar a conta")
   print("6 - Para verificar o status da conta")
   print("7 - Para sair")
   
   op = input("Digite o numero do menu: ")

   if op == '1':
       try:
           check = int(input("Digite o id da sua conta: "))
           if check in conta.get_ids():
               valor = float(input("Digite o valor para depositar: "))
               conta.depositar(check, valor)
               qlq = conta.get_titular_pelo_id(check)
               print(f"Bem vindo! {qlq}\nDepósito realizado com sucesso!")
           else:
               raise ValueError
           
       except ValueError:
           print("Sua conta não está cadastrada ou valor inválido.")
     
   elif op == '2':
       try:
           check = int(input("Digite o id da sua conta: "))
           senha = input("Digite sua senha")
           verificacao = conta.get_senha_pelo_id(check)
           if check in conta.get_ids() and senha == verificacao:
               valor = float(input("Digite o valor para sacar: "))
               conta.sacar(check, valor)
               print(f"Bem vindo!!\n{conta.get_titular_pelo_id(check)}\nSaque realizado com sucesso!")
            
           elif senha != verificacao:
               print("Senha incorreta tente novamente")

           else:
               raise ValueError
       except ValueError:
           print("Saldo insuficiente")
         
     
   elif op == '3':
       try:
           check = int(input("Digite o id da sua conta: "))
           if check in conta.get_ids():
               saldo = conta.get_saldo_by_id(check)
               print(f"OLA {conta.get_id_by_titulares(check)}!\nSUA CONTA É:{check}!\n Seu atual saldo é{saldo}!")
           else:
               raise ValueError
       except ValueError:
           print("Sua conta não está cadastrada.")
    
   elif op == '4':
       try:
           i += 1
           nome = input("Digite seu nome: ")
           senha = input("Digite sua senha")
           conta.set_senha(senha)
           conta.set_titular(nome)
           conta.set_id(1000+i)
           conta.set_saldo(0.0)
           qlq = conta.get_id_pelo_titular(nome)
           print(f"O id da sua conta é: {qlq}")
           os.system('clear')
       except ValueError:
           print("Erro ao adicionar a conta, verifique os dados.")
       
   elif op == '5':
       check = int(input("Digite o id da sua conta"))
       try:
        if check in conta.get_ids():
           conta.get_deletar_conta(check)
           print("Sua conta foi deletada")
           print(conta.get_ids(), conta.get_titulares(), conta.get_saldos())
        else:
            raise ValueError
       except  ValueError:
           print("Sua conta nunca existiu ou voce ja deletou!")
    
   elif op == '6':
        check = int(input("Digite o id da sua conta"))
        try:
            if check  not in conta.get_ids():
                print("Sua conta não existe no nosso sistema")
            elif check in conta.get_ids():
                print("Sua conta existe no nosso sistema")
                nome = conta.get_titular_pelo_id(check)
                conta = conta.get_id_pelo_titular(nome)
                os.system('cls')
               
                print(f"O nome da sua conta é {nome}\nO codigo bancario é{conta}")
            else:
                raise ValueError
                
        except ValueError:
            print("Digite numeros")
            
            
           

    

   elif op == '7':
       break
   
   else:
       print("Valor errado, tente novamente.")
    

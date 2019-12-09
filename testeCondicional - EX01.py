
print ("1. Corinthians\n2.Flamengo")
resposta = int ( input("Qual o melhor time?: "))

if resposta == 1:
    print ("Você deve ser corinthiano")
else:
    if resposta == 2:
        print("Você deve torcer para o Flamengo")
    else: #tem esse else para impedir outro digito alem de 1 ou 2
        print("Digite 1 ou 2")
        
        
        
#input para forçar apertar enter para sair
input ("\n\n\n--- aperte enter")
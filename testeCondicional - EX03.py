#Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.

valor = int ( input("Entre com um valor: "))

if valor == 0:
    print ("O Valor não é positivo nem negativo, é 0.")
else:
    if valor < 0:
        print ("O valor é negativo")
    else:
        print ("O valor é positivo")


#input para forçar apertar enter para sair
input ("\n\n\n- aperte enter -")
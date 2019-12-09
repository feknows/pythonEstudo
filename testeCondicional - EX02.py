
#  Faça um programa que peça dois números e imprima o maior deles.

numero1 = float ( input("Entre com um número: "))
numero2 = float ( input ("Entre com outro número: "))

if numero1 == numero2:
    print ("os números sao iguais")
else:
    if numero2 < numero1:
        print ("O primeiro número, %d, é o maior" %numero1) 
    else:
        print ("O segundo número, %d, é o maior" %numero2)
        
#input para forçar apertar enter para sair
input ("\n\n\n--- aperte enter")
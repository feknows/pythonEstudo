#Exercício: Crie um programa em Python que peça dois números ao usuário.
#Em seguida, você vai mostrar a soma, subtração, multiplicação, divisão, 
#exponenciação e resto da divisão do primeiro número pelo segundo.

numero1 = int ( input('Digite um numero inteiro: ') )
numero2 = int ( input('Digite outro inteiro:') )

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2
exponenciacao = numero1 ** numero2
restoDivisao = numero1 % numero2


print ('\nSoma:                ',numero1,'+',numero2,'=',soma)
print ('Subtracao:           ',numero1,'+',numero2,'=',subtracao)
print ('Multiplicacao:       ',numero1,'+',numero2,'=',multiplicacao)
print ('Divisao:             ',numero1,'+',numero2,'=',divisao)
print ('Exponenciacao:       ',numero1,'+',numero2,'=',exponenciacao)
print ('Resto da Divisao:    ',numero1,'+',numero2,'=',restoDivisao)


#input para forçar apertar enter para sair
input ("\n\n\n--- aperte enter")
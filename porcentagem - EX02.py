#A loja percebeu que não quer dar 20% em tudo. Quer dar 20% em algumas coisas, 10% em outra,
# nada em outro produto e até 30% em alguns outros produtos.
#Crie um script em Python que pergunte o preço original e o desconto que deve ser concedido.
#Ele deve mostrar a tabela igual a do exercício anterior.

valorOriginal = float ( input('Digite o valor original do produto: R$'))
porcentagemDesconto = float ( input('Qual a porcentagem de desconto quer dar?'))
#transformar a porcentagem em numero decinal
porcentagemDesconto = porcentagemDesconto / 100

#tabela de exibição
print ('O Valor original do produto é : ',valorOriginal)
print ('Você ganhou R$',valorOriginal * porcentagemDesconto,' de desconto')
print ('Valor do produto com desconto é R$', valorOriginal * (1-porcentagemDesconto))

#input para forçar apertar enter para sair
input ("\n\n\n--- aperte enter")


#Explicação
#o usuário vai entrar com a porcentagem em desconto, por exemplo, 10% (digitando o valor 10)
#na hora de dar o desconto dividimos por 100. dizendo ao programa que desconto = desconto / 100
#desta maneira ele vira 0.1 ... Para fazer o contrário, dizendo qual o valor do desconto, é só 
# fazer o valor * (1 - desconto)


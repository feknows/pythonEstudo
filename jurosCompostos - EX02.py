#Dizer o valor inicial que ele deve investir, para ao final de 'm' meses ele tenha um 
#valor 'vf', supondo que este dinheiro esteja rendendo uma rentabilidade 'i' mensal,
#em porcentagem esse 'i'.

#Faça um programa que pede o valor final, o tanto de meses que vai ficar aplicado,
# a rentabilidade e o script mostre o valor inicial que ele deve investir para atingir tal objetivo.


valorFinal = float ( input('Valor final que deseja ter: R$'))

#tempo do investimento
mesesRendimento = int ( input('Quantidade de meses rendendo:'))
rentabilidadeMensal = float ( input ('Porcentagem mensal de redimento:'))

valorInicial = valorFinal / (rentabilidadeMensal+1)**mesesRendimento
print (valorInicial)
print('Valor inicial: '(valorInicial))
#input para forçar apertar enter para sair
input ("\n\n\n--- aperte enter")
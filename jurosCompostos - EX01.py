#formula:
#         Vf = Vi. (1+i)m
#Vf (valorFinal)- Valor final na poupança, ao término do tempo
#Vi (valorInicial) - Valor inicial que o cliente vai colocar na poupança
#i (rentabilidadeMensal) - Rentabilidade mensal (em porcentagem)
#m (mesesRendimento) - Tanto de meses que o dinheiro do cliente vai ficar rendendo

#O primeiro passo, é perguntar o montante inicial que vai ser investido.
# Vamos armazenar esse número na variável 'valorInicial'.
#Em seguida, perguntamos a rentabilidade mensal, em % e armazenar na variável 'rentabilidadeMensal'.
#Por fim, pergunte o número de meses que a aplicação vai ficar rendando,
# e armazene na variável inteira 'mesesRendimento'.


valorInicial = float( input ('Entre com o valor inicial a ser depositado: R$') )
rentabilidadeMensal = float ( input ('Entre com a rentabilidade mensal em porcentagem:') )

#transformar a porcentagem em numero decinal
rentabilidadeMensal = rentabilidadeMensal / 100

#tempo do investimento
mesesRendimento = int ( input ('Quantidade de meses que ficará rendendo:') ) 

valorFinal = valorInicial * (1+rentabilidadeMensal)**mesesRendimento
print ('valor apos ',mesesRendimento,'meses: R$',valorFinal)

#input para forçar apertar enter para sair
input ("\n\n\n--- aperte enter")
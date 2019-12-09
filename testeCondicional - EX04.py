#Crie um programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.


#entrada do genero pelo usuario
entreGenero = input ("Entre com o Genero, informado F ou M: ")

if entreGenero == 'F':
    print("Feminino")
else:
    if entreGenero == 'M':
        print ("Masculino")
    else:
        print ("Você não digitou M ou F")
#input para forçar apertar enter para sair
input ("\n\n\n- aperte enter -")
#Crie um programa em Python que peça a nota do aluno,
#que deve ser um float entre 0.00 e 10.0
#Se a nota for menor que 6.0, deve exibir a nota F.
#Se a nota for de 6.0 até 7.0, deve exibir a nota D.
#Se a nota for entre 7.0 e 8.0, deve exibir a nota C.
#Se a nota for entre 8.0 e 9.0, deve exibir a nota B.
#Por fim, se for entre 9.0 e 10.0, deve exibir um belo de um A.

notaAluno = float ( input("Entre com a nota do aluno: "))

if notaAluno < 6.0:
    print ("A nota do aluno é F")
elif notaAluno < 7.0:
    print ("A nota do aluno é D")
elif notaAluno < 8.0:
    print ("A nota do aluno é C")
elif notaAluno < 9.0:
    print ("A nota do aluno é B")
elif notaAluno <10.0:
    print ("A nota do aluno é A")
else:
    print("Nota invalida")
#input para segurar o arquivo aberto
input ("\n\n - aperte enter")
'''3 – Muitos professores preferem adotar modelos diferentes de provas quando dão aulas para turmas muito grandes. Por essa razão, a escola de inglês JoWell Sant’ana, em que todas as turmas são compostas por 50 alunos, solicitou que você criasse um sistema capaz de atender ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 alunos que têm número ímpar na chamada (1, 3, 5..., 47, 49) e depois as notas dos 25 alunos que têm número par (2, 4, 6..., 48, 50). O sistema deve calcular e exibir a média de cada uma das metades da sala e informar, ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam, ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.'''




print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES!!!")
alunos = 50
alunos_impares = 0
soma_das_notas = 0.0
for i in range(1, alunos +1 ):
    if i % 2 != 0:
         nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: ".format(i)))
         alunos_impares += 1
         soma_das_notas += nota
    media_totali = soma_das_notas / alunos_impares
print("\nA Média das notas dos alunos Impares são: {:.1f}".format(media_totali))


print("\nVOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES!!!")
alunosp = 50
alunos_pares = 0
soma_das_notasp = 0.0
for p in range(2, alunosp + 1,):
    if p % 2 != 1:
            nota = float(input("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO  {}: ".format(p)))
            alunos_pares += 1
            soma_das_notasp += nota
    media_totalp = soma_das_notasp / alunos_pares
print("\nA Média das notas dos alunos Pares são: {:.1f}".format(media_totalp))

if media_totali > media_totalp:
    print("\nAlunos Impares obtiveram maior nota media em relação aos alunos Pares.")
elif media_totali == media_totalp:
    print("\n Todos os alunos tiveram nota maxima, informar a direção por suposto plagio nas provas!")

else:
    print("\nAlunos Pares obtiveram maior nota media em relação aos alunos Impares.")












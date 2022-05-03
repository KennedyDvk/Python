''' 1 – Você foi procurado por um aluno do curso de Produção Multimídia do FIAP ON para desenvolver um trabalho em parceria: um serviço em que as pessoas possam usar um estúdio profissional para gravar seus vídeos para o YouTube com máxima qualidade. O serviço ganha dinheiro por meio de um sistema de assinaturas e de um bônus calculado por uma porcentagem sobre o faturamento que o canal do cliente obteve ao longo do ano.

Sua tarefa é criar um algoritmo que receba o tipo de assinatura do cliente, o faturamento anual dele e que calcule e exiba qual o valor do bônus que o cliente deve pagar a vocês. A tabela abaixo mostra a porcentagem de acordo com cada nível de assinatura:'''



print("assinaturas Registradas no periodo de 1 ano!")


print('''        
                  Basic
                  Silver
                  Gold
                  Platinum''')

select = str(input("\nSelecione qual alternativa deseja calcular: "))
if select.upper() == 'BASIC':

    assinatura_basic = float(input("Digite quantas assinaturas foram registradads: "))
    faturamento = float(input("Digite o Faturamento: "))
    vbp = faturamento * 30 / 100
    print("o Bonus da equip Fiap on é {}".format(vbp))

elif select.upper() == 'SILVER':
    assinatura_silver = float(input("Digite quantas assinaturas foram registradads: "))
    faturamento = float(input("Digite o Faturamento: "))
    vsp = faturamento * 20 / 100
    print("o Bonus da equip Fiap on é {}".format(vsp))

elif select.upper() == 'GOLD':
    assinatura_gold = float(input("Digite quantas assinaturas foram registradads: "))
    faturamento = float(input("Digite o Faturamento: "))
    vgp = faturamento * 10 / 100
    print("o Bonus da equip Fiap on é {}".format(vgp))

elif select.upper() == 'PLATINUM':
    assinatura_platinum = float(input("Digite quantas assinaturas foram registradads: "))
    faturamento = float(input("Digite o Faturamento: "))
    vpp = faturamento * 5 / 100
    print("o Bonus da equip Fiap on é {}".format(vpp))

else:
    print("OPÇÃO INVALIDA!!!")
print("-----Fim-----")
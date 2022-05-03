'''2 – Os alunos da sua turma fizeram uma votação para escolher qual dia da semana é o melhor para a realização das lives. Desenvolva um programa em que o usuário informe a quantidade de votos que cada um dos 5 dias da semana (segunda-feira, terça-feira, quarta-feira, quinta-feira e sexta-feira) obtiveram, verifique e exiba qual dia foi o escolhido.'''



print("Votação para escolher qual dia da semana haverá as lives!")

print('''\n        
                  SEGUNDA
                  TERÇA
                  QUARTA
                  QUINTA
                  SEXTA
                  ''')



voto1 = input("Informe qual dia da semana você gostaria de ter a Live: ")

voto2 = input("Informe qual dia da semana você gostaria de ter a Live: ")

voto3 = input("Informe qual dia da semana você gostaria de ter a Live: ")

voto4 = input("Informe qual dia da semana você gostaria de ter a Live: ")

voto5 = input("Informe qual dia da semana você gostaria de ter a Live: ")

segunda = 0

terça = 0

quarta = 0

quinta = 0

sexta = 0

if voto1.upper()=="SEGUNDA":
    segunda = segunda + 1

elif voto1.upper()=="TERÇA":
    terça = terça + 1

elif voto1.upper()=="QUARTA":
    quarta = quarta + 1

elif voto1.upper()=="QUINTA":
    quinta = quinta + 1

elif voto1.upper()=="SEXTA":
    sexta = sexta + 1

else:
    print("voto invalido")


if voto2.upper()=="SEGUNDA":
    segunda = segunda + 1

elif voto2.upper()=="TERÇA":
    terça = terça + 1

elif voto2.upper()=="QUARTA":
    quarta = quarta + 1

elif voto2.upper()=="QUINTA":
    quinta = quinta + 1

elif voto2.upper()=="SEXTA":
    sexta = sexta + 1

else:
    print("voto invalido")

if voto3.upper()=="SEGUNDA":
    segunda = segunda + 1

elif voto3.upper()=="TERÇA":
    terça = terça + 1

elif voto3.upper()=="QUARTA":
    quarta = quarta + 1

elif voto3.upper()=="QUINTA":
    quinta = quinta + 1

elif voto3.upper()=="SEXTA":
    sexta = sexta + 1

else:
    print("voto invalido")


if voto4.upper()=="SEGUNDA":
    segunda = segunda + 1

elif voto4.upper()=="TERÇA":
    terça = terça + 1

elif voto4.upper()=="QUARTA":
    quarta = quarta + 1

elif voto4.upper()=="QUINTA":
    quinta = quinta + 1

elif voto4.upper()=="SEXTA":
    sexta = sexta + 1

else:
    print("voto invalido")

if voto5.upper()=="SEGUNDA":
    segunda = segunda + 1

elif voto5.upper()=="TERÇA":
    terça = terça + 1

elif voto5.upper()=="QUARTA":
    quarta = quarta + 1

elif voto5.upper()=="QUINTA":
    quinta = quinta + 1

elif voto5.upper()=="SEXTA":
    sexta = sexta + 1

else:
    print("voto invalido")

print("SEGUNDA: {}\nTERCA: {}\nQUARTA: {}\nQUINTA: {}\nSEXTA: {}".format(segunda, terça, quarta, quinta, sexta))

if segunda > terça and segunda > quarta and segunda > quinta and segunda > sexta:
    print("o Dia escolhido para as lives foi Segunda - Feira")

elif terça > segunda and terça > quarta and terça > quinta and terça > sexta:
    print("o Dia escolhido para as lives foi Terça - Feira")

elif quarta > segunda and quarta > terça and quarta > quinta and quarta > sexta:
    print("o Dia escolhido para as lives foi Quarta - Feira")

elif quinta > segunda and quinta > terça and quinta > quarta and quinta > sexta:
    print("o Dia escolhido para as lives foi Quinta - Feira")

elif sexta > segunda and sexta > terça and sexta > quarta and sexta > quinta:
    print("o Dia escolhido para as lives foi Sexta - Feira")

else:
    print("houve empate, por favor avisar a Direção ")
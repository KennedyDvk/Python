'''Desafio

O desafio será a criação de um ranking de criticidade de violações/vazamentos “breaches” de dados pessoais em serviços de internet, por meio dos critérios de dados comprometidos como senha, ajuda da senha, número do telefone, nomes, e-mail e data do vazamento.
deverá ser elaborado com o que o aluno aprendeu até o momento...'''



lista = ["\n Avvo: Aproximadamente em dezembro de 2019, uma suposta violação de dados do serviço de diretório de advogados Avvo foi publicada em um fórum de hackers online e usada\n em um golpe de extorsão (é possível que a exposição seja anterior a isso). Os dados continham 4,1 milhões de endereços de e-mail exclusivos ao lado de hashes SHA-1,\n provavelmente representando senhas de usuários. Várias tentativas de contato com a Avvo ao longo de uma semana foram malsucedidas e a autenticidade dos dados acabou\n sendo verificada com assinantes comuns da Avvo e HIBP.\n Dados Comprometidos:e-mail, Senhas."

,"\n Nvidia: Em fevereiro de 2022, a empresa de microchips NVIDIA sofreu uma violação de dados que expôs credenciais de funcionários e código proprietário.\n Os dados afetados incluíam mais de 70 mil endereços de e-mail de funcionários e hashes de senha NTLM, muitos dos quais foram posteriormente quebrados e divulgados\n na comunidade de hackers.\n Dados Comprometidos: credenciais de funcionários, código proprietário, endereços de e-mail, hashes de senha "

,"\n Facebook Em abril de 2021, um grande conjunto de dados de mais de 500 milhões de usuários do Facebook foi disponibilizado gratuitamente para download.\n Abrangendo aproximadamente 20% dos assinantes do Facebook, os dados foram supostamente obtidos explorando uma vulnerabilidade que o Facebook informa que corrigiu\n em agosto de 2019. O principal valor dos dados é a associação de números de telefone a identidades; enquanto cada registro incluía telefone, apenas 2,5 milhões\n continham um endereço de e-mail. A maioria dos registros continha nomes e gêneros, com muitos também incluindo datas de nascimento,localização,status de relacionamento \n e empregador.\n Dados comprometidos: números de telefone, identidades, endereço de e-mail, nomes, datas de nascimento, localização,status de relacionamento, empregador.",

"\n RedDoorz: Em setembro de 2020, a plataforma de gerenciamento e reservas de hotéis RedDoorz sofreu uma violação de dados que expôs mais de 5,8 milhões de contas\n de usuários. Os dados violados incluíam nomes, endereços de e-mail, números de telefone, sexos, datas de nascimento e senhas armazenadas como hashes bcrypt.\n Os dados foram fornecidos ao HIBP por uma fonte que solicitou que fossem atribuídos a ""white_peacock@riseup.net""\n Dados Comprometidos: contas de usuários, nomes,  e-mail,números de telefone, sexos, datas de nascimento, senhas.",

"\n Robinhood: Em novembro de 2021, a plataforma de negociação online Robinhood sofreu uma violação de dados depois que um representante de atendimento ao cliente\n foi projetado socialmente. O incidente expôs mais de 5 milhões de endereços de e-mail de clientes e 2 milhões de nomes de clientes. Os dados foram fornecidos\n ao HIBP por uma fonte que solicitou que fossem atribuídos a ""'Jarand Moen Romtviet'""\n Dados comprometidos: e-mail, nomes. ",

"\n Myspace: Em aproximadamente 2008, o MySpace sofreu uma violação de dados que expôs quase 360 milhões de contas. Em maio de 2016, os dados foram colocados à venda\n no site do mercado negro"""'Real Deal'" e incluíam endereços de e-mail, nomes de usuário e hashes SHA1 dos primeiros 10 caracteres da senha convertidos em minúsculas\n e armazenados sem sal. A data exata da violação é desconhecida, mas a análise dos dados sugere que foram 8 anos antes de serem divulgados.\n Dados comprometidos: e-mail, nome, ajuda de senha."]



for ranking in lista:
    print(ranking)

sites = ["Avvo", "Nvidia", "Facebook","RedDoorz","Robinhood","Myspace"]
print(sites)


senha = 2
ajuda_senha = 1
numero_de_telefone = 1
nomes = 1
email = 1
data_do_vazamento = 2

Avvo = [email,senha,data_do_vazamento]
lista1 = sum(Avvo)

RedDoorz = [numero_de_telefone, email, nomes,data_do_vazamento,senha]
lista2 = sum(RedDoorz)

Facebook = [senha, ajuda_senha, numero_de_telefone, nomes, email, data_do_vazamento]
lista3 = sum(Facebook)

Nvidia = [nomes, email, data_do_vazamento]
lista4 = sum(Nvidia)

Robinhood = [email,nomes,data_do_vazamento]
lista5 = sum(Robinhood)

Myspace = [email,nomes,ajuda_senha,data_do_vazamento]
lista6 = sum(Myspace)

if lista1>lista2 and lista1>lista3 and lista1>lista4 and lista1>lista5:
    print("\nO site da Avvo teve o maior nivel de criticidade no vazamento de dados.")
elif lista2>lista1 and lista2>lista3 and lista2>lista4 and lista2>lista5:
    print("\nO site da RedDoorz teve o maior nível de criticidade no vazamento de dados.")
elif lista3>lista1 and lista3>lista2 and lista3>lista4 and lista3>lista5:
    print("\nO site do Facebook teve o maior nível de criticidade no vazamento de dados.")
elif lista4>lista1 and lista4>lista2 and lista4>lista3 and lista4>lista5:
    print("\nO site do Nvidia teve o maior nível de criticidade no vazamento de dados.")
elif lista5>lista1 and lista5>lista2 and lista5>lista3 and lista5>lista4:
    print("\nO site do Robinhood teve o maior nível de criticidade no vazamento de dados.")
elif lista6>lista1 and lista6>lista2 and lista6>lista3 and lista6>lista4 and lista>lista5:
    print("\nO site do Myspace teve o maior nível de criticidade no vazamento de dados.")
print("_____Fim_____")

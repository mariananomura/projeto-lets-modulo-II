#{nome: 'Ricardo Meca' , e-mail: 'ricardo@lets.com', genero: ['rock', 'samba'], instrumentos: ['violino', 'flauta', 'pandero']}
import json

banco_de_dados = []

def registra_banco_de_dados(banco_de_dados: list):
    with open('banco_de_dados.json', 'w', encoding='utf-8') as banco:
        json.dump(banco_de_dados, banco, ensure_ascii=False)


def cria_novo_usuario():
    novo_usuario = {}
    return novo_usuario

def cadastro_nome(novo_usuario: dict):
    nome_usuario = input("Insira seu nome completo (apenas letras e espaços):").lower()
    novo_usuario["nome"] = nome_usuario
    return novo_usuario
    #Cadastrar músicos Nome (string contendo apenas letras e espaço) 
def cadastro_email(novo_usuario: dict):
    email_usuario = input("Insira seu e-mail:")
    novo_usuario["email"] = email_usuario
    return novo_usuario
    # E-mail (string contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, 
    #obrigatoriamente, exatamente 1 arroba (@))
    
def cadastro_generos(novo_usario:dict):
    generos = []
    quantidade_generos = int(input("Quantos gêneros músicais deseja incluir?"))
    generos_adicionados = 0
    while generos_adicionados < quantidade_generos:
        adicionando = input("Digite o gênero musicial:")
        generos.append(adicionando)
        generos_adicionados+=1
    novo_usuario["generos"] = generos
    return novo_usario
    #Gêneros musicais (mínimo 1, usuário pode digitar quantos forem necessários)

def cadastro_instrumentos(novo_usario:dict):
    instrumentos = []
    quantidade_instrumentos = int(input("Quantos instrumentos deseja incluir?"))
    instrumentos_adicionados = 0
    while instrumentos_adicionados < quantidade_instrumentos:
        adicionando = input("Digite o gênero musicial:")
        instrumentos.append(adicionando)
        instrumentos_adicionados+=1
    novo_usuario["instrumentos"] = instrumentos
    return novo_usario

    #Instrumentos (mínimo 1, usuário pode digitar quantos forem necessários)
    ...

def busca():
    #Na busca o usuário deve passar pelo menos 1 das opções: nome, e-mail, gênero (digitar apenas 1) ou instrumento (digitar apenas 1). 
    # O usuário deve selecionar se os resultados devem bater com todas as informações digitadas ou pelo menos uma 
    # (ex: se o usuário digitar nome e instrumento, a busca pode ser por resultados contendo o nome E o instrumento vs o nome OU o instrumento).
    ...

def modifica_cadastro():
    #Na modificação de um usuário, será feita uma busca especificamente por e-mail. 
    # É permitido adicionar ou remover gêneros e instrumentos. 
    # Não é permitido mudar nome ou e-mail.
    ...

def montar_banda():
    #Na opção de montar bandas, o usuário deverá informar o número desejado de músicos, 
    #o instrumento de cada um dos músicos (1 por músico) e 1 gênero. 
    #O programa deverá exibir na tela todas as combinações possíveis de músicos (e-mail + instrumento).
    ...

print("INICIANDO NOVO CADASTRO:")


novo_usuario = cria_novo_usuario()

cadastro_nome(novo_usuario)
cadastro_email(novo_usuario)
cadastro_generos(novo_usuario)
cadastro_instrumentos(novo_usuario)
banco_de_dados.append(novo_usuario)

registra_banco_de_dados(banco_de_dados)


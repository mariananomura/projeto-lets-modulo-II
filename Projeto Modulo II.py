import json

from sympy import re


def abre_banco_lista():
    with open('banco_de_dados.json', 'r', encoding='utf-8') as banco:
        banco = list(json.load(banco))
    return banco


def registra_banco_de_dados(novo_usuario:dict):   
    with open('banco_de_dados.json', 'r', encoding='utf-8') as banco:
        banco = list(json.load(banco))
        banco.append(novo_usuario)

    with open('banco_de_dados.json', 'w', encoding='utf-8') as dados:
        json.dump(banco, dados, ensure_ascii=False)


def cria_novo_usuario():
    novo_usuario = {}
    return novo_usuario


def cadastro_nome(novo_usuario:dict):
    nome_usuario = input("Insira seu nome completo (apenas letras e espaços): ").lower()

    for letra in nome_usuario:
        while letra.isalpha() == False and letra != ' ':
            print("Nome inválido: utilize apenas letras e números!")
            nome_usuario = input("Insira seu nome completo (apenas letras e espaços): ").lower()
        else:
            novo_usuario["nome"] = nome_usuario

    return novo_usuario
    #Cadastrar músicos Nome (string contendo apenas letras e espaço)

    
def cadastro_email(novo_usuario: dict):
    email_usuario = input("Insira seu e-mail: ").lower()
    caracteres_validos = ['@','.', '_']
    while '@' not in email_usuario:
        print("Endereço de e-mail inválido!@")
        email_usuario = input("Insira seu e-mail: ").lower()
    for caractere in email_usuario:
        if caractere.isalnum() == False:
            if caractere not in caracteres_validos:
                print("Endereço de e-mail inválido!??")
                cadastro_email(novo_usuario) 
            
        else:
            novo_usuario["email"] = email_usuario
            return novo_usuario




    # E-mail (string contendo apenas letras, underscore (_), ponto (.), dígitos numéricos e, 
    #obrigatoriamente, exatamente 1 arroba (@))

def validacao_email(novo_usuario: dict, banco_de_dados: list):
    for usuario in banco_de_dados:
        if novo_usuario["email"] == usuario["email"]:
            print ("E-mail de usuário já cadastrado. Utilize outro e-mail para o cadastro.")
            cadastro_email(novo_usuario)
        else:
            pass

def cadastro_generos(novo_usario:dict):
    generos = []
    quantidade_generos = int(input("Quantos gêneros músicais deseja incluir? "))
    generos_adicionados = 0
    while generos_adicionados < quantidade_generos:
        adicionando = input("Digite o gênero musicial: ").lower()
        generos.append(adicionando)
        generos_adicionados+=1
    novo_usuario["generos"] = generos
    return novo_usario
    #Gêneros musicais (mínimo 1, usuário pode digitar quantos forem necessários)


def cadastro_instrumentos(novo_usario:dict):
    instrumentos = []
    quantidade_instrumentos = int(input("Quantos instrumentos deseja incluir? "))
    instrumentos_adicionados = 0
    while instrumentos_adicionados < quantidade_instrumentos:
        adicionando = input("Digite o instrumento: ").lower()
        instrumentos.append(adicionando)
        instrumentos_adicionados+=1
    novo_usuario["instrumentos"] = instrumentos
    return novo_usario
    #Instrumentos (mínimo 1, usuário pode digitar quantos forem necessários)


def seleciona_parametro():
    parametros = []

    selecao_parametro = input("Selecione o parametro para sua busca:\n"
    "1 - Por nome.\n"
    "2 - Por e-mail.\n"
    "3 - Por gênero musical.\n"
    "4 - Por instrumento musical.\n")
    
    opcoes = {
        "1": "nome",
        "2": "email",
        "3": "generos",
        "4": "instrumentos"}

    return opcoes[selecao_parametro]


def descreve_parametro(selecao_parametro: str):

    opcoes = {
        "nome": "nome",
        "email": "e-mail",
        "generos": "gênero musical",
        "instrumentos": "instrumento musical"
        }

    descricao_parametro = input(f"Digite o {opcoes[selecao_parametro]}: ").lower()
    
    return descricao_parametro

   
def mais_parametro():
    resposta = input("Deseja incluir mais um parametro na sua buscas?\n1 - Sim\n2 - Não.\n")
    while resposta == "1":
        seleciona_parametro()
        if resposta =="2":
            break


def busca(banco_de_dados:list):
    resultados = []
    chave_parametro = seleciona_parametro()
    valor_parametro = descreve_parametro(chave_parametro)
    for usuario in banco_de_dados:
        if valor_parametro in usuario[chave_parametro]:
             resultados.append(usuario)

    return resultados      

    #Na busca o usuário deve passar pelo menos 1 das opções: nome, e-mail, gênero (digitar apenas 1) ou instrumento (digitar apenas 1). 
    # O usuário deve selecionar se os resultados devem bater com todas as informações digitadas ou pelo menos uma 
    # (ex: se o usuário digitar nome e instrumento, a busca pode ser por resultados contendo o nome E o instrumento vs o nome OU o instrumento).



def saida_resultados(resultados: list):
    print("Resultado(s) encontrado(s):\n")
    for resultado in resultados:
        print(
        f"Nome: {resultado['nome']}\n"
        f"Endereço de e-mail: {resultado['email']}\n"
        f"Gêneros: {', '.join(resultado['generos'])}\n"
        f"Instrumentos: {', '.join(resultado['instrumentos'])}\n")


def seleciona_usuario(banco_de_dados: list):
    print("INICIANDO ALTERAÇÃO DE CADASTRO:\n")
    email_selecionado = input("Digite o endereço de e-mail do usuário: ")
    for usuario in banco_de_dados:
        if email_selecionado == usuario["email"]:
            return usuario
        else:
            print("E-mail não encontrado.")
    




def remover(usuario:dict, topico_modificado):
     item_remover = input("Digite o item a ser removido:")
     lista_atual = usuario[topico_modificado]
     if item_remover in lista_atual:
        lista_atual.remove(item_remover)
     usuario[topico_modificado] = lista_atual
     print(usuario)

def adicionar (usuario:dict, topico_modificado):
    item_adicionar = input("Digite o item a ser adicionado:")


def modifica_cadastro(banco_de_dados:list, usuario:dict):
    print(
        f"Nome: {resultado['nome']}\n"
        f"Gêneros: {', '.join(resultado['generos'])}\n"
        f"Instrumentos: {', '.join(resultado['instrumentos'])}\n")
    topico_modificado = input("Digite a o tipo de alteração desejada:\n1- Alterar gêneros.\n2- Alterar instrumentos.")
    tipo_modificado = input("Digite a ação que deseja realizar:\n1- Remover \n2- Adicionar.")
    if topico_modificado == "1":
        return "generos"
    elif topico_modificado == "2":
        return "instrumentos"
    else:
        print("Opção inválida.")
    if tipo_modificado == "1":
        remover()
    elif tipo_modificado == "2":
        adicionar()


    

def montar_banda():
    # Na opção de montar bandas, o usuário deverá informar o número desejado de músicos, 
    # o instrumento de cada um dos músicos (1 por músico) e 1 gênero. 
    # O programa deverá exibir na tela todas as combinações possíveis de músicos (e-mail + instrumento).
    ...

# banco = abre_banco_lista()
# novo_usuario = cria_novo_usuario()
# cadastro_nome(novo_usuario)
# cadastro_email(novo_usuario)
# validacao_email(novo_usuario, banco)
# cadastro_generos(novo_usuario)
# cadastro_instrumentos(novo_usuario)
# registra_banco_de_dados(novo_usuario)



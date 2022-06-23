import json

#ABERTURA E REGISTRO NO BANCO DE DADOS
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


def registra_tudo(banco_de_dados):
    with open('banco_de_dados.json', 'w', encoding='utf-8') as dados:
        json.dump(banco_de_dados, dados, ensure_ascii=False)

#CADASTRO

def cadastro_nome(novo_usuario:dict):
    nome_usuario = input("Insira seu nome completo (apenas letras e espaços): ").lower()
    while nome_usuario == "":
        nome_usuario = input("É preciso incluir pelo menos um nome: ")

    for letra in nome_usuario:
        if letra.isalpha() == False and letra != ' ':
            print("Nome inválido: utilize apenas letras e espaços!")
            cadastro_nome(novo_usuario)
            break
        else:
            pass
    novo_usuario["nome"] = nome_usuario
    return novo_usuario

    
def cadastro_email(novo_usuario: dict):
    email_usuario = input("Insira seu e-mail: ").lower()
    caracteres_validos = ['@','.', '_']
    while '@' and ".com" not in email_usuario:
        print("Endereço de e-mail inválido! Exemplo de e-mail válido: email@exemplo.com")
        email_usuario = input("Insira seu e-mail: ").lower()
    for caractere in email_usuario:
        if caractere.isalnum() == False:
            if caractere not in caracteres_validos:
                print("Endereço de e-mail inválido!")
                cadastro_email(novo_usuario) 
            
        else:
            novo_usuario["email"] = email_usuario
            return novo_usuario


def validacao_email(novo_usuario: dict, banco_de_dados: list):
    for usuario in banco_de_dados:
        if novo_usuario["email"] == usuario["email"]:
            print ("E-mail de usuário já cadastrado. Utilize outro e-mail para o cadastro.")
            cadastro_email(novo_usuario)
        else:
            pass


def validacao_numerica(minimo: int, frase_input: str):
    input_usuario = input(frase_input)
    while input_usuario.isdigit() == False or int(input_usuario) < minimo:
        if input_usuario.isdigit() == False:
            print("Opção inválida! Digite um número.")
            input_usuario = input(frase_input)
        elif int(input_usuario) < minimo:
            print(f"É preciso incluir pelo menos {minimo} opção/opções)")
            input_usuario = input(frase_input)
    return input_usuario



def cadastro_generos(novo_usuario:dict): #Precisa corrigir algumas validações. Exemplo: ao digitar um numero quando se pede um instrumento musical, da erro.
    generos = []
    minimo = 1
    frase_input = "Quantos gêneros músicais deseja incluir? "
    quantidade_generos = validacao_numerica(minimo, frase_input)
    generos_adicionados = 0
    while generos_adicionados < int(quantidade_generos):
        adicionando = input("Digite um gênero musicial: ").lower()
        generos.append(adicionando)
        generos_adicionados+=1
        novo_usuario["generos"] = generos
    return novo_usuario


def cadastro_instrumentos(novo_usuario:dict): #Mesmos bugs cadastro de generos
    instrumentos = []
    minimo = 1
    frase_input = "Quantos instrumentos músicais deseja incluir? "
    quantidade_instrumentos = validacao_numerica(minimo, frase_input)
    instrumentos_adicionados = 0
    while instrumentos_adicionados < int(quantidade_instrumentos):
        adicionando = input("Digite o instrumento: ").lower()
        instrumentos.append(adicionando)
        instrumentos_adicionados+=1
    novo_usuario["instrumentos"] = instrumentos
    return novo_usuario


def retornar_encerrar():
    opcao = input("Deseja realizar outra ação?\n"
                "1 - Sim.\n"
                "2 - Não.\n")
    if opcao == "1":
        menu_app_bandas()
    elif opcao == "2":
        print("Encerrando.")


def cadastro(banco_de_dados):
    novo_usuario = {}
    cadastro_nome(novo_usuario)
    cadastro_email(novo_usuario)
    validacao_email(novo_usuario, banco_de_dados)
    cadastro_generos(novo_usuario)
    cadastro_instrumentos(novo_usuario)
    registra_banco_de_dados(novo_usuario)
    print("Cadastro realizado com sucesso!")


#BUSCA

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

    while selecao_parametro not in opcoes:
        print("Opção inválida.")
        selecao_parametro = input("Selecione o parametro para sua busca:\n")

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

   
def mais_parametro(): #Não está funcioando
    resposta = input("Deseja incluir mais um parametro na sua buscas?\n1 - Sim\n2 - Não.\n")
    while resposta == "1":
        seleciona_parametro()
        if resposta =="2":
            break


def busca(banco_de_dados:list): #Só faz busca por um parametro
    
    resultados = []
    chave_parametro = seleciona_parametro()
    valor_parametro = descreve_parametro(chave_parametro)
    for usuario in banco_de_dados:
        if valor_parametro in usuario[chave_parametro]:
             resultados.append(usuario)
    return resultados      


def saida_resultados(resultados: list):
    if bool(resultados) == True:
        print("Resultado(s) encontrado(s):\n")
        for resultado in resultados:
            print(
            f"Nome: {resultado['nome']}\n"
            f"Endereço de e-mail: {resultado['email']}\n"
            f"Gêneros: {', '.join(resultado['generos'])}\n"
            f"Instrumentos: {', '.join(resultado['instrumentos'])}\n")
    else:
        print("\nNenhum resultado encontrado.\n")

#MODIFICAR

def remover(banco_de_dados, usuario, topico):
    lista_atual = banco_de_dados[usuario][topico]
    print(f"Lista atual:", ", ".join(lista_atual))
    remocao = input("Digite qual você deseja remover: ")
    if remocao in lista_atual:
        lista_atual.remove(remocao)
        registra_tudo(banco_de_dados)
        print("Item adicionado ao cadastro.")
    else:
        print("Opção inexistente nno cadastro.")

def adicionar(banco_de_dados, usuario, topico):
    lista_atual = banco_de_dados[usuario][topico]
    print(f"Lista atual:", ", ".join(lista_atual))
    adicionar = input("Digite o que você deseja adicionar: ")
    if adicionar not in lista_atual:
        lista_atual.append(adicionar)
        registra_tudo(banco_de_dados)
        print("Item adicionado ao cadastro.")
    else:
        print("Opção já existe no cadastro.")


def mod_cadastro_seleciona_topico():
    topico_modificado = input("Digite a o tipo de alteração desejada:\n1- Alterar gêneros.\n2- Alterar instrumentos.\n")   
    if topico_modificado == "1":
        return "generos"
    elif topico_modificado == "2":
        return "instrumentos"
    else:
        print("Opção inválida.")

def mod_cadastro_seleciona_acao(banco_de_dados, usuario, topico):
    acao = input("Digite a ação que deseja realizar:\n1- Remover \n2- Adicionar.\n")
    if acao == "1":
        return remover(banco_de_dados, usuario, topico)    
    elif acao == "2":
        return adicionar(banco_de_dados, usuario, topico)

def seleciona_usuario_modificar(banco_de_dados: list):
    email_selecionado = input("Digite o endereço de e-mail do usuário: ")
    encontrado = False
    usuario = 0
    while usuario < len(banco_de_dados):        
        if banco_de_dados[usuario]["email"]== email_selecionado:
            print("USUÁRIO ENCONTRADO:")
            return usuario            
            encontrado = True  
        usuario +=1          
    if encontrado == False:
        print("Usuário não encontrado")
    

def mod_cadastro_exibir(usuario:dict): #banco_de_dados:list
    print(
        f"Nome: {usuario['nome']}\n"
        f"Gêneros: {', '.join(usuario['generos'])}\n"
        f"Instrumentos: {', '.join(usuario['instrumentos'])}\n")

def modifica(banco_de_dados):
    usuario = seleciona_usuario_modificar(banco_de_dados)
    if bool(usuario)== True:
        mod_cadastro_exibir(banco_de_dados[usuario])
        topico = mod_cadastro_seleciona_topico()
        if bool(topico) == True:
            acao = mod_cadastro_seleciona_acao(banco_de_dados, usuario, topico)


#MONTAR BANDA   

def seleciona_musicos_genero(banco_de_dados):
    genero_escolhido = input("Digite o gênero desejado da sua banda: ").lower()
    usuarios_encontrados = 0
    lista_usuarios_encontrados = []
    for usuario in banco_de_dados:
        if genero_escolhido in usuario["generos"]:
            usuarios_encontrados+=1
            lista_usuarios_encontrados.append(usuario)
    if usuarios_encontrados > 0:
        print(f"> Foram encontrados {usuarios_encontrados} usuarios que tocam {genero_escolhido}.")
        # for usuario in lista_usuarios_encontrados:
        #     mod_cadastro_exibir(usuario)
    elif usuarios_encontrados <= 0:
        print(f"> Não foram encontrados usuarios que tocam{genero_escolhido}.")
    return lista_usuarios_encontrados


def escolher_qtde_musicos_instrumentos(lista_usuarios_encontrados):
    minimo = 2
    frase_input = "Quantos integrantes devem formar a banda? "
    qtde_musicos = validacao_numerica(minimo, frase_input)
    instrumentos_selecionados = 0
    lista_instrumentos = []
    while int(qtde_musicos) > len(lista_usuarios_encontrados):
            print("> Não há músicos o suficiente no nosso banco de dados para formar a banda.\n> Sugerimos que tente um número de integrantes menor.")
            qtde_musicos = input("Quantos integrantes devem formar a banda? ")
        
    print("> Você pode escolher um instrumento por integrante.")
    while instrumentos_selecionados < int(qtde_musicos):
        lista_instrumentos.append(input("Digite um instrumento desejado: "))
        instrumentos_selecionados+=1
    return lista_instrumentos       

def seleciona_musicos_instrumento(lista_usuarios_encontrados, lista_instrumentos):
    lista_musicos_selecionados = {}
    for instrumentos in lista_instrumentos:
        lista_musicos_selecionados[instrumentos] = []

    for usuario in lista_usuarios_encontrados:
        for instrumento in lista_instrumentos:
            if instrumento in usuario["instrumentos"]:
                lista_musicos_selecionados[instrumento].append(usuario)
                if usuario in lista_usuarios_encontrados:
                    lista_usuarios_encontrados.remove(usuario)
    return lista_musicos_selecionados


def organiza_musicos_instrumentos(lista_musicos_selecionados):
    instrumentos_formatados = {}
    lista_emails = []
    for instrumento in lista_musicos_selecionados:
        instrumentos_formatados[instrumento] = []
        for musico in lista_musicos_selecionados[instrumento]:
            instrumentos_formatados[instrumento].append(f"{musico['email']} , {instrumento}")
            lista_emails.append(musico["email"])
    lista_emails = list(set(lista_emails))

    musico_por_instrumento = []
    for formatado in instrumentos_formatados:
        musico_por_instrumento.append(instrumentos_formatados[formatado])
    return musico_por_instrumento, lista_emails

def formar_bandas(lista_musicos_selecionados):
    if len(lista_musicos_selecionados) == 0:
        return [[]]
    result = []    
    sub_lista =  formar_bandas(lista_musicos_selecionados[1:])
    for musico_a in lista_musicos_selecionados[0]:
        for musico_b in sub_lista:
            result.append([musico_a, *musico_b])
    return result


def removedor_duplicados(bandas_formadas, lista_emails):
    for email in lista_emails:
        indice = 0
        while indice < len(bandas_formadas):
            aparece = 0
            for musico in bandas_formadas[indice]:
                if email in musico:
                    aparece+=1
            if aparece > 1:
                bandas_formadas.remove(bandas_formadas[indice])
                indice -=1
            indice +=1
    return bandas_formadas

def formata_saida_bandas(bandas_finais):
    if bool(bandas_finais) == False:
        print("Não foi possível formar uma banda.")
    else:
        for banda in bandas_finais:
            print(banda)



def montar_banda(banco_de_dados):
    lista_usuarios_encontrados = seleciona_musicos_genero(banco_de_dados)
    lista_instrumentos = escolher_qtde_musicos_instrumentos(lista_usuarios_encontrados)
    print("Instrumentos escolhidos:", ", ".join(lista_instrumentos))
    lista_musicos_selecionados = seleciona_musicos_instrumento(lista_usuarios_encontrados, lista_instrumentos)
    resultados = organiza_musicos_instrumentos(lista_musicos_selecionados)
    musico_por_instrumento = resultados[0]
    lista_emails = resultados[1]
    bandas_formadas = formar_bandas(musico_por_instrumento)
    bandas_finais = removedor_duplicados(bandas_formadas, lista_emails)
    formata_saida_bandas(bandas_finais)


def menu_app_bandas():
    opcoes = ["1", "2", "3", "4"]
    banco_de_dados = abre_banco_lista()
    escolha = input("Escolha uma opção para continuar:\n"
          "1 - Cadastrar novo músico.\n"
          "2 - Fazer uma busca.\n"
          "3 - Modificar um cadastro\n"
          "4 - Montar uma banda\n"
          "Digite sua escolha: ")
    while escolha not in opcoes:
        print("Opção inválida.")
        escolha = input("Escolha uma opção para continuar:\n"
          "1 - Cadastrar novo músico.\n"
          "2 - Fazer uma busca.\n"
          "3 - Modificar um cadastro\n"
          "4 - Montar uma banda\n"
          "Digite sua escolha: ")
    else:
        if escolha == "1":
            cadastro(banco_de_dados)
            retornar_encerrar()
        elif escolha == "2":
            resultados = busca(banco_de_dados)
            saida_resultados(resultados)
            retornar_encerrar()
        elif escolha == "3":
            modifica(banco_de_dados)
            retornar_encerrar()
        elif escolha == "4":
            montar_banda(banco_de_dados)
            retornar_encerrar()

print("Seja bem-vindo(a) ao Formador de Bandas.")
menu_app_bandas()







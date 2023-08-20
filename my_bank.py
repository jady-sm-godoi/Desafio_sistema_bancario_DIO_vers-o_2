usuarios = [{"cpf":"123", "nome": "Jady Godoi"}, {"cpf":"456"}]
cadastrado = False
contas = []

# funções:
def checa_usuario(cpf):
    is_user = False
    for usuario in usuarios:
        if(cpf in usuario["cpf"]):
            is_user = usuario["nome"]
    return is_user

def convite():
    convite = """
    Vimos que você não está cadastrado em nosso banco.
    Gostaria de se cadastrar?

    [s] - sim!
    [n] - não.
"""
    return input(convite)

def cadastrar_usuario():

    cpf = input("""Qual o seu cpf? Digite apenas os números: """)
    cliente = checa_usuario(cpf)

    if(cliente):
        print('Usuário já cadastrado!')
           
    else:
        nome = input("Qual seu nome? ")
        dtnascimento = input("Qual sua data de nascimento? ")
        rua = input("Qual nome da rua onde você mora? ")
        numero = input("Qual numero da casa? ")
        bairro = input("Qual o bairro? ")
        cidade = input("Qual a cidade? ")
        uf = input("Qual a unidade federal? ")

        endereco = f"{rua}, {numero} - {bairro} - {cidade}/{uf}"
        
        novo_usuario = {"cpf": cpf, "nome": nome, "nascimento": dtnascimento, "endereco": endereco}

        usuarios.append(novo_usuario)
        return novo_usuario
            
def cadastrar_conta():
    nova_conta = ''
    cpf_conta = input('Para quem é a nova conta? Digite seu cpf: ')

    cliente = checa_usuario(cpf_conta)
    if(cliente):
        nova_conta = input(f"""
    A nova conta será para {cliente}?
    [s] - sim. Sou eu!
    [n] - não. Foi engano.
    """)
    if(nova_conta == 'n'):
        print("Você não tem cadastro em nosso banco? Vamos abrir um cadastro!")
        cadastrar_usuario()
    if(nova_conta == 's'):
        conta_cliente = {'cpf': cliente, 'banco': '0001', 'conta': len(contas) + 1}
        contas.append(conta_cliente)
        print(f"Caro(a) ${cliente}, o número da sua conta é {len(contas) + 1} na agência 0001.")
        primeira_operacao = input("""
                                Gostaria de realizar alguma operação? 
                                [s] - sim
                                [n] - não
                                """)
        if(primeira_operacao == 's'):
            operacoes()
        if(primeira_operacao == 'n'):
            print("Seja bem vindo(a)! Esperamos te ver em breve!")
    else:
        print("Você não é cliente de nosso banco. Vamos abrir um cadastro!")
        cadastrar_usuario()

def deposito(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(*, saldo, limite, extrato, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite de R$500.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato, numero_saques

def extratos(extrato, /,saldo,*,nome):
    print(f"\n=============EXTRATO DE {nome.upper()}==============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def operacoes():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:

        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = deposito(saldo, extrato)

        elif opcao == "s":
            saldo, extrato, numero_saques = saque(saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques, limite_saques=limite_saques)

        elif opcao == "e":
            extratos(extrato, saldo, nome='Jady')

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def welcome():
    print("Bem vindo ao My Bank!")
    menu = """
    O que deseja fazer?
    [c] - abrir um cadastro
    [d] - abrir uma conta
    [b] - realizar operações bancárias em minha conta
    [s] - sair
    """

    while True:

        opcao = input(menu)

        if opcao == 'c':
            cadastrar_usuario()
        
        elif opcao == 'd':
            cadastrar_conta()

        elif opcao == 'b':
            cpf = input("Digite seu cpf: ")
            cliente = checa_usuario(cpf)
            if(cliente):
                operacoes()
            else:
                print("Você não possui conta em nosso banco!")
                break
        
        elif opcao == 's':
            break

#processos: 
welcome()


# cadastrar_conta()          
# cpf_number = input("Bem vindo! Qual é seu CPF? ")

# for usuario in usuarios:
#     if(cpf_number in usuario["cpf"]):
#         cadastrado = True

# if(cadastrado == True):
#     operacoes()
# elif(convite() == 's'):
#     cliente = cadastrar_usuario()
#     if(cliente):
#         operacoes()
# else:
#     print('Ok! Você sempre será bem vindo ao MyBank!')
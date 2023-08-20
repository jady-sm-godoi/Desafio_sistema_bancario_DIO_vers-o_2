# Sistema Bancário com Python - versão 2.0

Neste projeto, tive a oportunidade de criar um Sistema Bancário em Python. 

## Objetivo Geral

Separar as funções existentes de saque, depósito e extrato em funções. 

Criar duas novas funções: cadastrar usuário e cadastrar conta bancária

Cada função vai ter uma regra na passagem de argumentos:

- saque: argumentos apenas por nome (saldo, valor, extrato, limite, número_saques, limite_saques). Retorno: saldo e extrato
- depósito: argumentos apenas por posição (saldo, valor, extrato). Retorno: saldo e extrato
- extrato: argumentos por posição e nome.
    - Argumentos posicionais: saldo
    - Argumentos nomeados: extrato
- Criar usuário: o programa deve armazenar os usuários em uma lista
    - Usuário: nome, data de nascimento, cpf e endereço.
    - endereço: “logradouro, nro - bairro - cidade/sigla estado.
    - cpf: apenas os números
    - Não podemos cadastrar 2 usuários com o mesmo CPF
- Criar conta corrente: o programa deve armazenar contas em uma lista
    - Conta: agência, número da conta e usuário.
    - numero da conta é sequencia, iniciando com 1.
    - agencia é 0001
    - Usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuario.

Durante o desafio, tive a chance de aplicar meus conhecimentos de **manipulação de strings**, **estruturas condicionais** e de **repetição**, também de **operadores** em Python e **funçôes em Python** (com diferentes formas de receber parâmetros) e assim criar um sistema funcional que simule as operações bancárias.

Esta é a segunda versão. Melhorias ainda devem ser implementadas.
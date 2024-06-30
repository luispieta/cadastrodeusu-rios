escolha = ''
lista = []
chave = {}
def cadastro():
    chave['nome'] = input('Digite seu nome: ')
    chave['telefone'] = int(input('Digite seu telefone: '))
    chave['email'] = input('Digite seu email: ')
    lista.append(chave)

def relatorio():
    print('---Relatório---\n')
    for usuario in lista:
        for key in usuario.keys():
            print('{}: {}'.format(key, usuario[key]))
        print("\n")

def editor():
    print('Informe o que você escreveu num dos cadastros (sendo nome, telefone ou email, em específico no que você escreveu)')
    print("\n")
    editar = input('')
    for edicao in lista:
        if editar == chave['nome']:
            edicao['nome'] = input('Digite seu novo nome: ')
            return edicao

        if editar == chave['telefone']: 
            edicao['telefone'] = int(input('Digite seu novo telefone: '))
            return edicao

        if editar == chave['email']:
            edicao['email'] = input('Digite seu novo email: ')
            return edicao

while escolha.lower() != 'sair':
    print('===MENU=== \n Cadastro \n Relatório \n Editar \n Sair')
    escolha = input('')
    print("\n")

    if escolha == 'cadastro':
        cadastro()
        print('\n')
        print('**Usuário cadastrado**') 
        print('\n')

    if escolha.lower() == 'relatório':
        relatorio()

    if escolha.lower() == 'editar':
        editor()

print('Obrigado!')
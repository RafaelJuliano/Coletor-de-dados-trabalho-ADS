import pyodbc

conec = pyodbc.connect(
    'driver={MySQL ODBC 8.0 ANSI Driver}; server=localhost:3306; database=fazenda_bd; UID=root; PWD=*senha*;')
cursor = conec.cursor()

u = {'Usuário': [], 'Senha': [], 'Nome': []}

lmt = list(range(50))

def verificadorInt(lista, texto, textoe):
    while True:
        vr = input(texto)
        try:
            vr = int(vr)
            if vr in lista:
                return vr
            else:
                print(textoe, '\n')
        except:
            print('Digite um valor inteiro')
        else:
            print('Digite um valor válido\n')


def verificadorStr(lista, texto):
    while True:
        vr = input(texto)
        if vr in lista:
            return vr
        else:
            print('Valor inválido\n')


def login():
    cursor.execute('SELECT Matrícula, Nome, Senha FROM funcionários WHERE Cargo_ID = 23')
    x = []
    for row in cursor:
        x.append(row)
    for row in x:
        u['Usuário'].append(row[0])
        u['Nome'].append(row[1])
        u['Senha'].append(row[2])

    l = verificadorInt(u['Usuário'], 'Digite sua matrícula: ', 'Usuário não encontrado')
    index = 0
    for x in u['Usuário']:
        if x == l:
            while True:
                s = input('Digite a senha: ')
                if s == u['Senha'][index]:
                    resp = [l, u['Nome'][index]]
                    menu(resp[0], resp[1])
                    break
                else:
                    print('Senha inválida\n')
        else:
            index += 1


def menu(matricula, nome):
    resp = [matricula, nome]
    texto = ['SISTEMA DE COLETA DE LEITE',
             'RESPONSÁVEL: {}\n',
             'Escolha a opção',
             '1 - Consultar ordenha pendente',
             '2 - Registrar nova ordenha',
             '3 - Encerrar programa']
    print(texto[0])
    print(texto[1].format(resp[1]))
    print(texto[2])
    print(texto[3])
    print(texto[4])
    print(texto[5])
    o = verificadorInt([1, 2, 3], ': ', 'Digite 1, 2 ou 3')
    if o == 1:
        print('Vacas não ordenhadas\n', pendente(), '\n')
        menu(resp[0], resp[1])
    elif o == 2:
        registrar(resp)
    else:
        login()


def pendente():
    cursor.execute('SELECT ID FROM v_ordenhap')
    v = []
    v2 = []
    x = 0
    for row in cursor:
        v.append(row)
    for row in v:
        v2.append(v[x][0])
        x += 1
    return v2


def registrar(resp):
    vaca = verificadorInt(pendente(), 'Digite o código: ', 'Não existe ou já foi ordenhada')
    litr = verificadorInt(lmt, 'Quantidade em litros: ', 'Quantidade muito alta, verifique')
    temp = verificadorInt(lmt, 'Temperatura: ', 'Muito alta, verefique')

    string1 = 'CALL proc_ordenha ({}, {}, {}, {})'.format(resp[0], vaca, litr, temp)
    string2 = 'CALL proc_ordenhaU ({})'.format(vaca)

    cursor.execute(string1)
    cursor.execute(string2)
    cursor.execute('COMMIT')

    sn = verificadorStr(['s', 'n', 'S', 'N'], 'Inserir novo registro? s/n: ').lower()
    if sn == 's':
        registrar(resp)
        print('\n')
    else:
        menu(resp[0], resp[1])
        print('\n')


login()

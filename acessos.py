from Portifolio import funcoes, verificadores
import pyodbc

def login(cursor):
    u = {'Usuário': [], 'Senha': [], 'Nome': []}
    cursor.execute('SELECT Matrícula, Nome, Senha FROM funcionários WHERE Cargo_ID = 23')
    x = []
    for row in cursor:
        x.append(row)
    for row in x:
        u['Usuário'].append(row[0])
        u['Nome'].append(row[1])
        u['Senha'].append(row[2])

    l = verificadores.verificadorInt(u['Usuário'], 'Digite sua matrícula: ', 'Usuário não encontrado')
    index = 0
    for x in u['Usuário']:
        if x == l:
            while True:
                s = input('Digite a senha: ')
                if s == u['Senha'][index]:
                    resp = [l, u['Nome'][index]]
                    menu(resp[0], resp[1], cursor)
                    break
                else:
                    print('Senha inválida\n')
        else:
            index += 1


def menu(matricula, nome, cursor):
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
    o = verificadores.verificadorInt([1, 2, 3], ': ', 'Digite 1, 2 ou 3')
    if o == 1:
        print('Vacas não ordenhadas\n', funcoes.pendente(cursor), '\n')
        menu(resp[0], resp[1], cursor)
    elif o == 2:
        funcoes.registrar(resp, cursor)
    else:
        login(cursor)

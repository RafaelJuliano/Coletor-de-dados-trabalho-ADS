from Portifolio import acessos, verificadores

def pendente(cursor):
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


def registrar(resp, cursor):
    lmt = list(range(50))
    vaca = verificadores.verificadorInt(pendente(cursor), 'Digite o código: ', 'Não existe ou já foi ordenhada')
    litr = verificadores.verificadorInt(lmt, 'Quantidade em litros: ', 'Quantidade muito alta, verifique')
    temp = verificadores.verificadorInt(lmt, 'Temperatura: ', 'Muito alta, verefique')

    string1 = 'CALL proc_ordenha ({}, {}, {}, {})'.format(resp[0], vaca, litr, temp)
    string2 = 'CALL proc_ordenhaU ({})'.format(vaca)

    cursor.execute(string1)
    cursor.execute(string2)
    cursor.execute('COMMIT')

    sn = verificadores.verificadorStr(['s', 'n', 'S', 'N'], 'Inserir novo registro? s/n: ').lower()
    if sn == 's':
        registrar(resp, cursor)
        print('\n')
    else:
        acessos.menu(resp[0], resp[1], cursor)
        print('\n')

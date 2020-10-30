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

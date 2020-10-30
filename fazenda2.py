import pyodbc

from Portifolio import acessos

conec = pyodbc.connect(
        'driver={MySQL ODBC 8.0 ANSI Driver}; server=localhost:3306; database=fazenda_bd; UID=root; PWD=Dv#0812$;')
cursor = conec.cursor()

lmt = list(range(50))

acessos.login(cursor)

import pyodbc
import acessos

conec = pyodbc.connect(
        'driver={MySQL ODBC 8.0 ANSI Driver}; server=localhost:3306; database=fazenda_bd; UID=root; PWD=senha;')
cursor = conec.cursor()

acessos.login(cursor)

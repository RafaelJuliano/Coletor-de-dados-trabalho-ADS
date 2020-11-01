import pandas
import sqlalchemy
from datetime import date, datetime

data = date.today()
hora = datetime.now()

print(hora)
print(data)

engine = sqlalchemy.create_engine('mysql+pymysql://root:senhalocalhost:3306/fazenda_bd')

ordenhap = '''
SELECT ID FROM v_ordenhap
'''

r = '4'
v = '1'
l = '23'
t = '33'
ordenha = '''
call proc_ordenha(%(R)s, %(V)s, %(L)s, %(T)s)
'''

ordenha1 = '''
INSERT INTO Ordenha (Data, Hora, Responsável, Vaca_ID, Litros, TemperaturaLeite) VALUES (current_date (), current_time (), 4, 1, 23, 33)
'''

pedidos = '''
CALL proc_pedidos (%(I)s, %(F)s)
'''

df = pandas.read_sql_query('insert into teste (id) values (3)', engine)

#d = {'Data': [1, 2], 'col2': [3, 4]}
#df = pandas.DataFrame(data=d)


print(df)


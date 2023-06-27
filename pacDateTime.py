# datetime fornece classes para manipulação de datas e horas

# importando pacote
import datetime

dia_hoje = datetime.datetime.today()
print(dia_hoje)

print(type(dia_hoje))

print(datetime.datetime.today().date())

data = datetime.datetime.today().date()

ano = data.year
mes = data.month
dia = data.day
print(ano, mes, dia)

# date permite passar a data (ano, mes, dia)
data_antiga = datetime.date(2023, 6, 15)
print(data_antiga)

# calculo de datas
print(data - data_antiga)
print(data + datetime.timedelta(days= 30))

# inverter data
print(data.strftime('%d/%m/%y'))

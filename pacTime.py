# funções relacionadas a tempo

import time

print("Start now")
time.sleep(3)  # 3 segundos até próximo comando
print("Finish")

agora = time.localtime()
print(agora)
print(type(agora))

print(time.strftime("%m/%d/%y, %H:%M:%S", agora))

# conversao
time_texto = "21 June, 2020"
convert = time.strptime(time_texto, "%d %B, %Y")  # o B é da config do pac time
print(convert)

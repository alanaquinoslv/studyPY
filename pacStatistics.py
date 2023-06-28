# fornece funções para calcular estatisticas matemáticas e interage com listas

import statistics

lista = [12, 77, 15, 28, 32, 89, 58, 45, 77]

# media comum
print(sum(lista) / len(lista))

# media com pacote
print(statistics.mean(lista))

# mediana 
print(statistics.median(lista))

# moda
print(statistics.mode(lista))
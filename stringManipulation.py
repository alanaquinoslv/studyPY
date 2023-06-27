# algumas funções para manipulação de string mais utilizadas:

   # replace()
   # startswith()
   # endswith()
   # count()
   # capitalize()
   # isdigit()
   # isalnum()
   # upper()
   # lower()
   # find ()
   # strip()
   # split()

# Imprimindo uma string.
String = 'Olá Mundão!'
print( String )

# Tipo de uma string.
print( type( String ) )

# Tamanho de uma string.
print( len( String ) )

# Concatenação
print( String + ' Estou aprendendo Python...' )

# Substitui uma substring por alguma outra coisa.
Substituir = String.replace('Mundão', 'Mundo Louco :X')
print( Substituir )

# A string s começa com "Olá"?
print( String.startswith('Olá') )

# A string termina com "mundo"?
print( String.endswith('mundo') )

# Quantas ocorrências da palavra "a" a string possui?
print( String.count('M') )

# Capitalize - Transformar a primeira letra da primeira palavra em maiúscula.
String_02 = 'Alan'
print( String_02.capitalize() )

# Verificar se uma string só possui números.
String_03 = '123456789'
String_04 = '123456789ABC'
print( String_03.isdigit() )
print( String_04.isdigit() )

# Verificar se uma string é alfanumérica (só possui letras e números).
print( '12345abc'.isalnum() )

# Transformar tudo em Maiusculo
print( String.upper() )

# Transformar tudo em Minúsculo
print( String.lower() )

# Procurar algo na string
print( String.find('!') )

# Removendo espaçoes antes e fim da palavra
String_05 =' Olá Mundão! '
print( String_05.strip() )

# Removendo espaçoes antes e fim da palavra
String_06 ='Loja 1 vendeu 10, Loja 2 vendeu 20, Loja 3 vendeu 30 '
print( String_06.split(',') )
#há os seguintes tipos de dados integrados por padrao

    #Text Type: str
    #Numeric Types: int, float, complex
    #Sequence Types: list, tuple, range
    #Mapping Type: dict
    #Set Types: set, frozenset
    #Boolean Type: bool
    #Binary Types: bytes, bytearray, memoryview

String = str('Hello World')
Integer = int(10) 
Float = float(14.7)
Complex = complex(1j)
Lista = list(('Maçã', 'Morango'))
Tupla = tuple(("A", "B"))
Range = range(6)
Dicionario = dict(name = "Alan", age = 21)
Set = set(('A', 'B', 'C'))
Fronzet = frozenset(('A', 'B', 'C'))
Boolean = bool(5)
Bytes = bytes(5)
ByteArray = bytearray(5)
MemoryView = memoryview(bytes(5))

# importando pacote externo
from datetime import datetime
Data = datetime.today().date()
print(Data)

#para identificar o tipo usa-se o comando type
print(type(String))
print(type(Integer))
print(type(Float))
print(type(Complex))
print(type(Lista))
print(type(Tupla))
print(type(Range))
print(type(Dicionario))
print(type(Set)) 
print(type(Fronzet))
print(type(Boolean))
print(type(Bytes))
print(type(ByteArray))
print(type(MemoryView))
print(type(Data))
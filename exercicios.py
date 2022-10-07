# Testes exercícios
# Para os testes abaixo, pode-se criar uma aplicação simples.
# 1. Escreve um método que faça a soma de 1 até um número dado. O número deve ser maior que
# zero e um dos números deve ser 100000 (cem mil).
# Exemplos:
#  Soma(2) -> 3 (1 +2)
#  Soma(8) -> 36 (1+2+3+4+5+6+7+8)
def soma(n):
    if n <= 0:
        return 0
    return (1 + n) * n / 2 

print(soma(100000))

# 2. Dado um array de strings, remova as letras duplicadas em sequência de cada palavra,
# exemplos:
# duplicados(["abracadabra","allottee","assessee"])=["abracadabra","alote","asese"]
# duplicados(["kelless","keenness","Alfalggo"])=["keles","kenes","Alfalgo"]

def duplicados(lista):
    return ["".join([x for i, x in enumerate(y) if i == 0 or x != y[i-1]]) for y in lista]

print(duplicados(["abracadabra","allottee","assessee"]))
print(duplicados(["kelless","keenness","Alfalggo"]))

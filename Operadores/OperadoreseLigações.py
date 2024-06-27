
print(9 % 6 % 2)

#Maneiras de avaliar essa expressão:
# 1° da Esquerda para a direita: 9 % 6 dá 3 então 3 % 2 a saida é 1
# 2° da Direita para a esquerda: 2 % 6 dá 0 causando erro

print("Experimento com exponenciação: ")
# A expressão 2 ** 2 ** 3 é avaliada da direita para a esquerda devido à ordem de precedência dos operadores
print(2 ** 2 ** 3) 
#2 ** 3
#2 ** 8

print(-3 ** 2)    # Saída: -9
print(-2 ** 3)    # Saída: -8
print(-(3 ** 2))  # Saída: -9

print("Expresão misturada")
print(2 * 3 % 5)
#Faça pela ordem de prioridade 
"""
    1° **
    2° +,-(unarios)
    3° *,/,//,%
    4° +,-(binários)
"""



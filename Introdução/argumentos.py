#1 Usando varios argumentos
print("A aranha pequenininha" , "subiu" , "a tromba d'água.")

#2 Argumentos Posicionais
print("Meu nome é", "Python.")
print("Monty Python.")

#3 Argumentos Palavra-Chave
print("Meu nome é", "Python.", end=" ")
print("Monty Python.")

#4 olhe com atenção e veremos que usamos o argumento end mas a string atribuida está vazia 
print("Meu nome é ", end="")
print("Monty Python.")

#5 Argumento da palavra chave sep
print("Meu", "nome", "é", "Monty", "Python.", sep="-")

#6 Argumentos da palavra chave misturados
print("Meu", "nome", "é", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")

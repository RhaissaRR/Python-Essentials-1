#Modifique a primeira linha de código no editor, usando as palavras-chave sep e end, para corresponder à saída esperada. Use as duas funções print() no editor.
#Não altere nada na segunda invocação de print()
print("Programação","Essenciais","em")
print("Python")

#Modificado
print("Programação","Essenciais","em", sep="***", end="...")
print("Python")

# LAB formatação de saída
""" minimizar o número de invocações de função print() inserindo a sequência \n nas strings;
    aumentar a flecha duas vezes (mas manter as proporções)
    duplique a seta, colocando as duas setas lado a lado; observação: uma string pode ser multiplicada usando o seguinte truque: "string" * 2 produzirá "stringstring" (falaremos sobre isso em breve)
    remova qualquer uma das aspas e analise com cuidado a resposta do Python; preste atenção onde Python vê um erro - este é o lugar onde o erro realmente existe?
    faça o mesmo com alguns parênteses;
    altere qualquer uma das palavras Print em algo diferente, diferindo apenas no caso (por exemplo, Print) - o que acontece agora?
    substitua algumas aspas por apóstrofos; veja o que acontece com cuidado.
"""
print(" *")
print(" * *")
print(" * *")
print(" * *")
print("*** ***")
print(" * *")
print(" * *")
print(" *****")

#Modificado
###################
print("versão original:")
###################
print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")
###################
print("com menos 'print()' invocações:")
###################
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
###################
print("mais alto:")
###################
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("******     ******")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *     *")
print("     *******")
###################
print("dobrou:")
###################
print("        *        "*2)
print("       * *       "*2)
print("      *   *      "*2)
print("     *     *     "*2)
print("    *       *    "*2)
print("   *         *   "*2)
print("  *           *  "*2)
print(" *             * "*2)
print("******     ******"*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *     *     "*2)
print("     *******     "*2)

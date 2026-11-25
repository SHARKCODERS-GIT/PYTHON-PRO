# Aula 12 | Exercício 1 | Três formas de ler

with open("3_linhas.txt", "r", encoding="utf-8") as f:
    print("read():", repr(f.read()))

with open("3_linhas.txt", "r", encoding="utf-8") as f:
    print("readline():", repr(f.readline()))

with open("3_linhas.txt", "r", encoding="utf-8") as f:
    print("readlines():", f.readlines())

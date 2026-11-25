# Aula 09 | Extra 2 | Maior de três

def maior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    return c

print("Maior:", maior(12, 45, 31))

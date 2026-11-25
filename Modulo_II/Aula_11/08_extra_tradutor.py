# Aula 11 | Extra 2 | Mini tradutor

pt_en = {"casa": "house", "gato": "cat", "livro": "book",
         "água": "water", "sol": "sun", "mar": "sea"}

palavra = input("Palavra em português? ").strip().lower()
print(pt_en.get(palavra, "Ainda não conheço essa palavra."))

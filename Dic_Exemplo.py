filmes = {'Star Wars':1977,'Titanic':2003,'Jurassic Park':1993}
for x in sorted(filmes, key=filmes.get):
    print(filmes[x],x)
#for x in sorted(filmes.items()):
#    print(f'O filme {x[0]} é do ano de {x[1]}')
#for k, v in sorted(filmes.items()):
#    print(k,v)
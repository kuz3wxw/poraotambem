
livros = [
      {"titulo":"Ghost in the Shell Perfect", "autor":"Shirow Masamune", "ano de lançamento": 2017, "favorito":"0"},
      {"titulo":"Ghost in the Shell Perfect stand alone", "autor":"Shirow Masamune", "ano de lançamento": 2017, "favorito":"0"},
      {"titulo":"O livro da matemática", "autor":" Maria da Anunciação Rodrigues", "ano de lançamento": 2020, "favorito":"0"},
]


for livro in livros: 
    if livro["titulo"] == "Ghost in the Shell Perfect stand alone":
        livro["favorito"] = "1"
print(livros[1])

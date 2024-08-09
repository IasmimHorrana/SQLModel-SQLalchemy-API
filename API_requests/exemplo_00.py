import requests # Importa o módulo requests, usado para fazer requisições HTTP

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/25") # Faz uma requisição GET para a API da PokeAPI para obter dados do Pokémon de número 15 (Charizard)
data = response.json() # Converte a resposta da requisição para um dicionário Python usando o formato JSON
data_types = data['types'] # Extrai a lista de tipos (como 'Fogo', 'Voador') do dicionário 'data'
types_list = []

for type_info in data_types: # Itera sobre cada tipo no dicionário 'data_types'
    types_list.append(type_info['type']['name'])  # Adiciona o nome do tipo
types = ', '.join(types_list) # Junta os nomes dos tipos em uma única string separada por vírgula
print(data['name'], types)




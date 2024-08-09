import requests # Importa o módulo requests, usado para fazer requisições HTTP
from pydantic import BaseModel # Importa a classe BaseModel do pydantic para definição do esquema de dados

# Define um esquema de dados usando BaseModel do pydantic para representar um Pokémon
class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True # Configuração para indicar que o esquema será utilizado em modo ORM

def capturar_pokemon(id: int) -> PokemonSchema:

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}") # Faz uma requisição GET para a API da PokeAPI para obter dados do Pokémon de número 15 (Charizard)
    data = response.json() # Converte a resposta da requisição para um dicionário Python usando o formato JSON
    data_types = data['types'] # Extrai a lista de tipos (como 'Fogo', 'Voador') do dicionário 'data'
    types_list = []

    for type_info in data_types: # Itera sobre cada tipo no dicionário 'data_types'
        types_list.append(type_info['type']['name'])  # Adiciona o nome do tipo
    types = ', '.join(types_list) # Junta os nomes dos tipos em uma única string separada por vírgula
    return PokemonSchema(name=data['name'], type=types)

if __name__ == "__main__":
    print(capturar_pokemon(10))
    print(capturar_pokemon(6))
    print(capturar_pokemon(13))





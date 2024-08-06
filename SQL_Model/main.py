from typing import Optional  # Importa o tipo Optional para lidar com valores opcionais

from sqlmodel import Field, Session, SQLModel, create_engine  # Importa as classes necessárias do SQLModel

# Define a classe Hero, que herda de SQLModel e representa uma tabela no banco de dados
class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)  # Campo opcional 'id', chave primária da tabela
    name: str  # Campo obrigatório 'name' do tipo string
    secret_name: str  # Campo obrigatório 'secret_name' do tipo string
    age: Optional[int] = None  # Campo opcional 'age' do tipo inteiro, inicializado como None por padrão

# Cria uma engine de banco de dados SQLite, usando um arquivo chamado 'database.db', com saída (echo) ativada para debug
engine = create_engine("sqlite:///database.db", echo=True)

# Cria as tabelas no banco de dados conforme definido nos modelos (nesse caso, apenas a tabela Hero)
SQLModel.metadata.create_all(engine)

# Cria instâncias da classe Hero com dados fictícios
hero_1 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_2 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
hero_3 = Hero(name="Deadpond", secret_name="Dive Wilson", age=46)

# Inicia uma sessão de interação com o banco de dados
with Session(engine) as session:
    # Adiciona as instâncias de Hero à sessão para serem persistidas no banco de dados
    session.add(hero_1)
    session.add(hero_2)
    session.add(hero_3)
    # Confirma as mudanças feitas na sessão, efetivamente persistindo os dados no banco de dados
    session.commit()

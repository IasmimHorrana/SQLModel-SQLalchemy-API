from sqlalchemy import create_engine  

# Conecta ao banco de dados SQLite em memória e ativa a exibição de saída (echo) para depuração
engine = create_engine('sqlite:///meubanco.db', echo=True)
print("Conexão com SQLite estabelecida.") 

from sqlalchemy.orm import declarative_base  # Importa a função declarative_base do SQLAlchemy
from sqlalchemy import Column, Integer, String  # Importa classes necessárias para definir colunas

Base = declarative_base()  # Cria uma classe base para definição de modelos de dados

# Define a classe 'usuario' como uma tabela no banco de dados
class usuario(Base):
    __tablename__ = 'usuarios'  

    id = Column(Integer, primary_key=True)  
    nome = Column(String)  
    idade = Column(Integer)  

# Cria as tabelas no banco de dados com base nos modelos definidos (nesse caso, apenas 'usuarios')
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker  # Importa o sessionmaker para criar sessões

Session = sessionmaker(bind=engine)  # Cria um sessionmaker associado à engine criada
session = Session()  # Cria uma sessão para interagir com o banco de dados

# Cria um novo objeto 'usuario' com dados fictícios e adiciona à sessão
novo_usuario = usuario(nome="João", idade=28)
session.add(novo_usuario)
session.commit()  # Confirma a transação, efetivamente persistindo os dados no banco de dados

print("Usuário inserido com sucesso.")  

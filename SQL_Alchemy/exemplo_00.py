from sqlalchemy import create_engine

# Conectar ao SQLlite em memoria
engine = create_engine('sqlite:///meubanco.db', echo=True)
print("Conexão com SQLite estabelecida.")
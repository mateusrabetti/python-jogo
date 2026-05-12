# Importa o objeto db de 'db', que fornece as funcionalidades do SQLAlchemy para interagir com o banco de dados
from db import db  

# Define a classe jogo que representa a tabela 'jogos' no banco de dados
class Jogo(db.Model):  
    # Define o nome da tabela no banco de dados
    __tablename__ = 'jogos'  

    # Define as colunas da tabela 'jogos'
    id = db.Column(db.Integer, primary_key=True)  # Coluna para o ID do jogo, chave primária
    titulo = db.Column(db.String(80), nullable=False)  # Coluna para o titulo do jogo, não pode ser nulo
    genero = db.Column(db.String(80), nullable=False)  # Coluna para a genero do jogo, não pode ser nulo
    plataforma = db.Column(db.String, nullable=False)  # Coluna para o plataforma do jogo, não pode ser nulo
    dev = db.Column(db.String, nullable=False)

    # Método para retornar os dados do jogo como um dicionário
    def json(self):  
        return {
            'id': self.id,  # ID do jogo
            'titulo': self.titulo,  # titulo do jogo
            'genero': self.genero,  # genero do jogo
            'plataforma': self.plataforma,  # plataforma do jogo
            'dev': self.dev 
        }

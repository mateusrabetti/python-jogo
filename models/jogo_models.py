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
    desenvolvedor = db.Column(db.String(80), nullable=False)  # Coluna para o desenvolvedor do jogo, não pode ser nulo
    plataforma = db.Column(db.String(80), nullable=False)
    
    def json(self):  
        return {
            'id': self.id,  # ID do jogo
            'titulo': self.titulo,  # titulo do jogo
            'genero': self.genero,  # genero do jogo
            'desenvolvedor': self.desenvolvedor,  # desenvolvedor do jogo
            'plataforma': self.plataforma
        }

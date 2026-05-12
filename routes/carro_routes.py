from flask import Blueprint, request  
from controllers.carro_controllers import get_carros, create_carro, get_carro_by_id 

# Define um Blueprint para as rotas de "Carro"
carro_routes = Blueprint('carro_routes', __name__)  

# Rota para listar todos os carros (GET)
@carro_routes.route('/Carro', methods=['GET'])
def carros_get():
    return get_carros()

# Rota para buscar um carro pelo ID (GET)
@carro_routes.route('/Carro/<int:carro_id>', methods=['GET'])
def carro_get_by_id(carro_id):
    return get_carro_by_id(carro_id)

# Rota para criar um novo carro (POST)
@carro_routes.route('/Carro', methods=['POST'])
def carros_post():
    return create_carro(request.json)


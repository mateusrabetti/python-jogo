from models.carro_models import Carro  # Importa o modelo Carro
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os carros
def get_carros():
    carros = Carro.query.all()  # Busca todos os carros no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de carros.',
            'dados': [carro.json() for carro in carros]  # Converte os objetos de carro para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para obter um carro específico por ID
def get_carro_by_id(carro_id):
    carro = Carro.query.get(carro_id)  # Busca o carro pelo ID

    if carro:  # Verifica se o carro foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'Carro encontrado.',
                'dados': carro.json()  # Converte os dados do carro para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o carro não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'Carro não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo carro
def create_carro(carro_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in carro_data for key in ['modelo', 'marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Modelo, marca e ano são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo carro
    novo_carro = Carro(
        modelo=carro_data['modelo'],
        marca=carro_data['marca'],
        ano=carro_data['ano']
    )
    
    db.session.add(novo_carro)  # Adiciona o novo carro ao banco de dados
    db.session.commit()  # Confirma a transação no banco

# Função para atualizar um carro por ID
def update_carro(carro_id, carro_data):
    carro = Carro.query.get(carro_id)  # Busca o carro pelo ID

    if not carro:  # Se o carro não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'Carro não encontrado.'}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response

    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in carro_data for key in ['modelo', 'marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Modelo, marca e ano são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

    # Atualiza os dados do carro
    carro.modelo = carro_data['modelo']
    carro.marca = carro_data['marca']
    carro.ano = carro_data['ano']

    db.session.commit()  # Confirma a atualização no banco de dados

    # Resposta de sucesso com os dados do novo carro
    response = make_response(
        json.dumps({
            'mensagem': 'Carro cadastrado com sucesso.',
            'carro': carro.json()  # Retorna os dados do carro cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

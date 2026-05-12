from models.jogo_models import Jogo # Importa o modelo jogo
from db import db  # Importa a conexão com o banco de dados
import json
from flask import make_response, request

# Função para obter todos os jogos
def get_jogos():
    jogos = jogos.query.all()  # Busca todos os jogos no banco de dados
    response = make_response(
        json.dumps({
            'mensagem': 'Lista de jogos.',
            'dados': [jogo.json() for jogo in jogos]  # Converte os objetos de jogo para JSON
        }, ensure_ascii=False, sort_keys=False)  # Mantém caracteres especiais corretamente formatados
    )
    response.headers['Content-Type'] = 'application/json'  # Define o tipo de conteúdo como JSON
    return response

# Função para obter um jogo específico por ID
def get_jogo_by_id(jogo_id):
    jogo = Jogo.query.get(jogo_id)  # Busca o jogo pelo ID

    if jogo:  # Verifica se o jogo foi encontrado
        response = make_response(
            json.dumps({
                'mensagem': 'Jogo encontrado.',
                'dados': jogo.json()  # Converte os dados do jogo para formato JSON
            }, ensure_ascii=False, sort_keys=False)
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que o tipo da resposta seja JSON
        return response
    else:
        # Se o jogo não for encontrado, retorna erro com código 404
        response = make_response(
            json.dumps({'mensagem': 'Jogo não encontrado.', 'dados': {}}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

# Função para criar um novo jogo
def create_jogo(jogo_data):
    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogo_data for key in ['modelo', 'marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Modelo, marca e ano são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response
    
    # Se os dados forem válidos, cria o novo jogo
    novo_jogo = Jogo(
        modelo=jogo_data['modelo'],
        marca=jogo_data['marca'],
        ano=jogo_data['ano']
    )
    
    db.session.add(novo_jogo)  # Adiciona o novo jogo ao banco de dados
    db.session.commit()  # Confirma a transação no banco

# Função para atualizar um jogo por ID
def update_jogo(jogo_id, jogo_data):
    jogo = Jogo.query.get(jogo_id)  # Busca o jogo pelo ID

    if not jogo:  # Se o jogo não for encontrado, retorna erro
        response = make_response(
            json.dumps({'mensagem': 'jogo não encontrado.'}, ensure_ascii=False),
            404  # Código HTTP 404 para "Não encontrado"
        )
        response.headers['Content-Type'] = 'application/json'  # Garante que a resposta seja em JSON
        return response

    # Valida se todos os campos obrigatórios foram fornecidos
    if not all(key in jogo_data for key in ['modelo', 'marca', 'ano']):
        response = make_response(
            json.dumps({'mensagem': 'Dados inválidos. Modelo, marca e ano são obrigatórios.'}, ensure_ascii=False),
            400  # Código HTTP 400 para requisição inválida
        )
        response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
        return response

    # Atualiza os dados do jogo
    jogo.modelo = jogo_data['modelo']
    jogo.marca = jogo_data['marca']
    jogo.ano = jogo_data['ano']

    db.session.commit()  # Confirma a atualização no banco de dados

    # Resposta de sucesso com os dados do novo jogo
    response = make_response(
        json.dumps({
            'mensagem': 'Jogo cadastrado com sucesso.',
            'jogo': jogo.json()  # Retorna os dados do jogo cadastrado
        }, ensure_ascii=False, sort_keys=False)
    )
    response.headers['Content-Type'] = 'application/json'  # Define que a resposta é em JSON
    return response

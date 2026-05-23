from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from config import config, Config
from db import db
from datetime import datetime
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])

# CORS
CORS(app, resources={
    r"/api/*": {
        "origins": app.config.get('ALLOWED_ORIGINS', ['http://localhost:5000']),
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# ═══════════════════════════════════════════════════════════
# ROTAS ESTÁTICAS
# ═══════════════════════════════════════════════════════════

@app.route('/')
def index():
    try:
        return send_from_directory('frontend', 'index.html')
    except:
        return jsonify({'status': 'ok', 'message': 'Conscience Psicologia API'})

# ═══════════════════════════════════════════════════════════
# HEALTH CHECK
# ═══════════════════════════════════════════════════════════

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({
        'status': 'ok',
        'app': app.config.get('APP_NAME'),
        'professional': app.config.get('PROFESSIONAL_NAME'),
        'crp': app.config.get('CRP_NUMBER')
    })

# ═══════════════════════════════════════════════════════════
# PACIENTES
# ═══════════════════════════════════════════════════════════

@app.route('/api/pacientes', methods=['GET'])
def get_pacientes():
    pacientes = db.get_pacientes()
    return jsonify({
        'success': True,
        'data': pacientes,
        'total': len(pacientes)
    })

@app.route('/api/pacientes/<int:paciente_id>', methods=['GET'])
def get_paciente(paciente_id):
    paciente = db.get_paciente(paciente_id)
    if not paciente:
        return jsonify({'success': False, 'error': 'Paciente não encontrado'}), 404
    return jsonify({'success': True, 'data': paciente})

@app.route('/api/pacientes', methods=['POST'])
def criar_paciente():
    data = request.get_json()
    if not data.get('nome'):
        return jsonify({'success': False, 'error': 'Nome é obrigatório'}), 400

    paciente = db.criar_paciente(**data)
    if not paciente:
        return jsonify({'success': False, 'error': 'Erro ao criar paciente'}), 500

    return jsonify({'success': True, 'data': paciente}), 201

@app.route('/api/pacientes/<int:paciente_id>', methods=['PUT'])
def atualizar_paciente(paciente_id):
    data = request.get_json()
    paciente = db.atualizar_paciente(paciente_id, **data)
    if not paciente:
        return jsonify({'success': False, 'error': 'Erro ao atualizar paciente'}), 500

    return jsonify({'success': True, 'data': paciente})

@app.route('/api/pacientes/<int:paciente_id>', methods=['DELETE'])
def deletar_paciente(paciente_id):
    if not db.deletar_paciente(paciente_id):
        return jsonify({'success': False, 'error': 'Erro ao deletar paciente'}), 500

    return jsonify({'success': True, 'message': 'Paciente deletado'})

# ═══════════════════════════════════════════════════════════
# SESSÕES
# ═══════════════════════════════════════════════════════════

@app.route('/api/sessoes', methods=['GET'])
def get_sessoes():
    paciente_id = request.args.get('paciente_id', type=int)
    origem = request.args.get('origem')
    status = request.args.get('status')

    filters = {}
    if paciente_id:
        filters['paciente_id'] = paciente_id
    if origem:
        filters['origem'] = origem
    if status:
        filters['status_pagamento'] = status

    sessoes = db.get_sessoes(filters if filters else None)
    return jsonify({
        'success': True,
        'data': sessoes,
        'total': len(sessoes)
    })

@app.route('/api/sessoes', methods=['POST'])
def criar_sessao():
    data = request.get_json()
    paciente_id = data.get('paciente_id')
    data_sessao = data.get('data_sessao')

    if not paciente_id or not data_sessao:
        return jsonify({'success': False, 'error': 'paciente_id e data_sessao são obrigatórios'}), 400

    sessao = db.criar_sessao(paciente_id, data_sessao, **{k: v for k, v in data.items() if k not in ['paciente_id', 'data_sessao']})
    if not sessao:
        return jsonify({'success': False, 'error': 'Erro ao criar sessão'}), 500

    return jsonify({'success': True, 'data': sessao}), 201

@app.route('/api/sessoes/<int:sessao_id>', methods=['PUT'])
def atualizar_sessao(sessao_id):
    data = request.get_json()
    sessao = db.atualizar_sessao(sessao_id, **data)
    if not sessao:
        return jsonify({'success': False, 'error': 'Erro ao atualizar sessão'}), 500

    return jsonify({'success': True, 'data': sessao})

@app.route('/api/sessoes/<int:sessao_id>', methods=['DELETE'])
def deletar_sessao(sessao_id):
    if not db.deletar_sessao(sessao_id):
        return jsonify({'success': False, 'error': 'Erro ao deletar sessão'}), 500

    return jsonify({'success': True, 'message': 'Sessão deletada'})

# ═══════════════════════════════════════════════════════════
# AGENDAMENTOS
# ═══════════════════════════════════════════════════════════

@app.route('/api/agendamentos', methods=['GET'])
def get_agendamentos():
    data = request.args.get('data')
    agendamentos = db.get_agendamentos(data)
    return jsonify({
        'success': True,
        'data': agendamentos,
        'total': len(agendamentos)
    })

@app.route('/api/agendamentos', methods=['POST'])
def criar_agendamento():
    data = request.get_json()
    paciente_id = data.get('paciente_id')
    data_agend = data.get('data')
    hora = data.get('hora')

    if not all([paciente_id, data_agend, hora]):
        return jsonify({'success': False, 'error': 'paciente_id, data e hora são obrigatórios'}), 400

    agendamento = db.criar_agendamento(paciente_id, data_agend, hora, **{k: v for k, v in data.items() if k not in ['paciente_id', 'data', 'hora']})
    if not agendamento:
        return jsonify({'success': False, 'error': 'Erro ao criar agendamento'}), 500

    return jsonify({'success': True, 'data': agendamento}), 201

@app.route('/api/agendamentos/<int:agendamento_id>', methods=['PUT'])
def atualizar_agendamento(agendamento_id):
    data = request.get_json()
    agendamento = db.atualizar_agendamento(agendamento_id, **data)
    if not agendamento:
        return jsonify({'success': False, 'error': 'Erro ao atualizar agendamento'}), 500

    return jsonify({'success': True, 'data': agendamento})

@app.route('/api/agendamentos/<int:agendamento_id>', methods=['DELETE'])
def deletar_agendamento(agendamento_id):
    if not db.deletar_agendamento(agendamento_id):
        return jsonify({'success': False, 'error': 'Erro ao deletar agendamento'}), 500

    return jsonify({'success': True, 'message': 'Agendamento deletado'})

# ═══════════════════════════════════════════════════════════
# NOTAS FISCAIS
# ═══════════════════════════════════════════════════════════

@app.route('/api/nf/pendentes', methods=['GET'])
def get_nfs_pendentes():
    nfs = db.get_nfs_pendentes()
    return jsonify({
        'success': True,
        'data': nfs,
        'total': len(nfs)
    })

@app.route('/api/nf', methods=['POST'])
def registrar_nf():
    data = request.get_json()
    sessao_id = data.get('sessao_id')
    data_emissao = data.get('data_emissao')

    if not sessao_id or not data_emissao:
        return jsonify({'success': False, 'error': 'sessao_id e data_emissao são obrigatórios'}), 400

    nf = db.registrar_nf(sessao_id, data_emissao, data.get('numero_nf'))
    if not nf:
        return jsonify({'success': False, 'error': 'Erro ao registrar NF'}), 500

    return jsonify({'success': True, 'data': nf}), 201

# ═══════════════════════════════════════════════════════════
# ALERTAS & ESTATÍSTICAS
# ═══════════════════════════════════════════════════════════

@app.route('/api/alertas', methods=['GET'])
def get_alertas():
    alertas = db.gerar_alertas()
    return jsonify({
        'success': True,
        'data': alertas,
        'total': len(alertas)
    })

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Retorna estatísticas do dashboard"""
    try:
        sessoes = db.get_sessoes()
        pacientes = db.get_pacientes()

        # Calcular totais
        total_recebido = sum(s.get('valor', 0) for s in sessoes if s.get('status_pagamento') == 'pago')
        total_pendente = sum(s.get('valor', 0) for s in sessoes if s.get('status_pagamento') in ['pendente', 'atraso'])
        nfs_pendentes = sum(1 for s in sessoes if s.get('nf_emitida') == False and s.get('status_pagamento') == 'pago')

        return jsonify({
            'success': True,
            'data': {
                'total_pacientes': len(pacientes),
                'total_sessoes': len(sessoes),
                'total_recebido': total_recebido,
                'total_pendente': total_pendente,
                'nfs_pendentes': nfs_pendentes
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ═══════════════════════════════════════════════════════════
# ERROR HANDLERS
# ═══════════════════════════════════════════════════════════

@app.errorhandler(404)
def not_found(error):
    return jsonify({'success': False, 'error': 'Rota não encontrada'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'success': False, 'error': 'Erro interno do servidor'}), 500

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', True), host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from db import db
from datetime import datetime
import os

app = Flask(__name__, static_folder='frontend', static_url_path='')
app.config['DEBUG'] = True

# CORS
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
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
        'app': 'Conscience Psicologia',
        'professional': 'Rosa Almeida',
        'crp': '03/11768'
    })

# ═══════════════════════════════════════════════════════════
# DASHBOARD & STATS
# ═══════════════════════════════════════════════════════════

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Retorna estatísticas do dashboard"""
    try:
        sessoes = db.get_sessoes()
        pacientes = db.get_pacientes()

        # Particular
        part = [s for s in sessoes if s.get('origem') == 'particular']
        total_recebido = sum(s.get('valor', 0) for s in part if s.get('status') == 'pago')
        total_pendente = sum(s.get('valor', 0) for s in part if s.get('status') in ['pendente', 'atraso'])
        nfs_pendentes = sum(1 for s in part if not s.get('nf') and s.get('status') == 'pago')

        # Planos
        planos = [s for s in sessoes if s.get('origem') != 'particular']
        prev_plano = 0
        for p in planos:
            sessoes_pend = (p.get('sessoes', 0) or 0) - (p.get('pagas', 0) or 0)
            valor_unit = p.get('valorunit', 0) or 0
            if 'amar' in (p.get('origem') or ''):
                prev_plano += sessoes_pend * valor_unit * 0.5
            else:
                prev_plano += sessoes_pend * valor_unit

        return jsonify({
            'success': True,
            'data': {
                'total_pacientes': len(pacientes),
                'total_sessoes': len(sessoes),
                'total_recebido': total_recebido,
                'total_pendente': total_pendente,
                'nfs_pendentes': nfs_pendentes,
                'prev_planos': prev_plano
            }
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ═══════════════════════════════════════════════════════════
# SESSÕES / REGISTROS
# ═══════════════════════════════════════════════════════════

@app.route('/api/sessoes', methods=['GET'])
def get_sessoes():
    """Retorna sessões com filtros"""
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

@app.route('/api/sessoes/<int:sessao_id>', methods=['GET'])
def get_sessao(sessao_id):
    """Retorna uma sessão específica"""
    sessao = db.get_paciente(sessao_id)
    if not sessao:
        return jsonify({'success': False, 'error': 'Sessão não encontrada'}), 404
    return jsonify({'success': True, 'data': sessao})

@app.route('/api/sessoes', methods=['POST'])
def criar_sessao():
    """Cria uma nova sessão"""
    data = request.get_json()
    paciente_id = data.get('paciente_id', 0)
    data_sessao = data.get('data', '')
    # Remove paciente_id e data para não duplicar em **kwargs
    kwargs = {k: v for k, v in data.items() if k not in ['paciente_id', 'data']}
    result = db.criar_sessao(paciente_id, data_sessao, **kwargs)
    if not result:
        return jsonify({'success': False, 'error': 'Erro ao criar sessão'}), 500
    return jsonify({'success': True, 'data': result}), 201

@app.route('/api/sessoes/<int:sessao_id>', methods=['PUT'])
def atualizar_sessao(sessao_id):
    """Atualiza uma sessão"""
    data = request.get_json()
    sessao = db.atualizar_sessao(sessao_id, **data)
    if not sessao:
        return jsonify({'success': False, 'error': 'Erro ao atualizar sessão'}), 500
    return jsonify({'success': True, 'data': sessao})

@app.route('/api/sessoes/<int:sessao_id>', methods=['DELETE'])
def deletar_sessao(sessao_id):
    """Deleta uma sessão"""
    if not db.deletar_sessao(sessao_id):
        return jsonify({'success': False, 'error': 'Erro ao deletar sessão'}), 500
    return jsonify({'success': True, 'message': 'Sessão deletada'})

# ═══════════════════════════════════════════════════════════
# PACIENTES
# ═══════════════════════════════════════════════════════════

@app.route('/api/pacientes', methods=['GET'])
def get_pacientes():
    """Retorna todos os pacientes"""
    pacientes = db.get_pacientes()
    return jsonify({
        'success': True,
        'data': pacientes,
        'total': len(pacientes)
    })

@app.route('/api/pacientes/<int:paciente_id>', methods=['GET'])
def get_paciente(paciente_id):
    """Retorna um paciente específico"""
    paciente = db.get_paciente(paciente_id)
    if not paciente:
        return jsonify({'success': False, 'error': 'Paciente não encontrado'}), 404
    return jsonify({'success': True, 'data': paciente})

@app.route('/api/pacientes', methods=['POST'])
def criar_paciente():
    """Cria um novo paciente"""
    data = request.get_json()
    if not data.get('nome'):
        return jsonify({'success': False, 'error': 'Nome é obrigatório'}), 400

    paciente = db.criar_paciente(data.get('nome'), **data)
    if not paciente:
        return jsonify({'success': False, 'error': 'Erro ao criar paciente'}), 500

    return jsonify({'success': True, 'data': paciente}), 201

@app.route('/api/pacientes/<int:paciente_id>', methods=['PUT'])
def atualizar_paciente(paciente_id):
    """Atualiza um paciente"""
    data = request.get_json()
    return atualizar_sessao(paciente_id)

@app.route('/api/pacientes/<int:paciente_id>', methods=['DELETE'])
def deletar_paciente(paciente_id):
    """Deleta um paciente"""
    if not db.deletar_sessao(paciente_id):
        return jsonify({'success': False, 'error': 'Erro ao deletar paciente'}), 500
    return jsonify({'success': True, 'message': 'Paciente deletado'})

# ═══════════════════════════════════════════════════════════
# AGENDAMENTOS
# ═══════════════════════════════════════════════════════════

@app.route('/api/agendamentos', methods=['GET'])
def get_agendamentos():
    """Retorna agendamentos"""
    data = request.args.get('data')
    agendamentos = db.get_agendamentos(data)
    return jsonify({
        'success': True,
        'data': agendamentos,
        'total': len(agendamentos)
    })

@app.route('/api/agendamentos', methods=['POST'])
def criar_agendamento():
    """Cria um novo agendamento"""
    data = request.get_json()
    agendamento = db.criar_agendamento(
        data.get('paciente_id', 0),
        data.get('data', ''),
        data.get('hora', ''),
        **{k: v for k, v in data.items() if k not in ['paciente_id', 'data', 'hora']}
    )
    if not agendamento:
        return jsonify({'success': False, 'error': 'Erro ao criar agendamento'}), 500
    return jsonify({'success': True, 'data': agendamento}), 201

@app.route('/api/agendamentos/<int:agendamento_id>', methods=['PUT'])
def atualizar_agendamento(agendamento_id):
    """Atualiza um agendamento"""
    data = request.get_json()
    agendamento = db.atualizar_agendamento(agendamento_id, **data)
    if not agendamento:
        return jsonify({'success': False, 'error': 'Erro ao atualizar agendamento'}), 500
    return jsonify({'success': True, 'data': agendamento})

@app.route('/api/agendamentos/<int:agendamento_id>', methods=['DELETE'])
def deletar_agendamento(agendamento_id):
    """Deleta um agendamento"""
    if not db.deletar_agendamento(agendamento_id):
        return jsonify({'success': False, 'error': 'Erro ao deletar agendamento'}), 500
    return jsonify({'success': True, 'message': 'Agendamento deletado'})

# ═══════════════════════════════════════════════════════════
# NOTAS FISCAIS
# ═══════════════════════════════════════════════════════════

@app.route('/api/nf/pendentes', methods=['GET'])
def get_nfs_pendentes():
    """Retorna NFs pendentes"""
    nfs = db.get_nfs_pendentes()
    return jsonify({
        'success': True,
        'data': nfs,
        'total': len(nfs)
    })

@app.route('/api/nf', methods=['POST'])
def registrar_nf():
    """Registra uma nota fiscal"""
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
# ALERTAS
# ═══════════════════════════════════════════════════════════

@app.route('/api/alertas', methods=['GET'])
def get_alertas():
    """Retorna alertas"""
    alertas = db.gerar_alertas()
    return jsonify({
        'success': True,
        'data': alertas,
        'total': len(alertas)
    })

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
    app.run(debug=True, host='0.0.0.0', port=3000)

#!/usr/bin/env python3
"""
Script para migrar dados do localStorage (HTML) para Supabase
Execute: python migrate_data.py <caminho-para-arquivo.html>
"""

import json
import sys
from datetime import datetime
from db import db

# Dados de exemplo do localStorage que será preenchido pelo usuário
DADOS_EXEMPLO = [
    {"id": 1, "nome": "ANDRE", "origem": "particular", "tipopart": "individual", "data": "2026-05-15", "datapgto": "", "valor": 0, "status": "pendente", "nf": False, "nfdata": "", "nfnum": "", "forma": "PIX"},
    {"id": 2, "nome": "CAROL", "origem": "particular", "tipopart": "individual", "data": "2026-04-06", "datapgto": "", "valor": 100, "status": "pendente", "nf": False, "nfdata": "", "nfnum": "", "forma": "Cartão"},
]

def migrar_dados_localStorage(dados_json):
    """Migra dados do localStorage para Supabase"""
    print("🔄 Iniciando migração de dados...")

    # Parse dados
    try:
        dados = json.loads(dados_json) if isinstance(dados_json, str) else dados_json
    except json.JSONDecodeError as e:
        print(f"❌ Erro ao fazer parse do JSON: {e}")
        return False

    if not dados:
        print("⚠️  Nenhum dado para migrar")
        return False

    # Mapear pacientes únicos
    pacientes_map = {}
    sessoes_a_criar = []

    print(f"📊 Processando {len(dados)} registros...")

    for reg in dados:
        nome = reg.get('nome', '').strip().upper()
        if not nome:
            continue

        # Garantir que paciente existe
        if nome not in pacientes_map:
            print(f"👤 Criando paciente: {nome}")
            paciente = db.criar_paciente(
                nome=nome,
                observacoes=f"Migrado de localStorage em {datetime.now().strftime('%d/%m/%Y %H:%M')}"
            )
            if paciente:
                pacientes_map[nome] = paciente.get('id')
            else:
                print(f"  ❌ Erro ao criar paciente {nome}")
                continue

        paciente_id = pacientes_map[nome]

        # Preparar sessão
        data_sessao = reg.get('data')
        if not data_sessao:
            print(f"  ⚠️  {nome}: data_sessao vazia, pulando")
            continue

        origem = reg.get('origem', 'particular')

        sessao_data = {
            'paciente_id': paciente_id,
            'data_sessao': data_sessao,
            'origem': origem,
            'status_pagamento': reg.get('status', 'pendente'),
            'observacoes': reg.get('obs', '') or None,
        }

        # Adicionar dados específicos por origem
        if origem == 'particular':
            sessao_data.update({
                'tipo': reg.get('tipopart', 'individual'),
                'valor': reg.get('valor') or 0,
                'data_pagamento': reg.get('datapgto') or None,
                'forma_pagamento': reg.get('forma', 'PIX'),
                'nf_emitida': reg.get('nf', False),
                'data_emissao_nf': reg.get('nfdata') or None,
                'numero_nf': reg.get('nfnum') or None,
            })
        else:
            # Plano de saúde (Volare/Amar)
            sessao_data.update({
                'convenio': reg.get('convenio') or None,
                'duracao_plano': int(reg.get('duracao')) if reg.get('duracao') else 20,
                'valor_unitario': reg.get('valorunit') or 0,
                'numero_guia': reg.get('guia') or None,
                'sessoes_realizadas': reg.get('sessoes', 0),
                'sessoes_pagas': reg.get('pagas', 0),
            })

        sessoes_a_criar.append((nome, sessao_data))

    # Criar sessões
    print(f"\n💾 Criando {len(sessoes_a_criar)} sessões...")
    sucesso = 0
    erro = 0

    for nome, sessao_data in sessoes_a_criar:
        try:
            sessao = db.criar_sessao(**sessao_data)
            if sessao:
                sucesso += 1
                print(f"  ✅ {nome} - {sessao_data['data_sessao']}")
            else:
                erro += 1
                print(f"  ❌ Erro ao criar sessão para {nome}")
        except Exception as e:
            erro += 1
            print(f"  ❌ Erro para {nome}: {e}")

    print(f"\n{'='*50}")
    print(f"✅ Pacientes criados: {len(pacientes_map)}")
    print(f"✅ Sessões criadas: {sucesso}")
    print(f"❌ Erros: {erro}")
    print(f"{'='*50}")

    return erro == 0

def main():
    print("=" * 50)
    print("MIGRAÇÃO CONSCIENCE PSICOLOGIA")
    print("localStorage → Supabase")
    print("=" * 50)

    if len(sys.argv) > 1:
        # Ler arquivo HTML
        html_file = sys.argv[1]
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Extrair DADOS_INICIAIS do HTML
            import re
            match = re.search(r'var DADOS_INICIAIS\s*=\s*(\[.*?\]);', content, re.DOTALL)
            if match:
                dados_json = match.group(1)
                migrar_dados_localStorage(dados_json)
            else:
                print("❌ Não foi possível encontrar DADOS_INICIAIS no HTML")
        except FileNotFoundError:
            print(f"❌ Arquivo não encontrado: {html_file}")
    else:
        print("\n📌 Uso:")
        print("  python migrate_data.py <caminho/arquivo.html>")
        print("\nExemplo:")
        print("  python migrate_data.py ~/Downloads/gestao_rosa_almeida_11.html")
        print("\nOu forneça os dados diretamente em formato JSON")

if __name__ == '__main__':
    main()

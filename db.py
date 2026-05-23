from supabase import create_client, Client
from config import Config
from typing import List, Dict, Any
import json
from datetime import datetime

class Database:
    def __init__(self):
        self.url = Config.SUPABASE_URL
        self.key = Config.SUPABASE_KEY
        self.client: Client = None

        # Só conecta se tiver as credenciais
        print(f"[DB] SUPABASE_URL={self.url is not None}, SUPABASE_KEY={self.key is not None}")
        if self.url and self.key:
            try:
                self.client = create_client(self.url, self.key)
                print(f"[DB] ✅ Conectado ao Supabase com sucesso")
            except Exception as e:
                print(f"[DB] ❌ Erro ao conectar ao Supabase: {e}")
                self.client = None
        else:
            print(f"[DB] ⚠️  Credenciais do Supabase não configuradas")

    # ═══════════════════════════════════════════════════════════
    # PACIENTES
    # ═══════════════════════════════════════════════════════════

    def get_pacientes(self, user_id=None):
        """Retorna todos os pacientes"""
        if not self.client:
            return []
        try:
            response = self.client.table('pacientes').select('*').execute()
            return response.data
        except Exception as e:
            print(f"Erro ao obter pacientes: {e}")
            return []

    def get_paciente(self, paciente_id):
        """Retorna um paciente específico"""
        if not self.client:
            return None
        try:
            response = self.client.table('pacientes').select('*').eq('id', paciente_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao obter paciente: {e}")
            return None

    def criar_paciente(self, nome: str, **kwargs):
        """Cria um novo paciente"""
        if not self.client:
            return None
        try:
            data = {'nome': nome, **kwargs}
            response = self.client.table('pacientes').insert(data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar paciente: {e}")
            return None

    def atualizar_paciente(self, paciente_id, **kwargs):
        """Atualiza um paciente"""
        if not self.client:
            return None
        try:
            response = self.client.table('pacientes').update(kwargs).eq('id', paciente_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar paciente: {e}")
            return None

    def deletar_paciente(self, paciente_id):
        """Deleta um paciente"""
        if not self.client:
            return False
        try:
            response = self.client.table('pacientes').delete().eq('id', paciente_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar paciente: {e}")
            return False

    # ═══════════════════════════════════════════════════════════
    # SESSÕES
    # ═══════════════════════════════════════════════════════════

    def get_sessoes(self, filters=None):
        """Retorna sessões com filtros opcionais"""
        if not self.client:
            return []
        try:
            query = self.client.table('sessoes').select('*')
            if filters:
                for key, value in filters.items():
                    query = query.eq(key, value)
            response = query.execute()
            return response.data
        except Exception as e:
            print(f"Erro ao obter sessões: {e}")
            return []

    def criar_sessao(self, paciente_id: int, data_sessao: str, **kwargs):
        """Cria uma nova sessão"""
        if not self.client:
            return None
        try:
            data = {
                'paciente_id': paciente_id,
                'data_sessao': data_sessao,
                'created_at': datetime.now().isoformat(),
                **kwargs
            }
            response = self.client.table('sessoes').insert(data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar sessão: {e}")
            return None

    def atualizar_sessao(self, sessao_id, **kwargs):
        """Atualiza uma sessão"""
        if not self.client:
            return None
        try:
            kwargs['updated_at'] = datetime.now().isoformat()
            response = self.client.table('sessoes').update(kwargs).eq('id', sessao_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar sessão: {e}")
            return None

    def deletar_sessao(self, sessao_id):
        """Deleta uma sessão"""
        if not self.client:
            return False
        try:
            response = self.client.table('sessoes').delete().eq('id', sessao_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar sessão: {e}")
            return False

    # ═══════════════════════════════════════════════════════════
    # AGENDAMENTOS
    # ═══════════════════════════════════════════════════════════

    def get_agendamentos(self, data=None):
        """Retorna agendamentos"""
        if not self.client:
            return []
        try:
            query = self.client.table('agendamentos').select('*')
            if data:
                query = query.eq('data', data)
            response = query.execute()
            return response.data
        except Exception as e:
            print(f"Erro ao obter agendamentos: {e}")
            return []

    def criar_agendamento(self, paciente_id: int, data: str, hora: str, **kwargs):
        """Cria um novo agendamento"""
        if not self.client:
            return None
        try:
            data_agend = {
                'paciente_id': paciente_id,
                'data': data,
                'hora': hora,
                'confirmado': False,
                **kwargs
            }
            response = self.client.table('agendamentos').insert(data_agend).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao criar agendamento: {e}")
            return None

    def atualizar_agendamento(self, agendamento_id, **kwargs):
        """Atualiza um agendamento"""
        if not self.client:
            return None
        try:
            response = self.client.table('agendamentos').update(kwargs).eq('id', agendamento_id).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao atualizar agendamento: {e}")
            return None

    def deletar_agendamento(self, agendamento_id):
        """Deleta um agendamento"""
        if not self.client:
            return False
        try:
            response = self.client.table('agendamentos').delete().eq('id', agendamento_id).execute()
            return True
        except Exception as e:
            print(f"Erro ao deletar agendamento: {e}")
            return False

    # ═══════════════════════════════════════════════════════════
    # NOTAS FISCAIS
    # ═══════════════════════════════════════════════════════════

    def registrar_nf(self, sessao_id: int, data_emissao: str, numero_nf: str = None):
        """Registra uma nota fiscal"""
        if not self.client:
            return None
        try:
            data = {
                'sessao_id': sessao_id,
                'data_emissao': data_emissao,
                'numero_nf': numero_nf,
                'criada_em': datetime.now().isoformat()
            }
            response = self.client.table('notas_fiscais').insert(data).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Erro ao registrar NF: {e}")
            return None

    def get_nfs_pendentes(self):
        """Retorna NFs pendentes de emissão"""
        if not self.client:
            return []
        try:
            response = self.client.table('sessoes').select(
                'id, paciente_id (nome), data_sessao, valor, origem'
            ).eq('nf_emitida', False).eq('status_pagamento', 'pago').execute()
            return response.data
        except Exception as e:
            print(f"Erro ao obter NFs pendentes: {e}")
            return []

    # ═══════════════════════════════════════════════════════════
    # ALERTAS
    # ═══════════════════════════════════════════════════════════

    def gerar_alertas(self):
        """Gera alertas baseado nos dados"""
        alertas = []

        if not self.client:
            return alertas

        # Alertas de pagamento atrasado
        try:
            sessoes_atraso = self.client.table('sessoes').select('*').eq(
                'status_pagamento', 'atraso'
            ).execute()
            for sessao in sessoes_atraso.data:
                alertas.append({
                    'tipo': 'danger',
                    'mensagem': f"{sessao.get('paciente_id')} - pagamento em atraso"
                })
        except Exception as e:
            print(f"Erro ao gerar alertas de atraso: {e}")

        return alertas

# Instância global
db = Database()

# Conscience Psicologia - Sistema de Gestão

Sistema completo de gestão para consultório psicológico com integração Supabase e API Flask.

## 🚀 Configuração Inicial

### 1. Variáveis de Ambiente

Copie `.env.example` para `.env` e preencha:

```bash
cp .env.example .env
```

Edite `.env` com suas credenciais:
```
SUPABASE_URL=https://rnuwdhlqfjyqxqmxizcr.supabase.co
SUPABASE_KEY=sb_publishable_sSuHtSFEiQQ695n6H2zQsg_-fkwkJ9k
SUPABASE_SERVICE_KEY=sua-service-key-aqui (obter no Supabase)
```

### 2. Configurar Banco de Dados (Supabase)

1. Acesse [https://app.supabase.com](https://app.supabase.com)
2. Vá para **SQL Editor**
3. Copie todo o conteúdo de `schema.sql`
4. Execute no SQL Editor

**Ou importe o arquivo:**
```sql
-- Copie e cole todo o conteúdo de schema.sql no SQL Editor do Supabase
```

### 3. Instalar Dependências

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Executar Backend

```bash
python app.py
```

O servidor estará em `http://localhost:5000`

## 📁 Estrutura do Projeto

```
conscience-psicologia/
├── app.py              # Aplicação Flask principal
├── config.py           # Configurações
├── db.py               # Camada de banco de dados
├── schema.sql          # Schema do Supabase
├── requirements.txt    # Dependências Python
├── .env                # Variáveis de ambiente
├── .gitignore          # Arquivos a ignorar no Git
├── frontend/           # Interface HTML/JS
│   └── index.html      # Aplicação web adaptada
└── README.md           # Este arquivo
```

## 🔌 Endpoints da API

### Pacientes
- `GET /api/pacientes` - Listar todos
- `GET /api/pacientes/<id>` - Obter específico
- `POST /api/pacientes` - Criar novo
- `PUT /api/pacientes/<id>` - Atualizar
- `DELETE /api/pacientes/<id>` - Deletar

### Sessões
- `GET /api/sessoes?paciente_id=1&origem=particular` - Listar com filtros
- `POST /api/sessoes` - Criar nova sessão
- `PUT /api/sessoes/<id>` - Atualizar
- `DELETE /api/sessoes/<id>` - Deletar

### Agendamentos
- `GET /api/agendamentos?data=2026-05-23` - Listar por data
- `POST /api/agendamentos` - Criar novo
- `PUT /api/agendamentos/<id>` - Atualizar
- `DELETE /api/agendamentos/<id>` - Deletar

### Notas Fiscais
- `GET /api/nf/pendentes` - NFs para emitir
- `POST /api/nf` - Registrar emissão

### Estatísticas
- `GET /api/stats` - Dashboard
- `GET /api/alertas` - Alertas

## 📊 Campos Importantes

### Pacientes
- `nome` (obrigatório)
- `email`, `telefone`, `cpf`
- `endereco`, `cidade`, `estado`, `cep`
- `observacoes`

### Sessões
- `paciente_id` (obrigatório)
- `data_sessao` (obrigatório)
- `origem` (particular, volare, amar-ter, amar-qua, amar-qui)
- `tipo` (individual, plano4) - apenas para particular
- `valor`, `status_pagamento`
- Para planos: `convenio`, `duracao_plano`, `valor_unitario`
- NF: `nf_emitida`, `data_emissao_nf`, `numero_nf`

## 🔄 Migração de Dados (localStorage → Supabase)

Execute o script de migração para trazer dados do localStorage:

```bash
python migrate_data.py
```

## 🛠 Desenvolvimento

### Testar API localmente

```bash
# Health check
curl http://localhost:5000/api/health

# Listar pacientes
curl http://localhost:5000/api/pacientes

# Criar paciente
curl -X POST http://localhost:5000/api/pacientes \
  -H "Content-Type: application/json" \
  -d '{"nome": "João Silva", "email": "joao@example.com"}'
```

## 📝 Commits no Git

Estrutura de commits:

```
feat: descrição da feature
fix: descrição do fix
docs: atualização de documentação
refactor: refatoração de código
test: testes
```

Exemplo:
```bash
git add .
git commit -m "feat: integração Supabase para sessões"
git push origin main
```

## 🔐 Segurança

- Nunca commite `.env` (já está no .gitignore)
- Use SUPABASE_SERVICE_KEY apenas no backend
- SUPABASE_KEY (public key) é segura para frontend

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'supabase'"
```bash
pip install supabase==2.3.0
```

### Erro de CORS
Verifique `ALLOWED_ORIGINS` em `.env` e em `config.py`

### Erro de conexão Supabase
- Verifique se SUPABASE_URL e SUPABASE_KEY estão corretos
- Teste a conexão com `/api/health`

## 📞 Contato

Rosa Almeida - CRP 03/11768  
📱 (71) 99231-0234  
📧 rosa.psic@hotmail.com

---

**Versão**: 1.0.0  
**Última atualização**: 2026-05-23

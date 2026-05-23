# 🚀 SETUP - Conscience Psicologia

Guia passo a passo para configurar o projeto.

## 1️⃣ Configurar Banco de Dados (Supabase)

### Passo 1: Acessar o Supabase
1. Vá para [https://app.supabase.com](https://app.supabase.com)
2. Faça login com sua conta (já criada)
3. Selecione seu projeto

### Passo 2: Executar SQL Schema
1. Na sidebar, clique em **SQL Editor**
2. Clique em **+ New query**
3. Copie todo o conteúdo de `schema.sql`
4. Cole na área de código
5. Clique em **▶ Run** (canto superior direito)

✅ Seu banco de dados está pronto!

### Passo 3: Obter Service Key (opcional, apenas para desenvolvimento avançado)
1. Vá para **Settings** → **API**
2. Copie **service_role key**
3. Cole em `.env` na linha `SUPABASE_SERVICE_KEY`

---

## 2️⃣ Instalar e Rodar Backend (Python/Flask)

### Passo 1: Criar ambiente virtual
```bash
cd ~/conscience-psicologia
python3 -m venv venv
source venv/bin/activate
```

No Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### Passo 2: Instalar dependências
```bash
pip install -r requirements.txt
```

### Passo 3: Testar conexão
```bash
python -c "from db import db; print(db.get_pacientes())"
```

Deve retornar uma lista (vazia ou com dados).

### Passo 4: Iniciar servidor
```bash
python app.py
```

Você verá:
```
 * Running on http://127.0.0.1:5000
```

✅ Backend está rodando!

---

## 3️⃣ Testar API

Em outro terminal:

```bash
# Testar health check
curl http://localhost:5000/api/health

# Listar pacientes
curl http://localhost:5000/api/pacientes

# Criar paciente
curl -X POST http://localhost:5000/api/pacientes \
  -H "Content-Type: application/json" \
  -d '{"nome":"João Silva","email":"joao@example.com","telefone":"11999999999"}'
```

---

## 4️⃣ Migrar Dados do localStorage

Se você tiver dados do HTML antigo:

```bash
python migrate_data.py ~/Downloads/gestao_rosa_almeida_11.html
```

Isso vai:
- ✅ Ler os dados do arquivo HTML
- ✅ Criar pacientes no Supabase
- ✅ Criar sessões associadas

---

## 5️⃣ Configurar Git e GitHub

### Passo 1: Inicializar repositório
```bash
cd ~/conscience-psicologia
git init
git add .
git commit -m "feat: inicializar projeto Conscience Psicologia com Flask e Supabase"
```

### Passo 2: Criar repositório no GitHub
1. Vá para [https://github.com/new](https://github.com/new)
2. Nome: `conscience-psicologia`
3. Descrição: `Sistema de gestão para consultório psicológico`
4. Clique em **Create repository**

### Passo 3: Conectar repositório local com GitHub
```bash
git remote add origin https://github.com/seu-usuario/conscience-psicologia.git
git branch -M main
git push -u origin main
```

✅ Seu código está no GitHub!

---

## 6️⃣ Acessar Frontend

Abra em um navegador:
```
file:///Users/rosaalmeida/conscience-psicologia/frontend/index.html
```

Ou use um servidor local:
```bash
# Com Python 3
python -m http.server 8000
# Acesse http://localhost:8000/frontend/
```

---

## 📋 Checklist Final

- [ ] Supabase configurado e schema criado
- [ ] Backend Flask rodando em `http://localhost:5000`
- [ ] API testada com curl
- [ ] Dados migrados (se aplicável)
- [ ] Git inicializado
- [ ] Repositório GitHub criado
- [ ] Código pushed para GitHub
- [ ] Frontend acessível

---

## 🆘 Troubleshooting

### Erro: "connection refused" ao iniciar Flask
**Solução**: Certifique-se de que ninguém está usando a porta 5000
```bash
lsof -i :5000  # Ver o que está usando a porta
```

### Erro: "ModuleNotFoundError: No module named 'supabase'"
**Solução**:
```bash
pip install supabase==2.3.0
```

### Erro de CORS
**Solução**: Verifique `.env`
```
ALLOWED_ORIGINS=http://localhost:5000,file://
```

### Erro: "Variáveis de ambiente não carregadas"
**Solução**:
```bash
pip install python-dotenv
```

---

## 📞 Próximos Passos

1. **Expandir Frontend** - Implementar todas as abas (Pacientes, Sessões, Agendamentos)
2. **Adicionar Autenticação** - Login com Supabase Auth
3. **Implementar Relatórios** - Gerar PDFs
4. **Deploy** - Colocar em produção (Heroku, Railway, Render)

---

**Pronto para desenvolvER!** 🎉

# 🚀 Deploy no Vercel

Guia completo para rodar o projeto na nuvem com Vercel.

## ⚡ Pré-requisitos

- ✅ Código no GitHub (fazer push primeiro!)
- ✅ Conta Vercel criada (você já criou)
- ✅ Variáveis de ambiente configuradas

---

## 🔧 Configuração Vercel

### Passo 1: Conectar GitHub ao Vercel

1. Vá para [https://vercel.com/dashboard](https://vercel.com/dashboard)
2. Clique em **"New Project"**
3. Clique em **"Import Git Repository"**
4. Procure por `conscience-psicologia`
5. Clique em **"Import"**

### Passo 2: Configurar Variáveis de Ambiente

Na próxima tela, você verá **"Environment Variables"**:

Adicione:
```
SUPABASE_URL = https://rnuwdhlqfjyqxqmxizcr.supabase.co
SUPABASE_KEY = sb_publishable_sSuHtSFEiQQ695n6H2zQsg_-fkwkJ9k
FLASK_ENV = production
SECRET_KEY = seu-secret-key-muito-seguro-aqui
ALLOWED_ORIGINS = sua-url-vercel.vercel.app,https://seu-dominio.com
```

### Passo 3: Deploy

1. Clique em **"Deploy"**
2. Aguarde (pode levar 2-3 minutos)
3. Você verá ✅ **"Congratulations! Your project has been successfully deployed"**
4. Clique em **"Visit"** para abrir

---

## 📝 Arquivo vercel.json

Já criado no projeto! Contém:
```json
{
  "buildCommand": "pip install -r requirements.txt",
  "devCommand": "python app.py",
  "framework": "flask"
}
```

Este arquivo diz ao Vercel como rodar seu Flask!

---

## 🔐 Variáveis de Ambiente no Vercel

Após deploy:

1. Vá para **Settings** → **Environment Variables**
2. Adicione:
   - `SUPABASE_URL`
   - `SUPABASE_KEY`
   - `SECRET_KEY`
   - `ALLOWED_ORIGINS`

---

## ✅ Testar API em Produção

Depois que deploy terminar:

```bash
# Substitua pela sua URL do Vercel
curl https://seu-projeto.vercel.app/api/health

# Deve retornar:
# {"status":"ok","app":"Conscience Psicologia",...}
```

---

## 🌐 Acessar Frontend

Seu frontend estará em:
```
https://seu-projeto.vercel.app/frontend/
```

Ou configure redirecionamento para a raiz.

---

## 🔄 Deploy Automático

Toda vez que você fazer `git push` para `main`:

1. GitHub notifica Vercel
2. Vercel puxa código atualizado
3. Vercel executa build
4. Deploy automático!

**Sem fazer nada de sua parte!** ✅

---

## 🐛 Troubleshooting

### Erro: "Build failed"

Verifique logs em **Deployments** → clique no deployment → **Build Logs**

Causas comuns:
- Módulo Python não instalado → Verifique `requirements.txt`
- Variável de ambiente faltando → Adicione em Settings
- Porta incorreta → Flask deve usar porta 3000+ no Vercel

### Erro: "Connection refused to Supabase"

- Verifique `SUPABASE_URL` e `SUPABASE_KEY` em Environment Variables
- Não deve ter espaços extras
- Copie exatamente como em `.env` local

### Frontend não carrega

- Verifique se `frontend/index.html` existe
- API_URL no HTML deve apontar para sua URL Vercel
- Exemplo: `const API_URL = 'https://seu-projeto.vercel.app/api';`

---

## 📊 Monitoramento

No Vercel Dashboard você pode:

- ✅ Ver status do último deploy
- ✅ Visualizar logs
- ✅ Ver uso de resources
- ✅ Configurar domínio customizado
- ✅ Configurar CI/CD

---

## 🎯 Próximas Otimizações

1. **Domínio Custom** - Usar seu próprio domínio
2. **SSL/HTTPS** - Automático no Vercel ✅
3. **Cache** - Configurar cache de responses
4. **Monitoring** - Adicionar observability
5. **Backups** - Backup automático do Supabase

---

## 📞 Links Úteis

- [Vercel Dashboard](https://vercel.com/dashboard)
- [Vercel Docs - Flask](https://vercel.com/guides/deploying-flask-with-vercel)
- [Supabase Docs](https://supabase.com/docs)
- [Flask Deployment](https://flask.palletsprojects.com/en/3.0.x/deploying/)

---

## ✨ Status Final

```
Local:      http://localhost:5000        ✅
GitHub:     github.com/RosaPsic/...      (após push)
Vercel:     seu-projeto.vercel.app      (após deploy)
Supabase:   rnuwdhlqfjyqxqmxizcr...      ✅
```

Seu app está em 3 lugares! 🚀

---

**Pronto para deploy!** Siga os passos acima e sua aplicação estará no ar em minutos.

# 🚀 Push e Deploy Automático

Script automático para fazer push para GitHub e preparar Vercel em 2 minutos.

## 📋 Pré-requisitos

1. ✅ Repositório GitHub vazio criado em: https://github.com/new
   - Nome: `conscience-psicologia`
   - Descrição: `Sistema de gestão para consultório psicológico`
   - Público (recomendado)

2. ✅ Personal Access Token do GitHub

## 🔑 Gerar Personal Access Token

### Passo 1: Ir para configurações do GitHub
```
https://github.com/settings/tokens
```

### Passo 2: Gerar novo token
1. Clique em **"Generate new token (classic)"**
2. Dê um nome: `conscience-deploy`
3. Selecione escopo: **`repo`** (full control of private repositories)
4. Clique em **"Generate token"**
5. **COPIE O TOKEN** (é a única vez que aparece!)

### Exemplo de token:
```
ghp_1234567890abcdefghij1234567890abc
```

---

## 🚀 Executar Deploy Automático

### Passo 1: Preparar variável de ambiente

```bash
# Mac/Linux - execute isto no terminal:
export GITHUB_TOKEN=seu-token-aqui
```

**Exemplo:**
```bash
export GITHUB_TOKEN=ghp_1234567890abcdefghij1234567890abc
```

### Passo 2: Rodar script de deploy

```bash
cd ~/conscience-psicologia
chmod +x deploy.sh
bash deploy.sh
```

### Resultado esperado:
```
✅ Token encontrado
✅ Push realizado com sucesso!
```

---

## 🎯 Após o deploy automático:

### 1️⃣ Verificar GitHub
Acesse:
```
https://github.com/RosaPsic/conscience-psicologia
```

Você deve ver todos os arquivos! ✅

### 2️⃣ Deploy no Vercel

#### Opção A: Automático (recomendado)
1. Vá para: https://vercel.com/dashboard
2. Clique em **"New Project"**
3. Conecte seu repositório `conscience-psicologia`
4. Na próxima tela, adicione **Environment Variables**:

```
SUPABASE_URL=https://rnuwdhlqfjyqxqmxizcr.supabase.co
SUPABASE_KEY=sb_publishable_sSuHtSFEiQQ695n6H2zQsg_-fkwkJ9k
FLASK_ENV=production
SECRET_KEY=seu-secret-key-muito-seguro-aqui-pode-ser-qualquer-coisa
ALLOWED_ORIGINS=seu-projeto.vercel.app,localhost:5000
```

5. Clique em **"Deploy"**
6. Aguarde 2-3 minutos
7. Clique em **"Visit"** para abrir sua aplicação!

#### Opção B: Deploy manual
```bash
npm i -g vercel
vercel
# Siga as instruções
```

---

## ✅ Checklist Final

- [ ] Repositório criado em GitHub.com
- [ ] Personal Access Token gerado
- [ ] Variável `GITHUB_TOKEN` exportada
- [ ] Script `deploy.sh` executado
- [ ] Código push para GitHub (verificar em GitHub.com)
- [ ] Vercel conectado ao repositório
- [ ] Variáveis de ambiente adicionadas
- [ ] Deploy iniciado no Vercel
- [ ] URL do Vercel acessível

---

## 🆘 Troubleshooting

### Erro: "fatal: authentication failed"
- Token expirado ou inválido
- Gere um novo token em https://github.com/settings/tokens
- Exporte novamente: `export GITHUB_TOKEN=novo-token`

### Erro: "Remote already exists"
```bash
git remote remove origin
# Depois execute o script novamente
```

### Vercel build failed
- Verifique variáveis de ambiente
- Verifique logs em Vercel Dashboard
- Certifique-se de `requirements.txt` estar correto

### API não responde em Vercel
- Verificar `SUPABASE_URL` e `SUPABASE_KEY`
- Verificar se `FLASK_ENV=production`
- Checar logs de build/runtime no Vercel

---

## 📞 Links Úteis

- [GitHub Settings](https://github.com/settings/tokens)
- [Vercel Dashboard](https://vercel.com/dashboard)
- [Supabase Console](https://app.supabase.com)

---

## 🎉 Pronto!

Seu projeto está:
- ✅ No GitHub (versionado)
- ✅ No Vercel (na nuvem)
- ✅ Conectado ao Supabase (banco de dados)
- ✅ Pronto para produção!

**Deploy automático habilitado:** Toda vez que fizer `git push`, Vercel puxa e deploy automaticamente! 🚀

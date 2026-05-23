# 📤 Fazer Push para GitHub

## Opção 1: GitHub CLI (Recomendado - Mais Fácil)

### Passo 1: Instalar GitHub CLI
```bash
# Mac
brew install gh

# Ou baixe em: https://cli.github.com
```

### Passo 2: Fazer login
```bash
gh auth login
# Escolha: GitHub.com
# Escolha: HTTPS
# Autorize com seu navegador
```

### Passo 3: Criar repositório e fazer push
```bash
cd ~/conscience-psicologia

# Criar repositório
gh repo create conscience-psicologia --public --source=. --remote=origin --push

# Pronto! Seu código está no GitHub! ✅
```

---

## Opção 2: Usar SSH

### Passo 1: Gerar SSH key
```bash
ssh-keygen -t ed25519 -C "rosa.psic@hotmail.com"
# Pressione Enter para todas as perguntas (sem senha)
```

### Passo 2: Adicionar SSH key ao GitHub
```bash
# Copiar chave
cat ~/.ssh/id_ed25519.pub

# Ir para: https://github.com/settings/keys
# Clique em "New SSH key"
# Cole a chave
# Clique em "Add SSH key"
```

### Passo 3: Fazer push
```bash
cd ~/conscience-psicologia

# Remover HTTPS remote
git remote remove origin

# Adicionar SSH remote
git remote add origin git@github.com:RosaPsic/conscience-psicologia.git

# Fazer push
git push -u origin main
```

---

## Opção 3: Criar repositório na web e fazer push

### Passo 1: Criar no GitHub.com
1. Vá para https://github.com/new
2. Nome: `conscience-psicologia`
3. Descrição: `Sistema de gestão para consultório psicológico`
4. Clique em **Create repository**

### Passo 2: Usar Personal Access Token
```bash
cd ~/conscience-psicologia

# Remover remote anterior se existir
git remote remove origin

# Adicionar novo remote
git remote add origin https://github.com/RosaPsic/conscience-psicologia.git

# Fazer push
git push -u origin main

# Quando pedir autenticação:
# Username: RosaPsic
# Password: [Cole seu Personal Access Token]
```

### Como gerar Personal Access Token:
1. https://github.com/settings/tokens
2. Clique em "Generate new token"
3. Selecione escopo `repo` (full control)
4. Clique em "Generate token"
5. **Copie o token** (é a única vez que aparece)
6. Cole quando git pedir password

---

## ✅ Verificar se funcionou

Depois de fazer push, acesse:
```
https://github.com/RosaPsic/conscience-psicologia
```

Você deve ver todos os arquivos lá! ✅

---

## 🆘 Problemas?

### Erro: "Repository already exists"
```bash
git remote remove origin
git remote add origin https://github.com/RosaPsic/conscience-psicologia.git
git push -u origin main
```

### Erro: "Permission denied (publickey)"
Você não configurou SSH corretamente. Use a Opção 1 ou 3 em vez disso.

### Erro: "401 Unauthorized"
Token expirou ou é inválido. Gere um novo em https://github.com/settings/tokens

---

## ✨ Recomendação

**Use a Opção 1 (GitHub CLI)** - É a mais simples e moderna!

```bash
brew install gh
gh auth login
gh repo create conscience-psicologia --public --source=. --remote=origin --push
```

Pronto em 3 comandos! 🚀

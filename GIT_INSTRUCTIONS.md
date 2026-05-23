# 🚀 Enviar para GitHub

## Suas credenciais
- **GitHub**: Você já criou uma conta
- **Email**: rosa.psic@hotmail.com
- **Projeto**: `conscience-psicologia`

---

## Passo 1: Criar repositório no GitHub

1. Acesse [https://github.com/new](https://github.com/new)
2. Preencha:
   - **Repository name**: `conscience-psicologia`
   - **Description**: `Sistema de gestão para consultório psicológico com Flask e Supabase`
   - **Public**: Deixe como preferir
   - **Add a README**: Desmarque (já temos)
   - **Add .gitignore**: Desmarque (já temos)

3. Clique em **Create repository**

---

## Passo 2: Copiar URL do repositório

Após criar, você verá uma tela com:
```
https://github.com/seu-usuario/conscience-psicologia.git
```

Copie essa URL.

---

## Passo 3: Conectar e fazer push

Execute estes comandos:

```bash
cd ~/conscience-psicologia

# Adicionar remote
git remote add origin https://github.com/seu-usuario/conscience-psicologia.git

# Renomear branch para main (pode já estar)
git branch -M main

# Fazer push
git push -u origin main
```

**Se pedir autenticação:**
- Use seu **GitHub username**
- Para **senha**, use um **Personal Access Token**:
  1. GitHub → Settings → Developer settings → Personal access tokens
  2. Generate new token
  3. Selecione `repo` (full control)
  4. Copie o token
  5. Cole quando pedir

---

## Passo 4: Verificar no GitHub

Acesse:
```
https://github.com/seu-usuario/conscience-psicologia
```

Você deve ver todos os arquivos lá! ✅

---

## 📝 Commits futuros

Para cada mudança:

```bash
# 1. Ver mudanças
git status

# 2. Adicionar arquivos
git add .

# 3. Fazer commit
git commit -m "tipo: descrição

descrição detalhada se necessário"

# 4. Fazer push
git push
```

### Tipos de commit:
- `feat:` - Nova feature
- `fix:` - Correção de bug
- `docs:` - Documentação
- `refactor:` - Refatoração
- `test:` - Testes
- `chore:` - Manutenção

**Exemplo:**
```bash
git commit -m "feat: adicionar endpoint de estatísticas

- Implementar GET /api/stats
- Calcular totais por origem
- Adicionar estatísticas de NF pendente"
```

---

## 🔄 Atualizar localmente (quando trabalhar em múltiplos computadores)

```bash
git pull origin main
```

---

## ⚠️ NÃO fazer commit

Estes arquivos já estão no `.gitignore`:
- `.env` (variáveis sensíveis)
- `__pycache__/`
- `venv/`
- `*.egg-info/`
- `.vscode/`, `.idea/`

---

## ✅ Checklist

- [ ] Conta GitHub criada
- [ ] Repositório criado no GitHub
- [ ] Commit inicial feito localmente
- [ ] Remote adicionado com `git remote add origin`
- [ ] Push realizado com `git push -u origin main`
- [ ] Verificado no GitHub

---

**Pronto para colaborar!** 🎉

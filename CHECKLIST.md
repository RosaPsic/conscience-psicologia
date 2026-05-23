# ✅ CHECKLIST DE SETUP

Cole este arquivo em um editor de texto e marque conforme progride.

## FASE 1: SUPABASE (5 minutos)

- [ ] Acessar https://app.supabase.com
- [ ] Login com sua conta
- [ ] Selecionar projeto
- [ ] Ir para SQL Editor
- [ ] Clicar em "+ New query"
- [ ] Copiar conteúdo de `schema.sql`
- [ ] Colar no editor do Supabase
- [ ] Clicar em "Run" (canto superior direito)
- [ ] Aguardar "Success"
- [ ] Verificar em "Tables" que 4 tabelas foram criadas

## FASE 2: AMBIENTE LOCAL (2 minutos)

- [ ] Abrir terminal
- [ ] `cd ~/conscience-psicologia`
- [ ] `python3 -m venv venv`
- [ ] `source venv/bin/activate` (Windows: `venv\Scripts\activate`)
- [ ] Verificar prompt com `(venv)`

## FASE 3: INSTALAR DEPENDÊNCIAS (3 minutos)

- [ ] `pip install -r requirements.txt`
- [ ] Aguardar conclusão (pode levar 1-2 min)
- [ ] Verificar que não há erros

## FASE 4: RODAR BACKEND (1 minuto)

- [ ] `python app.py`
- [ ] Aguardar mensagem: "Running on http://127.0.0.1:5000"
- [ ] Deixar terminal aberto

## FASE 5: TESTAR API (em outro terminal - 2 minutos)

- [ ] Abrir novo terminal (não fechar o anterior)
- [ ] `curl http://localhost:5000/api/health`
- [ ] Deve retornar JSON com status "ok"
- [ ] `curl http://localhost:5000/api/pacientes`
- [ ] Deve retornar JSON com array vazio `[]`

## FASE 6: (OPCIONAL) MIGRAR DADOS (5 minutos)

- [ ] Se você tiver dados antigos do HTML:
- [ ] `python migrate_data.py ~/Downloads/gestao_rosa_almeida_11.html`
- [ ] Aguardar conclusão
- [ ] Verificar se pacientes foram criados

## FASE 7: GITHUB (5 minutos)

- [ ] Acessar https://github.com/new
- [ ] Preencher "Repository name": `conscience-psicologia`
- [ ] Clique em "Create repository"
- [ ] Copiar URL do repositório
- [ ] No terminal (onde app.py NÃO está rodando):
- [ ] `git remote add origin https://github.com/SEU-USUARIO/conscience-psicologia.git`
- [ ] `git push -u origin main`
- [ ] Digitar username e token do GitHub (se pedido)
- [ ] Verificar em GitHub se arquivos aparecem

## FASE 8: ACESSAR FRONTEND (1 minuto)

- [ ] Abrir navegador
- [ ] Ir para: `file:///Users/rosaalmeida/conscience-psicologia/frontend/index.html`
- [ ] Deve carregar interface Conscience
- [ ] Ver "Backend conectado em http://localhost:5000"

## ✅ PRONTO!

Se você marcou tudo acima, parabéns! 🎉

**Próximos passos:**
- Expandir interface (adicionar mais abas)
- Implementar cadastro de pacientes no frontend
- Adicionar autenticação
- Deploy em produção

---

## 🆘 SE ALGO DER ERRADO

### Erro: "ModuleNotFoundError: No module named 'supabase'"
```bash
pip install supabase==2.3.0
```

### Erro: "Connection refused" na API
- Backend está rodando? (`python app.py`)
- API está em http://127.0.0.1:5000?
- Tente novamente em outro terminal

### Erro: "CORS error"
- Verificar `.env` em ALLOWED_ORIGINS
- Deve incluir `http://localhost:5000`

### Git push rejected
- Verificar se repositório existe em GitHub
- Usar token ao invés de senha
- Usar `git push -u origin main` apenas na primeira vez

---

**Data de início:** 23 de Maio de 2026  
**Tempo estimado:** 20-30 minutos

#!/bin/bash

# Script de Deploy Automático - Conscience Psicologia
# Este script faz push para GitHub e prepara para Vercel

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║           DEPLOY AUTOMÁTICO - CONSCIENCE PSICOLOGIA           ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Cores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Variáveis
GITHUB_USER="RosaPsic"
REPO_NAME="conscience-psicologia"
GITHUB_REPO="https://github.com/${GITHUB_USER}/${REPO_NAME}.git"

echo -e "${YELLOW}📝 PASSO 1: Verificar credenciais${NC}"
echo ""

# Verificar se tem token do GitHub
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${RED}❌ Variável GITHUB_TOKEN não encontrada${NC}"
    echo ""
    echo "Para fazer push, você precisa de um Personal Access Token:"
    echo ""
    echo "1. Vá para: https://github.com/settings/tokens"
    echo "2. Clique em 'Generate new token'"
    echo "3. Selecione escopo 'repo'"
    echo "4. Copie o token"
    echo ""
    echo "Depois execute:"
    echo "  export GITHUB_TOKEN=seu-token-aqui"
    echo "  bash deploy.sh"
    echo ""
    exit 1
fi

echo -e "${GREEN}✅ Token encontrado${NC}"
echo ""

# PASSO 2: Fazer push para GitHub
echo -e "${YELLOW}📤 PASSO 2: Fazer push para GitHub${NC}"
echo ""

cd "$(dirname "$0")"

# Verificar se remote já existe
if git remote get-url origin > /dev/null 2>&1; then
    echo "Removendo remote anterior..."
    git remote remove origin
fi

# Adicionar remote com token
git remote add origin "https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_USER}/${REPO_NAME}.git"

# Fazer push
echo "Fazendo push para GitHub..."
if git push -u origin main; then
    echo -e "${GREEN}✅ Push realizado com sucesso!${NC}"
else
    echo -e "${RED}❌ Erro ao fazer push${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}🎯 PASSO 3: Próximos passos${NC}"
echo ""
echo "1️⃣  Verifique seu repositório:"
echo "    https://github.com/${GITHUB_USER}/${REPO_NAME}"
echo ""
echo "2️⃣  Para fazer deploy no Vercel:"
echo "    - Vá para: https://vercel.com/dashboard"
echo "    - Clique em 'New Project'"
echo "    - Clique em 'Import Git Repository'"
echo "    - Procure por '${REPO_NAME}'"
echo "    - Clique em 'Import'"
echo "    - Adicione variáveis de ambiente:"
echo "      • SUPABASE_URL=https://rnuwdhlqfjyqxqmxizcr.supabase.co"
echo "      • SUPABASE_KEY=sb_publishable_sSuHtSFEiQQ695n6H2zQsg_-fkwkJ9k"
echo "      • FLASK_ENV=production"
echo "      • SECRET_KEY=seu-secret-key-aqui"
echo "    - Clique em 'Deploy'"
echo ""
echo "3️⃣  Ou veja documentação completa em:"
echo "    - PUSH_GITHUB.md"
echo "    - VERCEL_DEPLOY.md"
echo ""

echo -e "${GREEN}╔════════════════════════════════════════════════════════════════╗"
echo "║                    ✅ DEPLOY COMPLETO!                        ║"
echo "╚════════════════════════════════════════════════════════════════╝${NC}"

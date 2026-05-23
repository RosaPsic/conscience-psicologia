import sys
import os

# Adicionar o diretório pai ao path para importar módulos
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel requires this export
def handler(request):
    return app(request)

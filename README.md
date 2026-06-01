# FinTrack API

API REST para o sistema de controle financeiro FinTrack. Fornece endpoints para gerenciamento de transações financeiras.

## 🚀 Tecnologias

- Python 3.14
- Django 6
- Django REST Framework
- SQLite (desenvolvimento)
- PostgreSQL (produção)

## 📋 Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /api/transactions/ | Lista todas as transações |
| POST | /api/transactions/ | Cria nova transação |
| GET | /api/transactions/{id}/ | Busca transação por ID |
| PUT | /api/transactions/{id}/ | Atualiza transação |
| DELETE | /api/transactions/{id}/ | Remove transação |

## 🔧 Como rodar localmente

```bash
# Clone o repositório
git clone https://github.com/kellzero/fintrack-api.git
cd fintrack-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Rode as migrações
python manage.py migrate

# Inicie o servidor
python manage.py runserver
```

Acesse http://localhost:8000/api/transactions/

## 🔗 Front-end

Interface desenvolvida em React + TypeScript: [fintrack](https://github.com/kellzero/fintrack)
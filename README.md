# Desafio-CME

Desafio-CME é um projeto desenvolvido como parte de um desafio técnico. Ele é uma aplicação web construída com Django, React e Docker, utilizando PostgreSQL como banco de dados. A aplicação oferece uma API para gerenciamento de materiais e usuários, utilizando autenticação JWT para segurança.

Pré-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:

Docker
Docker Compose
Python
Node
PostgreSql

Clonando o Repositório

git clone https://github.com/VasconcelosVictor/Desafio-CME.git

Entre no projeto 
cd BackEnd/
cd cme-backend/
python3 -m venv suavirtualenv
cd cmeBack/ (Raiz)

Variáveis de Ambiente

Edite o arquivo um arquivo .env na pasta dotenv_files com as seguintes variáveis:

SECRET_KEY="CHANGE-ME"

# 0 False, 1 True
DEBUG="1"

# Comma Separated values
ALLOWED_HOSTS="127.0.0.1, localhost"

DB_ENGINE="django.db.backends.postgresql"
POSTGRES_DB="CHANGE-ME"
POSTGRES_USER="CHANGE-ME"
POSTGRES_PASSWORD="CHANGE-ME"
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"

Executando o Docker Compose

docker-compose up --build

Migrações do Banco de Dados

docker exec -it <container_id> python manage.py migrate
Criando um Superusuário


docker exec -it <container_id> python manage.py createsuperuser
Acessando a Aplicação

Acesse a aplicação em http://127.0.0.1:8000/.

Funcionalidades
Autenticação
A autenticação é feita via JWT (JSON Web Token). Para obter um token JWT, você pode utilizar a rota de login da API:

Rota de Login: api/v1/login/ 

Método: POST

Parâmetros:

json

{
  "username": "seu_username",
  "password": "sua_senha"
}
Exemplo de resposta:

json

{
  "access": "seu_access_token",
  "refresh": "seu_refresh_token"
}

Rota de logout: api/v1/logout/
Método: POST
Parâmetros:

json
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxOTc5N
               zI0MiwiaWF0IjoxNzE5MTkyNDQyLCJqdGkiOiI4NTM0NTJmNzkxNGU0MmRhYTM4Mjk0ZjJhMWY3ZTVkYiIsIn
               VzZXJfaWQiOjJ9.1rAF94tOV-ZnoJljzm5zlMlVjpqEYsS8oWtS-tVLJFw"
}


Rota de Criação de Usuário: api/v1/register/ 

Método: POST

Parâmetros:

json
{
	"username":"victor",
	"first_name":"victor",
	"last_name":"vasconcelos",
	"email": "vic@gmail.com",
	"password":"1234",
	"role":"TECH"
}



API de Usuários
A API de usuários permite a criação, atualização, listagem e exclusão de usuários.

# Atenção em todas as Urls do sistema com excessao de login você deve inserir no Headers da sua requisição:  Authorization Bearer seu_access_token 

Método: GET
Listar Usuários: /api/v1/users/


Método: POST
Criar Usuário: /api/v1/users/

Exemplo de dados:

json

{
	"username":"victor",
	"first_name":"victor",
	"last_name":"vasconcelos",
	"email": "vic@gmail.com",
	"password":"1234",
	"role":"TECH"
}

API de Materiais
A API de materiais permite o gerenciamento de materiais.

Listar Materiais: /api/v1/materials/

Método: GET

Criar Material: /api/v1/materials/

Método: POST

Exemplo de dados:

json

{
	"name":"Bisturi",
	"data" :"2024-09-01",
	"type_material": "CIR",
	"stage":"etapa1"
}


O FrontEnd não foi concluido ainda em desenvolvimento .

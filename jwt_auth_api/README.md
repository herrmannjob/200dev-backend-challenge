# JWT Authentication API
Este projeto é uma API em Python utilizando Flask para autenticação JWT com controle de acesso baseado em funções (admin e user). A API também interage com endpoints externos simulados para obter dados de saúde, admin, e user.

## Funcionalidades:
- Autenticação JWT: O endpoint /token gera um token JWT para usuários autenticados.
- Controle de Acesso por Funções:
- Usuários com função user podem acessar a rota /user.
- Usuários com função admin podem acessar a rota /admin.
- Interação com API Externa: O sistema consome dados de serviços externos de saúde, dados de usuário, e dados administrativos.

## Pré-requisitos
- Python 3.8 ou superior
- Git
- Virtualenv (opcional, mas recomendado)

## Instalação

### Clone o repositório:

```sh
git clone https://github.com/seu-usuario/jwt-auth-api.git
cd jwt-auth-api
```

### Crie e ative um ambiente virtual:

No Linux/MacOS:
```sh
python3 -m venv venv
source venv/bin/activate
```

No Windows:
```sh
python -m venv venv
venv\Scripts\activate
```

### Instale as dependências do projeto:

```sh
pip install -r requirements.txt
```

### Configurações adicionais:

Certifique-se de que o Flask e os módulos JWT estão configurados corretamente e suas variáveis de ambiente estão definidas corretamente.

## Executando a API

Inicie o servidor Flask:

```sh
flask run
```
O servidor será iniciado em http://127.0.0.1:5000/.

## Testando o Projeto
Gerar Token JWT:
Para gerar um token JWT, faça uma requisição POST ao endpoint /token com as credenciais do usuário:

```sh
curl -X POST http://127.0.0.1:5000/token -H "Content-Type: application/json" -d '{"username": "user", "password": "L0XuwPOdS5U"}'
```

Exemplo de resposta (com um token JWT):

json
```sh
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1Ni..."
}
```

## Acessar Rotas Protegidas:
Rota /user (apenas para usuários com o papel user):
Use o token JWT no cabeçalho da requisição para acessar:

```sh
curl -X GET http://127.0.0.1:5000/user -H "Authorization: Bearer <seu_token_jwt>"
Rota /admin (apenas para usuários com o papel admin):
```

```sh
curl -X GET http://127.0.0.1:5000/admin -H "Authorization: Bearer <seu_token_jwt>"
```

## Rotas Simuladas
A API interage com os seguintes endpoints externos:

| NOME | ROTA |
| ------ | ------ |
| Health check | GET /fake/health |
| Admin data | GET /fake/admin |
| User data | GET /fake/user |


Estes endpoints retornam respostas simuladas para o sistema.

## Tecnologias Utilizadas
- Python: Linguagem principal do projeto.
- Flask: Framework web utilizado para criar a API.
- Flask-JWT-Extended: Extensão do Flask para JWT Authentication.
- Werkzeug: Utilizado para segurança de senhas com hashing.
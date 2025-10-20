MinhaAPI — Documentação Oficial

env está na gitignore, precisa criar toda vez que for usar

Índice
O que é MinhaAPI?
Instalação
Primeiros passos
Estrutura da API
Exemplos de uso
Configurações avançadas
Boas práticas
Perguntas frequentes (FAQ)
Contribuindo
Licença

O que é MinhaAPI?

MinhaAPI é uma biblioteca/framework leve e intuitiva para construir APIs RESTful de forma rápida e eficiente em Python. Inspirada em boas práticas modernas, MinhaAPI facilita a criação, validação e documentação automática das rotas da sua aplicação.

Instalação

Para começar a usar MinhaAPI, você só precisa do Python 3.8+ e instalar via pip:

pip install minhaapi

Se quiser testar a API localmente, recomendamos usar o servidor ASGI rápido:

pip install uvicorn

Primeiros passos

Vamos criar uma API simples que responde "Olá, mundo!".

from minhaapi import MinhaAPI

app = MinhaAPI()

@app.get("/")
def home():
    return {"message": "Olá, mundo!"}


Para rodar, salve o código acima em main.py e execute:

uvicorn main:app --reload

--reload reinicia o servidor automaticamente quando houver mudanças no código, ótimo para desenvolvimento.

Abra o navegador e acesse:

http://127.0.0.1:8000/


Você verá:

{"message": "Olá, mundo!"}

Estrutura da API
Rotas

As rotas definem os endpoints da sua API. Cada rota está associada a um método HTTP:
@app.get("/caminho") — responde a requisições GET
@app.post("/caminho") — responde a POST
@app.put("/caminho") — responde a PUT
@app.delete("/caminho") — responde a DELETE

Parâmetros

Você pode definir parâmetros na URL:

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


Aqui, item_id é um parâmetro do tipo inteiro extraído da URL.

Corpo da requisição

Para receber dados via JSON, defina parâmetros com tipos e MinhaAPI valida automaticamente:

from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    preco: float

@app.post("/items/")
def create_item(item: Item):
    return item

Exemplos de uso
Validação automática com Pydantic

MinhaAPI integra o Pydantic para validação dos dados de entrada e saída.

from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str

@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} criado com sucesso!"}


Se o JSON enviado não corresponder ao modelo, a API responde com erro 422 e uma mensagem clara.

Documentação automática

Sua API já terá documentação interativa acessível via:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

Você pode testar todos os endpoints diretamente pelo navegador.

Configurações avançadas
Middlewares

Você pode adicionar middlewares para interceptar requisições e respostas:

@app.middleware("http")
async def log_request(request, call_next):
    print(f"Requisição para {request.url.path}")
    response = await call_next(request)
    return response

Segurança e autenticação

MinhaAPI oferece suporte integrado para OAuth2, JWT, API Keys e outras estratégias.

Boas práticas

Sempre defina modelos para dados de entrada e saída.

Use validação automática para evitar erros comuns.

Documente cada rota com comentários para facilitar manutenção.

Utilize as ferramentas de documentação para testar sua API frequentemente.

Mantenha seu servidor atualizado para aproveitar melhorias de performance e segurança.

Perguntas frequentes (FAQ)

Como faço para retornar erros customizados?

Use exceções específicas:

from minhaapi import HTTPException

@app.get("/protected")
def protected():
    raise HTTPException(status_code=401, detail="Não autorizado")


POST: send data;
PUT: update data;
DELETE: delette data.

grater than = gt / maior que...
grater or equal = ge / maior ou igual...
lower than = lt / menor que...
lower or equal = le / menor ou igual...

exemplo de query parametro também


Minha API suporta WebSockets?

Sim! Você pode definir rotas para WebSocket nativamente.

Contribuindo

Quer contribuir? Veja o arquivo CONTRIBUTING.md no repositório para guias e código de conduta.

Licença

MinhaAPI está licenciada sob a licença MIT. Você pode usar, modificar e distribuir livremente, desde que mantenha os créditos aos autores originais.

É possível desenvolver um pouco de front-end usando o pacote Angular, Bootstrap e tailwind css, e conectá-lo ao Back-End. Futuramente ele será desenvolvido.

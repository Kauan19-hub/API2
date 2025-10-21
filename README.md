**<h2> Documentação Oficial</h2>**

###

API é uma **biblioteca**/**framework** leve e intuitiva para construir **APIs** **RESTful** de forma rápida e eficiente em **Python**. Inspirada em boas práticas
modernas, **API** facilita a criação, validação e documentação automática das rotas da sua aplicação.

###

**<h2>Começando</h2>**

Para começar a usar **API**, você só precisa do `Python 3.8+` e instalar via `pip`:

###
```python
pip install api
```

###

✅ Se quiser testar a API localmente, recomendamos usar o servidor ASGI rápido:

###
```python
pip install uvicorn
```

###

Vamos criar uma **API** simples que responde **"API With FastAPI"**.

###
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API With FastAPI"}
```

###

✅ Para rodar, salve o código acima em `main.py` e rode:

###
```powershell
uvicorn main:app --reload
```

###

`--reload` reinicia o servidor automaticamente quando houver mudanças no código, ótimo para **desenvolvimento**.

---

Abra o **navegador** e acesse:

###
```powershell
http://127.0.0.1:8000/
```

###

✅ Você verá: `{"message": "API With Python"}`

###

**<h2>Estrutura da API</h2>**

###

**Rotas**

###

As rotas definem os **endpoints** da sua **API**. Cada rota está associada a um método `HTTP`:

###
```python
@app.get("/caminho") ### responde a requisições GET
```

###
```python
@app.post("/caminho") ### responde a POST
```

###
```python
@app.put("/caminho") ### responde a PUT
```

###
```python
@app.delete("/caminho") ### responde a DELETE
```

###

**<h2>Parâmetros</h2>**

###

✅ Você pode definir parâmetros na `URL`:

###
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

###

Aqui, `item_id` é um parâmetro do tipo **inteiro** extraído da `URL`.

---

**<h2>Corpo da requisição</h2>**

###

Para receber dados via `JSON`, defina **parâmetros** com tipos e **API** valida automaticamente:

###
```python
from pydantic import BaseModel

class Item(BaseModel):
    nome: str
    preco: float

@app.post("/items/")
def create_item(item: Item):
    return item
```

###

**<h2>Exemplos de uso</h2>**

###

✅ Validação automática com `Pydantic`. **API** integra o `Pydantic` para validação dos dados de entrada e saída.

###
```python
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    email: str

@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    return {"mensagem": f"Usuário {usuario.nome} criado com sucesso!"}
```

###

> Se o `JSON` enviado não corresponder ao modelo, a **API** responde com erro `422` e uma mensagem clara.

---

**<h2>Documentação automática<h2>**

###

✅ Sua **API** já terá documentação **interativa** acessível via:

###
```powershell
Swagger UI: http://127.0.0.1:8000/docs
```

###
```powershell
ReDoc: http://127.0.0.1:8000/redoc
```

---

Você pode testar **todos** os `endpoints` diretamente pelo navegador.

###

- Configurações avançadas;
- Middlewares.

###

✅ Você pode adicionar **middlewares** para interceptar requisições e respostas:

###
```python
@app.middleware("http")
async def log_request(request, call_next):
    print(f"Requisição para {request.url.path}")
    response = await call_next(request)
    return response
```

###

**<h2>Segurança e autenticação</h2>**

###

- API oferece suporte integrado para `OAuth2`, `JWT`, `API Keys` e outras estratégias;
- Sempre defina modelos para dados de entrada e saída;
- Use validação automática para evitar erros comuns;
- Documente cada rota com comentários para facilitar manutenção;
- Utilize as ferramentas de documentação para testar sua `API` frequentemente;
- Mantenha seu servidor atualizado para aproveitar melhorias de segurança.

---

**</h2>Extras</h2>**

###

✅ `env` está na `.gitignore`, precisa criar toda vez que for usar;

###
```python
grater than = gt ### maior que...
grater or equal = ge ### maior ou igual...
lower than = lt ### menor que...
lower or equal = le ### menor ou igual...
```

###

**<h2>Contribuindo</h2>**

###

Deseja contribuir? Veja o arquivo [CONTRIBUTING.md](github.com/Kauan19-hub/CONTRIBUTING.md.git) no repositório para guias e código de conduta.

###

**<h2>Licença</h2>**

###

✅️ O projeto está licenciada sob a licença MIT. Você pode usar, modificar e distribuir livremente, desde que mantenha os créditos aos autores originais.

É possível desenvolver um pouco de front-end usando o pacote Angular, Bootstrap e tailwind css, e conectá-lo ao Back-End.

---

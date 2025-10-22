**<h2>Official Documentation</h2>**

###

API is a  **library**/**framework** light and intuitive to build **APIs** **RESTful** quickly and efficiently in **Python**. Inspired by good practices
modern, **API** facilitates the automatic creation, validation and documentation of your application's routes. 

###

**<h2>Starting</h2>**

To start using **API**, you just need the `Python 3.8+` and install with `pip`:

###
```python
pip install api
```

###

✅ If you want to test the API locally, we recommend using the fast ASGI server:

###
```python
pip install uvicorn
```

###

Let's create a **API** simple that responds **"API With FastAPI"**.

###
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API With FastAPI"}
```

###

✅ To run, save the above code in `main.py`:

###
```powershell
uvicorn main:app --reload
```

###

`--reload` restarts the server automatically when there are code changes, great for  **development**.

---

Open the **navigation** and access:

###
```powershell
http://127.0.0.1:8000/
```

###

✅ : `{"message": "API With Python"}`

###

**<h2>Official Documentation</h2>**

###

API is a light and intuitive **library**/**framework** to build **APIs** **RESTful** quickly and efficiently in **Python**. Inspired by good practices
modern, **API** facilitates the automatic creation, validation and documentation of your application's routes. 

###

**<h2>Starting</h2>**

###

To start using **API**, you just need the `Python 3.8+` and install with `pip`:

###
```python
pip install api
```

###

✅ If you want to test the API locally, we recommend using the fast ASGI server:

###
```python
pip install uvicorn
```

###

Let's create a simple **API** that responds **"API With FastAPI"**.

###
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API With FastAPI"}
```

###

✅ To run, save the above code in `main.py`:

###
```powershell
uvicorn main:app --reload
```

###

`--reload` restarts the server automatically when there are code changes, great for **development**.

---

Open the navigation and access:

###
```Powershell
http://127.0.0.1:8000/
```

###

✅ The output: `{"message": "API With Python"}`

###

**<h2>API Structure</h2>**

###

**Routes**

###

Routes define the endpoints of your API. Each route is associated with an HTTP method:

###
```python
@app.get("/path") ### responds to GET requests
```

###
```python
@app.post("/path") ### responds to POST
```

###
```python
@app.put("/path") ### responds to PUT
```

###
```python
@app.delete("/path") ### responds to DELETE
```

###

**<h2>Parameters</h2>**

###

✅ You can define parameters in the URL:

###
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
return {"item_id": item_id}
```

###

Here, `item_id` is an integer parameter extracted from the URL.

---

**<h2>Request Body</h2>**

###

To receive data via JSON, define typed parameters and the API automatically validates it:

###
```python
from pydantic import BaseModel

class Item(BaseModel):
name: str
price: float

@app.post("/items/")
def create_item(item: Item):
return item
```

###

**<h2>Usage Examples</h2>**

###

✅ Automatic validation with Pydantic. The API integrates with Pydantic to validate input and output data.

###
```python
from pydantic import BaseModel

class User(BaseModel):
name: str
email: str

@app.post("/users/")
def create_user(user: User):
return {"message": f"User {user.name} created successfully!"}
```

###

> If the sent JSON doesn't match the model, the API responds with a 422 error and a clear message.

---

**<h2>Automatic Documentation<h2>**

###

✅ Your **API** will already have **interactive** documentation accessible via:

###
```Powershell
Swagger UI: http://127.0.0.1:8000/docs
```

###
```Powershell
ReDoc: http://127.0.0.1:8000/redoc
```

---

You can test **all** endpoints directly through the browser.

###

- Advanced Settings;
- Middlewares.

###

✅ You can add **middleware** to intercept requests and responses:

###
```python
@app.middleware("http")
async def log_request(request, call_next):
print(f"Request for {request.url.path}")
response = await call_next(request)
return response
```

###

**<h2>Security and Authentication</h2>**

###

- API offers built-in support for OAuth2, JWT, API Keys, and other strategies;
- Always define models for input and output data;
- Use automatic validation to avoid common errors;
- Document each route with comments for easier maintenance;
- Use documentation tools to test your API frequently;
- Keep your server up to date to take advantage of security improvements.

---

**<h2>Extras</h2>**

###

✅ `env` is in `.gitignore`, you need to create it every time you use it.

###
```python
grater than = gt ### greater than...
grater or equal = ge ### greater than or equal...
lower than = lt ### less than...
lower or equal = le ### less than or equal...
```

###

**<h2>Contributing</h2>**

###

Want to contribute? See the [CONTRIBUTING.md](github.com/Kauan19-hub/CONTRIBUTING.md.git) file in the repository for guidelines and code of conduct.

###

**<h2>License</h2>**

###

✅️ The project is licensed under the MIT license. You can use, modify, and distribute it freely, as long as you keep credit to the original authors.

###

You can develop a small front-end using the Angular, Bootstrap, and Tailwind CSS packages, and connect it to the back-end.

---
 
**<h2>API Structure</h2>**

###

**Routes**

###

Routes define the **endpoints** of yours  **API**. Each route is associated with a method `HTTP`:

###
```python
@app.get("/caminho") ### responds to GET
```

###
```python
@app.post("/caminho") ### responds to POST
```

###
```python
@app.put("/caminho") ### responds to PUT
```

###
```python
@app.delete("/caminho") ### responds to DELETE
```

###

**<h2>Parameters</h2>**

###

✅ You can set parameters in the `URL`:

###
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

###

Here, `item_id` is a **int** parameter extracted from `URL`.

---

**<h2>Request body</h2>**

###

To receive data via `JSON`, define  **parameters** with types and **API** automatically validates:

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

**<h2>Examples of use</h2>**

###

✅ Automatic validation with `Pydantic`. **API** integrates the `Pydantic` for validating input and output data.

###
```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str

@app.post("/usuarios/")
def create_user(user: User):
    return {"mensagem": f"User {user.name} created!"}
```

###

> If `JSON` sent does not match the model, the **API** responds with error `422` and a clear message.

---

**<h2>Automatic Documentation<h2>**

###

✅ Your **API** will already have documentation **interativa** accessible via: 

###
```powershell
Swagger UI: http://127.0.0.1:8000/docs
```

###
```powershell
ReDoc: http://127.0.0.1:8000/redoc
```

---

You can test **all** the `endpoints` directly through the **browser**.

###

- Advanced settings;
- `Middlewares`.

###

✅ You can add **middlewares** to intercept requests and responses:

###
```python
@app.middleware("http")
async def log_request(request, call_next):
    print(f"Requisition for {request.url.path}")
    response = await call_next(request)
    return response
```

###

**<h2>Security and Authentication</h2>**

###

- API offers integrated support for `OAuth2`, `JWT`, `API Keys` and other strategies;
- Always define models for input and output data;
- Use automatic validation to avoid common mistakes;
- Document each route with comments for easy maintenance;
- Use documentation tools to test your `API` often;
- Keep your server updated to take advantage of security improvements.

---

**<h2>Extras</h2>**

###

✅ `env` is in `.gitignore`, you need to create it every time you use it.

###
```python
grater than = gt ### greater than...
grater or equal = ge ### greater than or equal to...
lower than = lt ### less than...
lower or equal = le ### less than or equal to...
```

###

**<h2>Contributing</h2>**

###

Do you want to contribute? See the file  [CONTRIBUTING.md](github.com/Kauan19-hub/CONTRIBUTING.md.git) in the repository for guides and code of conduct.

###

**<h2>License</h2>**

###

✅️ The project is licensed under the license  MIT. You may **use**, **modify**, and **distribute freely**, as long as you keep **credit** to the **original authors**. 

###

It is possible to develop some front-end using Angular, Bootstrap and tailwind css package, and connect it to Back-End. 

---

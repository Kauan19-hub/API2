# fastapi dev main.py - rodar o script
# pip install "fastapi[standard]" - instala o FastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from routes.area_routes import router as area_router
from fastapi.middleware.cors import CORSMiddleware
import os


app = FastAPI(
  title='API - Áreas da Programação',
  description='Uma simples API com Back-End e Front-End para para gerenciamento de áreas da tecnologia.',
  version='1.0.0',
  contact={
    'name': 'Kauan Vinícius',
    'email': 'saleskauan308@gmail.com'

  }
)

origins = [
  "http://localhost:5173", # React (Vite)
  "http://localhost:3000", # React (CRA)
  "https://site.com" # Deploy do sistema
]

allow_all = True

app.add_middleware (
  CORSMiddleware,
  allow_origins=["*"] if allow_all else origins, # Requisições em qualquer origem
  allow_credentials=True,
  allow_methods=["*"], # Permite todos os métodos
  allow_headers=["*"] # Permite todos os cabeçalhos
)

os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
  return FileResponse("static/favicon.ico")

app.include_router(area_router)

# app.mount('/static', StaticFiles(directory='static'), name='static')
  
# GET: Mensagem que será exibida no início (http://127.0.0.1:8000/)
@app.get('/', response_class=HTMLResponse)
def root():
  html = """
  <!DOCTYPE html>
  <html lang="pt-BR">
  <head>
    <title>API - Áreas da Programação</title>
    <link rel="icon" href="/static/favicon.ico" type="image/x-icon">
    
    <!-- TAILWINDCSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
  </head>
  
  <body class="font-sans bg-gray-100 flex flex-col items-center p-6">
  <h1 class="text-3xl font-bold text-blue-600 mb-6">API - Áreas da Programação</h1>

  <div class="flex gap-3 mb-6">
    <a href="/docs" target="_blank" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded shadow">
      Ver Documentação
    </a>
    <button onclick="load()" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded shadow">
      Listar Áreas
    </button>
    <button onclick="add()" class="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded shadow">Adicionar Exemplo</button>
  </div>

  <ul id="areas" class="text-gray-800 w-full max-w-md pl-6 space-y-2"></ul>

    <script>
      async function load() {
        const res = await fetch('/area');
        const data = await res.json();
        const ul = document.getElementById('areas');

        ul.innerHTML = '';
        data.forEach(a => {

          const li = document.createElement('li');
          li.classList.add('flex', 'justify-between', 'items-center', 'mb-2');
          
          li.innerHTML = `
            <span>${a.name} - ${a.description}</span>
            <button onclick="removeArea('${a.id}')" class="bg-red-500 hover:bg-red-600 text-white px-2 py-1 rounded ml-2">
              Apagar
            </button>
          `;
          
          ul.appendChild(li);
    
        });
      }

      async function add() {
        const newArea = {
          name: "CI/CD",
          description: "Testes e Deploys",
          hours: 6,
          available: true,
          languages: "Inglês",
          wage: 20100.45,
          market: "Valorizado",
          difficulty: "Pleno"

        };

        await fetch('/area', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json'},
          body: JSON.stringify(newArea)

        });

        load();
        
      }

      async function removeArea(id) {
        const yesDelete = confirm("Deseja apagar essa área?");
        if (!yesDelete) return;

        await fetch(`/area/${id}`, {
          method: 'DELETE'
        });

        load();
      }

      console.log("API funcionando")
    </script>
  </body>
  </html>
  """
  return html
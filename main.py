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
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Áreas da Programação</title>
<link rel="icon" href="/static/fastlogo.webp" type="image/png">
<script src="https://cdn.tailwindcss.com"></script> 
</head>
<body class="font-sans bg-gray-100 flex flex-col items-center min-h-screen p-6 sm:p-10">

<h1 class="text-3xl font-bold text-blue-600 mb-6 text-center">Áreas da Programação</h1>

<!-- Mensagens -->
<div id="msg" class="hidden mb-4 w-full max-w-md text-center px-4 py-2 rounded-lg"></div>

<!-- Spinner -->
<div id="loading" class="hidden mb-4">
  <div class="loader border-t-4 border-blue-500 border-solid rounded-full w-10 h-10 animate-spin mx-auto"></div>
</div>

<!-- Botões -->
<div class="flex flex-col sm:flex-row gap-3 mb-6">
  <a href="/docs" target="_blank" class="bg-green-600 hover:bg-green-700 text-white px-4 py-2 rounded shadow text-center transition">Ver Documentação</a>
  <button onclick="load()" id="btnLoad" class="bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded shadow transition">Listar Áreas</button>
</div>

<!-- Formulário -->
<div class="w-full max-w-md bg-white rounded-lg shadow-md p-4 sm:p-6 mb-6">
  <h2 class="text-lg font-semibold mb-3 text-gray-700">Adicionar / Editar Área</h2>
  <form id="areaForm" class="flex flex-col gap-3">
    <input type="hidden" id="areaId">
    <input type="text" id="name" placeholder="Nome da área" class="border rounded px-3 py-2 w-full" required>
    <input type="text" id="description" placeholder="Descrição" class="border rounded px-3 py-2 w-full" required>
    <button type="submit" id="btnSubmit" class="bg-yellow-500 hover:bg-yellow-600 text-white px-4 py-2 rounded transition w-full">Salvar</button>
  </form>
</div>

<!-- Lista -->
<div class="w-full max-w-2xl bg-white rounded-xl shadow-md p-4 sm:p-6">
  <ul id="areas" class="text-gray-800 space-y-3"></ul>
</div>

<style>
.loader { border-top-width: 4px; border-right-width: 4px; border-bottom-width: 4px; border-left-width: 4px; border-color: #3b82f6 transparent transparent transparent; border-style: solid; border-radius: 50%; width: 2.5rem; height: 2.5rem; animation: spin 1s linear infinite; }
@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
</style>

<script>
const msgBox = document.getElementById('msg');
const loading = document.getElementById('loading');
const btnLoad = document.getElementById('btnLoad');
const btnSubmit = document.getElementById('btnSubmit');

function showMessage(text, type="success") {
  msgBox.textContent = text;
  msgBox.classList.remove("hidden", "bg-green-500", "bg-red-500");
  msgBox.classList.add(type === "success" ? "bg-green-500" : "bg-red-500", "text-white");
  setTimeout(() => msgBox.classList.add("hidden"), 4000);
}

function showLoading(show = true) {
  loading.classList.toggle('hidden', !show);
  btnLoad.disabled = show;
  btnSubmit.disabled = show;
}

// Carrega áreas
async function load() {
  showLoading(true);
  try {
    const res = await fetch('/area');
    if (!res.ok) throw new Error("Erro ao carregar áreas");
    const data = await res.json();

    const ul = document.getElementById('areas');
    ul.innerHTML = '';
    if (data.length === 0) {
      ul.innerHTML = '<p class="text-center text-gray-500">Nenhuma área cadastrada.</p>';
      return;
    }

    data.forEach(a => {
      const li = document.createElement('li');
      li.classList.add('flex','flex-col','sm:flex-row','justify-between','items-start','sm:items-center','bg-gray-50','p-3','rounded-lg','border');
      li.innerHTML = `
        <div>
          <span class="font-semibold text-blue-600">${a.name}</span>
          <p class="text-sm text-gray-600">${a.description}</p>
        </div>
        <div class="flex gap-2 mt-2 sm:mt-0">
          <button onclick="editArea(${a.id}, '${a.name}', '${a.description}')" class="bg-yellow-500 hover:bg-yellow-600 text-white px-3 py-1 rounded text-sm transition">Editar</button>
          <button onclick="removeArea(${a.id})" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-sm transition">Apagar</button>
        </div>
      `;
      ul.appendChild(li);
    });

  } catch(err) {
    showMessage(err.message, "error");
  } finally {
    showLoading(false);
  }
}

// Adicionar / Editar área
document.getElementById('areaForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const id = document.getElementById('areaId').value;
  const name = document.getElementById('name').value.trim();
  const description = document.getElementById('description').value.trim();

  if (!name || !description) { showMessage("Preencha todos os campos!", "error"); return; }

  const payload = { name, description, hours: 8, available:true, languages:"Inglês", wage:10000, market:"Bom", difficulty:"Intermediário" };

  showLoading(true);
  try {
    const url = id ? `/area/${id}` : '/area';
    const method = id ? 'PUT' : 'POST';
    const res = await fetch(url, {
      method,
      headers: {'Content-Type':'application/json'},
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error(id ? "Erro ao atualizar área" : "Erro ao adicionar área");

    document.getElementById('areaForm').reset();
    document.getElementById('areaId').value = '';
    showMessage(id ? "Área atualizada!" : "Área adicionada!");
    load();
  } catch(err) {
    showMessage(err.message, "error");
  } finally {
    showLoading(false);
  }
});

function editArea(id, name, description) {
  document.getElementById('areaId').value = id;
  document.getElementById('name').value = name;
  document.getElementById('description').value = description;
  window.scrollTo({top:0, behavior:'smooth'});
}

async function removeArea(id) {
  if (!confirm("Deseja apagar essa área?")) return;

  showLoading(true);
  try {
    const res = await fetch(`/area/${id}`, { method:'DELETE' });
    if (!res.ok) throw new Error("Erro ao apagar área");
    showMessage("Área removida!");
    load();
  } catch(err) {
    showMessage(err.message, "error");
  } finally {
    showLoading(false);
  }
}

load();
</script>
</body>
</html>
    """
  return html
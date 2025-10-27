# fastapi dev main.py - rodar o script
from fastapi import FastAPI
from typing import Optional
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()
# app.mount('/static', StaticFiles(directory='static'), name='static')

# Uma área foi definida. Nessa API, é possível criar, puxar, atualizar e deletar uma área. Essa é
# um exemplo:
AREA = [
  {
    'id': 1,
    'name': 'Full-Stack',
    'description': 'Be the legend of technology',
    'hours': 7,
    'available': True,
    'languages': 'Portuguese and English',
    'wage': 15250.00,
    'market': 'high demand',
    'difficulty': 'advanced/sênior',
  }
]

# Características da área escolhida foram tipadas
class Area(BaseModel):
  name: str
  description: Optional[str] = None
  hours: float
  available: Optional[bool] = True
  languages: str
  wage: float
  market: str
  difficulty: str
  
# GET: Mensagem que será exibida no início (http://127.0.0.1:8000/)
@app.get('/', response_class=HTMLResponse)
def root():
  html = """
  <!DOCTYPE html>
  <html lang="pt-BR">
  <head>
    <title>API - Áreas da Programação</title>
    
    <!-- TAILWINDCSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
  </head>
  
  <body class="font-arial bg-gray-100 flex flex-col items-center p-3 justify-center mt-10">
    <h2 class="text-2xl font-bold mb-4 text-black">Bem-Vindo(a)!</h2>
    <button onclick="load()" class="bg-blue-500 text-white px-10 py-3 rounded hover:bg-blue-600 mb-4 hover:shadow-lg">Ver áreas disponíveis</button>
    <ul id="areas" class="list-inside text-gray-700"></ul>
  
    <script>
      async function load() {
        const res = await fetch('/area');
        const data = await res.json();
        const ul = document.getElementById('areas');
        ul.innerHTML = '';
        data.forEach(a => {
          const li = document.createElement('li');
          li.textContent = a.name + ' - ' + a.description;
          ul.appendChild(li);
    
        });
    
      }
    </script>
  </body>
  </html>
  """
  
  return html
  
# GET: Retorna todas as áreas;
@app.get('/area', tags=['area'])
def list_area() -> list:
  return AREA

# GET: Retorna áreas disponíveis, percorre a lista AREA e seleciona só aqueles que possuem
# o campo 'available' = TRUE
@app.get('/area/available', tags=['area'])
def lis_available_area() -> list:
  available_area = []
  for tech in AREA:
    if tech['available']:
      available_area.append(tech)
  return available_area

# GET: Retorna dados específicos pelo seu ID, caso esse ID ainda não exista, ele retorna 
# uma string vazia
@app.get('/area/{area_id}', tags=['area'])
def obtain_techno(area_id: int) -> dict:
  for technology in AREA:
    if technology['id'] == area_id:
      return technology
  return{}

# POST: Uma nova área poderá ser adicionada à lista
@app.post('/area', tags=['area'])
def add_techno(new_tech: Area) -> dict:
  new_tech = new_tech.dict()
  new_tech['id'] = len(AREA) + 1
  AREA.append(new_tech)
  return new_tech

# PUT: A área poderá ser atualizada através de seu ID
@app.put('/area/{area_id}', tags=['area'])
def up_techno(area_id: int, area: Area) -> dict:
  for idx, tec in enumerate(AREA):
    if tec['id'] == area_id:
      AREA[idx] = area.dict()
      AREA[idx]['id'] = area_id
      return AREA[idx]
  return{}

# DELETE: A área poderá ser deletada pelo seu ID, aqui pode deletar uma área que foi 
# adicionada
@app.delete('/area/{area_id}', tags=['area'])
def delete_techno(area_id: int) -> dict:
  for idx, tec in enumerate(AREA):
    if tec['id'] == area_id:
      AREA.pop(idx)
      return {'message': "This technology has been succesfully removed."}
  return{}

# grater than = gt / maior que...
# grater or equal = ge / maior ou igual...
# lower than = lt / menor que...
# lower or equal = le / menor ou igual...

# POST: send data;
# PUT: update data;
# DELETE: delette data.
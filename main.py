# fastapi dev main .py
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

cursos = [
  "Soluções Digitais",
  "Mecatrônica",
  "Manufatura Digital",
  "Manufatura Eletrônica",
  "Manufatura Automativa",
  "Administração"
  
]

disciplinas 

# GET: take data;
@app.get('/cursos')
def root():
  return {"cursos": cursos}

@app.get('/cursos/{curso_id}')
async def read_curso(curso_id: Annotated[int, Path("O ID de um determinado curso da ETS", ge=0, lt=6)]):
  # curso_id = int(curso_id)
  
  # grater than = gt / maior que...
  # grater or equal = ge / maior ou igual...
  # lower than = lt / menor que...
  # lower or equal = le / menor ou igual...
  return {"curso": cursos[curso_id]}

# POST: send data;
# PUT: update data;
# DELETE: delette data.
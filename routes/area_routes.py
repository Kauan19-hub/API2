from fastapi import APIRouter, HTTPException
from data.mock_data import AREA
from models.area_model import Area

router = APIRouter(prefix="/area", tags=["Área"])

# GET: Retorna todas as áreas;
@router.get('/')
def list_area() -> list:
  return AREA

# GET: Retorna áreas disponíveis, percorre a lista AREA e seleciona só aqueles que possuem
# o campo 'available' = TRUE
@router.get('/available')
def lis_available_area() -> list:
  available_area = []
  for tech in AREA:
    if tech['available']:
      available_area.append(tech)
  return available_area

# GET: Retorna dados específicos pelo seu ID, caso esse ID ainda não exista, ele retorna 
# uma string vazia
@router.get('/{area_id}')
def obtain_techno(area_id: int) -> dict:
  for technology in AREA:
    if technology['id'] == area_id:
      return technology
  return{}

# POST: Uma nova área poderá ser adicionada à lista
@router.post('/')
def add_techno(new_tech: Area) -> dict:
  new_tech = new_tech.dict()
  new_tech['id'] = len(AREA) + 1
  AREA.append(new_tech)
  return new_tech

# PUT: A área poderá ser atualizada através de seu ID
@router.put('/{area_id}')
def up_techno(area_id: int, area: Area) -> dict:
  for idx, tec in enumerate(AREA):
    if tec['id'] == area_id:
      AREA[idx] = area.dict()
      AREA[idx]['id'] = area_id
      return AREA[idx]
  return{}

# DELETE: A área poderá ser deletada pelo seu ID, aqui pode deletar uma área que foi 
# adicionada
@router.delete('/{area_id}')
def delete_area(area_id: int):
  global AREA
  for i, area in enumerate(AREA):
    if area["id"] == area_id:
      AREA.pop(i)
      return {'message': "Área removida com sucesso"}
    
  raise HTTPException(status_code=404, detail="Área não identificada")

# grater than = gt / maior que...
# grater or equal = ge / maior ou igual...
# lower than = lt / menor que...
# lower or equal = le / menor ou igual...

# POST: send data;
# PUT: update data;
# DELETE: delette data.
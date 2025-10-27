from pydantic import BaseModel, Field

# Características da área escolhida foram tipadas
class Area(BaseModel):
  name: str = Field(...,min_length=3,max_length=50)
  description: str | None = Field(None,max_length=200)
  hours: float = Field(...,gt=0, le=24)
  available: bool = Field(default=True)
  languages: str = Field(...,min_length=2)
  wage: float = Field(...,gt=1000)
  market: str
  difficulty: str
from pydantic import BaseModel, HttpUrl
from typing import Optional

# Schema para criar uma organização
class OrganizationCreate(BaseModel):
    name: str
    image: str = None

# Schema para atualizar uma organização
class OrganizationUpdate(BaseModel):
    name: Optional[str] = None
    image: str = None

# Schema para exibir uma organização
class OrganizationOut(BaseModel):
    id: int
    name: str
    image: str = None

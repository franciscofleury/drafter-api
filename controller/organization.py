from database import supabase
from schemas.organization import OrganizationCreate, OrganizationUpdate

# Criar uma nova organização
def create_organization(org_data: OrganizationCreate):
    response = supabase.table('Organization').insert({
        "name": org_data.name,
        "image": org_data.image
    }).execute()
    return response.data

# Buscar todas as organizações
def get_organizations():
    response = supabase.table('Organization').select('*').execute()
    return response.data

# Buscar uma organização por ID
def get_organization_by_id(org_id: int):
    response = supabase.table('Organization').select('*').eq('id', org_id).execute()
    return response.data

# Atualizar uma organização
def update_organization(org_id: int, org_data: OrganizationUpdate):
    update_data = org_data.dict(exclude_unset=True)
    response = supabase.table('Organization').update(update_data).eq('id', org_id).execute()
    return response.data

# Deletar uma organização
def delete_organization(org_id: int):
    response = supabase.table('Organization').delete().eq('id', org_id).execute()
    return response.data
from fastapi import APIRouter, HTTPException
from schemas.organization import OrganizationCreate, OrganizationUpdate, OrganizationOut
from controller.organization import (
    create_organization,
    get_organizations,
    get_organization_by_id,
    update_organization,
    delete_organization,
)

organization_router = APIRouter(
    prefix = "/organization",
    tags = ["organization"],
)

@organization_router.post("/organizations/", response_model=OrganizationOut)
def create_org(org: OrganizationCreate):
    result = create_organization(org)
    if not result:
        raise HTTPException(status_code=400, detail="Failed to create organization")
    return result[0]

@organization_router.get("/organizations/", response_model=list[OrganizationOut])
def list_organizations():
    return get_organizations()

@organization_router.get("/organizations/{org_id}", response_model=OrganizationOut)
def read_organization(org_id: int):
    result = get_organization_by_id(org_id)
    if not result:
        raise HTTPException(status_code=404, detail="Organization not found")
    return result[0]

@organization_router.put("/organizations/{org_id}", response_model=OrganizationOut)
def update_org(org_id: int, org: OrganizationUpdate):
    result = update_organization(org_id, org)
    if not result:
        raise HTTPException(status_code=404, detail="Organization not found")
    return result[0]

@organization_router.delete("/organizations/{org_id}")
def delete_org(org_id: int):
    result = delete_organization(org_id)
    if not result:
        raise HTTPException(status_code=404, detail="Organization not found")
    return {"message": "Organization deleted successfully"}

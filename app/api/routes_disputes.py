from fastapi import APIRouter, UploadFile, File, HTTPException
router = APIRouter()

@router.get("/disputes")
async def list_disputes(merchant_id: str):
    return {"disputes": []}

@router.post("/disputes/{dispute_id}/evidence")
async def upload_evidence(dispute_id: str, file: UploadFile = File(...)):
    from app.disputes.evidence import validate_and_store
    return await validate_and_store(dispute_id, file)

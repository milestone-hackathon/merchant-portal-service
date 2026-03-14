from fastapi import APIRouter
router = APIRouter()

@router.get("/settlements")
async def list_settlements(merchant_id: str, page: int = 1):
    from app.settlements.reconciliation import get_settlement_summary
    return await get_settlement_summary(merchant_id, page)

@router.get("/settlements/{settlement_id}")
async def get_settlement(settlement_id: str):
    return {"id": settlement_id, "status": "completed"}

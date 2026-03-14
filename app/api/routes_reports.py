from fastapi import APIRouter
from fastapi.responses import StreamingResponse
router = APIRouter()

@router.get("/reports/transactions")
async def transaction_report(merchant_id: str, start_date: str, end_date: str):
    from app.reports.exporter import export_transactions_csv
    return await export_transactions_csv(merchant_id, start_date, end_date)

@router.get("/reports/dashboard")
async def dashboard_metrics(merchant_id: str):
    from app.reports.metrics import calculate_dashboard_metrics
    return await calculate_dashboard_metrics(merchant_id)

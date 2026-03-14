from fastapi import FastAPI

app = FastAPI(title="Merchant Portal Service", version="1.0.0")

from app.api import routes_settlements, routes_disputes, routes_reports, routes_accounts
app.include_router(routes_settlements.router, prefix="/api")
app.include_router(routes_disputes.router, prefix="/api")
app.include_router(routes_reports.router, prefix="/api")
app.include_router(routes_accounts.router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "ok"}

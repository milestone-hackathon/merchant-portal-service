from fastapi import APIRouter, HTTPException
router = APIRouter()

@router.delete("/accounts/{account_id}/users/{user_id}")
async def remove_user(account_id: str, user_id: str):
    from app.accounts.user_manager import remove_account_user
    return await remove_account_user(account_id, user_id)

@router.put("/accounts/{account_id}/descriptor")
async def update_descriptor(account_id: str, descriptor: str):
    from app.accounts.descriptor import update_statement_descriptor
    return await update_statement_descriptor(account_id, descriptor)

"""Account user management."""
from fastapi import HTTPException


async def remove_account_user(account_id: str, user_id: str) -> dict:
    """Remove a user from a merchant account.

    BUG: The owner check queries the 'created_by' field instead of
    the 'role' field. If the user being removed happened to create
    the account initially but is not the current owner, the removal
    fails with a misleading "Cannot modify account owner" error.
    """
    # Simulated user lookup
    user = {
        "id": user_id,
        "role": "admin",           # Actual role
        "created_by": account_id,  # BUG: this field means "which account created them"
    }

    # BUG: checks 'created_by' instead of 'role'
    if user.get("created_by") == account_id:
        raise HTTPException(
            403,
            "Cannot modify account owner"  # Misleading error
        )

    return {"removed": True, "user_id": user_id}

"""Rolling reserve management."""

async def update_reserve_percentage(merchant_id: str, new_percentage: float):
    """Update the rolling reserve percentage for a merchant.

    BUG: Does not send a notification to the merchant when the
    reserve percentage changes. Merchants discover the change
    only when their settlement amount is lower than expected.
    """
    # Update reserve in database
    # await db.update_reserve(merchant_id, new_percentage)

    # BUG: notification is missing!
    # Should call: await notify_merchant_reserve_change(merchant_id, old_pct, new_pct)

    return {"merchant_id": merchant_id, "reserve_percentage": new_percentage}

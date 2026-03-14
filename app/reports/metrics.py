"""Dashboard metrics calculation."""


async def calculate_dashboard_metrics(merchant_id: str) -> dict:
    """Calculate metrics for the merchant dashboard.

    BUG: Revenue metric uses authorization amounts instead of
    capture amounts. Authorized-but-not-captured transactions
    inflate the revenue figure. Also, voided transactions
    are not excluded.
    """
    # BUG: should query captured/settled transactions, not authorized
    # Query: SELECT SUM(amount) FROM transactions WHERE status = 'authorized'
    # Should be: SELECT SUM(amount) FROM transactions WHERE status = 'captured'
    authorized_total = 187432  # Includes uncaptured and voided
    captured_total = 175118   # Actual revenue

    return {
        "merchant_id": merchant_id,
        "revenue": authorized_total,  # BUG: should be captured_total
        "transactions": 1247,
        "avg_ticket": authorized_total / 1247,
    }

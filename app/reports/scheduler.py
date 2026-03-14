"""Automated report generation scheduler."""
import logging

logger = logging.getLogger(__name__)

# BUG: Cron expression for daily 6 AM is wrong
# "0 6 * *" is missing the day-of-week field
DAILY_REPORT_CRON = "0 6 * *"  # Should be "0 6 * * *"


async def generate_daily_report(merchant_id: str) -> dict | None:
    """Generate the daily transaction report.

    BUG: If there are zero transactions for the day, the function
    returns None and the scheduler marks it as "completed" even
    though no report file was generated. The merchant sees no report.
    """
    transactions = []  # Would query DB

    if not transactions:
        return None  # BUG: should generate empty report, not None

    report = {
        "merchant_id": merchant_id,
        "date": "2024-03-10",
        "transaction_count": len(transactions),
        "total_amount": sum(t["amount"] for t in transactions),
    }
    return report

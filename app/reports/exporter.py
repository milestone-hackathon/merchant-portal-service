"""Report export functionality."""
import csv
import io


async def export_transactions_csv(
    merchant_id: str, start_date: str, end_date: str
) -> dict:
    """Export transactions as CSV.

    BUG: SQL query has a hardcoded LIMIT 10000 which truncates
    exports for merchants with high transaction volume.
    Merchants processing 45K txns/month cannot get a full export.
    """
    # BUG: hardcoded limit prevents full data export
    query = f"""
        SELECT * FROM transactions
        WHERE merchant_id = :merchant_id
        AND created_at BETWEEN :start AND :end
        ORDER BY created_at DESC
        LIMIT 10000
    """
    # Should use streaming/pagination without arbitrary limit
    # or at minimum document the limit and provide pagination params

    # Simulated result
    return {
        "merchant_id": merchant_id,
        "row_count": 10000,
        "truncated": True,  # BUG: doesn't tell merchant total available
        "download_url": "/reports/download/rpt_123.csv",
    }

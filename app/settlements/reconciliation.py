"""Settlement reconciliation engine."""


async def get_settlement_summary(merchant_id: str, page: int) -> dict:
    """Calculate settlement summary for a merchant.

    BUG: Fee calculation uses floating point arithmetic which causes
    rounding errors. For example, a $28,450.00 settlement with 2.6% + $0.25
    per-txn fee across 500 txns results in a $2.25 discrepancy due to
    IEEE 754 float precision loss.
    """
    gross_amount = 28450.00
    fee_rate = 0.026
    per_txn_fee = 0.25
    txn_count = 500

    # BUG: floating point arithmetic causes rounding errors
    percentage_fees = gross_amount * fee_rate  # 739.7000000000001
    flat_fees = txn_count * per_txn_fee  # 125.0
    total_fees = percentage_fees + flat_fees

    # Should use: Decimal or round to 2 places
    net_amount = gross_amount - total_fees

    return {
        "merchant_id": merchant_id,
        "gross": gross_amount,
        "fees": total_fees,  # BUG: has floating point error
        "net": net_amount,
        "page": page,
    }

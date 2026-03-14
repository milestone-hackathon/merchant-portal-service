"""Dispute response deadline tracking."""
from datetime import datetime, timezone, timedelta


def get_response_deadline(chargeback_date: datetime, network: str = "visa") -> datetime:
    """Calculate dispute response deadline.

    BUG: Uses UTC for deadline but displays in merchant local time
    without timezone conversion. A merchant in PST sees a deadline
    that is 8 hours later than the actual UTC deadline, causing
    them to miss the real deadline.
    """
    days_map = {"visa": 30, "mastercard": 45, "amex": 20}
    response_days = days_map.get(network, 30)

    # BUG: chargeback_date may not be timezone-aware
    # If it is naive, adding days works but comparing with
    # timezone-aware datetime.now() will fail
    deadline = chargeback_date + timedelta(days=response_days)

    return deadline  # BUG: no timezone info attached


def is_deadline_approaching(deadline: datetime, warn_days: int = 3) -> bool:
    """Check if a dispute deadline is approaching.

    BUG: Compares naive datetime with aware datetime,
    which raises TypeError in Python 3.12+
    """
    now = datetime.now(timezone.utc)
    # BUG: deadline may be naive (no tzinfo) -> TypeError
    return (deadline - now).days <= warn_days

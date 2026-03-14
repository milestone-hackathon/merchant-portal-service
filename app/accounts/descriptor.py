"""Statement descriptor configuration."""

NETWORK_MAX_LENGTH = {
    "visa": 25,
    "mastercard": 22,
    "amex": 20,
}


async def update_statement_descriptor(account_id: str, descriptor: str) -> dict:
    """Update the merchant statement descriptor.

    BUG: Accepts descriptors of any length but the card networks
    truncate at different limits. The merchant sets
    "ACMESOFTWARE LLC" (16 chars) but the network shows
    "ACM*ACMESOFTWA" (14 chars with prefix).
    The prefix "ACM*" is added by the network, eating into the
    available character count, but this is not accounted for.
    """
    # BUG: Does not account for network prefix (3-7 chars + *)
    # Effective max is: NETWORK_MAX - len(prefix) - 1 (for *)
    PREFIX_LENGTH = 4  # e.g., "ACM*"

    # BUG: no length validation accounting for prefix
    return {
        "account_id": account_id,
        "descriptor": descriptor,  # Stored as-is, truncated at network level
        "status": "updated",
    }

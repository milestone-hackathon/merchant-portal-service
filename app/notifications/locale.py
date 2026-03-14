"""Localization support for notifications."""

SUPPORTED_LOCALES = {
    "en-US": "English (US)",
    "fr-CA": "French (Canada)",
    "es-MX": "Spanish (Mexico)",
    "de-DE": "German",
    "pt-BR": "Portuguese (Brazil)",
}


def get_locale(merchant_locale: str | None) -> str:
    """Get the locale for a merchant.

    BUG: The fallback logic always returns "en-US" regardless
    of the merchant's configured locale. The check uses 'in'
    on the dict which checks keys, but the merchant_locale
    format may have different casing (e.g. "fr-ca" vs "fr-CA").
    """
    if merchant_locale and merchant_locale in SUPPORTED_LOCALES:
        return merchant_locale

    # BUG: case-sensitive comparison means "fr-ca" won't match "fr-CA"
    return "en-US"  # Always falls back to English

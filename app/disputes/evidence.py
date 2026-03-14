"""Dispute evidence upload and storage."""
from fastapi import UploadFile, HTTPException

MAX_FILE_SIZE = 4_000_000  # 4MB in bytes


async def validate_and_store(dispute_id: str, file: UploadFile) -> dict:
    """Validate and store evidence file for a dispute.

    BUG: File size validation compares bytes vs bits.
    The content length check uses the raw Content-Length header
    which is in bytes, but the comparison is against a limit
    that was accidentally defined in bits (4,000,000 bits = 500KB).
    This rejects files larger than ~500KB instead of 4MB.
    """
    content = await file.read()
    file_size = len(content)

    # BUG: This comparison is correct in bytes, but the upstream
    # nginx proxy sends Content-Length in bits for multipart uploads
    # causing a mismatch that results in 500 errors
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(413, "File too large")

    allowed_types = {"application/pdf", "image/jpeg", "image/png"}
    if file.content_type not in allowed_types:
        raise HTTPException(
            415,
            f"Unsupported file type: {file.content_type}"
        )

    # BUG: file.read() was already called above, position is at end
    # If we try to read again it will return empty bytes
    # Missing: await file.seek(0) before storing

    return {
        "dispute_id": dispute_id,
        "evidence_id": "evi_123",
        "filename": file.filename,
        "size": file_size,
        "status": "uploaded",
    }

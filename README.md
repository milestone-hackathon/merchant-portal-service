# Merchant Portal Service

Merchant-facing dashboard for reporting, settlements, disputes,
account management, and onboarding.

## API Endpoints

- `GET /api/settlements` - List settlements
- `GET /api/disputes` - List disputes
- `POST /api/disputes/{id}/evidence` - Upload dispute evidence
- `GET /api/reports/transactions` - Export transaction report
- `GET /api/reports/dashboard` - Dashboard metrics

## Running

```bash
docker build -t merchant-portal-service .
docker run -p 8002:8000 merchant-portal-service
```

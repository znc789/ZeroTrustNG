# API Documentation

## Authentication

### POST /api/v1/auth/login

Request body:

```json
{
  "username": "nadia.voss",
  "password": "Secure!Pass"
}
```

Response:

```json
{
  "access_token": "demo-token",
  "token_type": "bearer",
  "user": {
    "id": "u-1001",
    "name": "Nadia Voss",
    "role": "SOC Analyst",
    "risk_score": 18
  }
}
```

### GET /api/v1/auth/me

Returns identity and trust metadata.

## Health

### GET /api/v1/health

Returns service health and readiness metadata.

## Dashboard

### GET /api/v1/dashboard/overview

Returns SOC summary widgets and alert data.

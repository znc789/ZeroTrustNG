# Zero Trust Network Guardian with AI

AI-powered Adaptive Zero Trust Security Framework for Modern Networks.

## Overview

This project is a production-ready MVP for a cybersecurity platform focused on zero trust, adaptive security, AI-driven risk analysis, and automated response. It combines a FastAPI backend, a Next.js dashboard, AI analytics modules, and security engineering concepts for real-world demonstration.

## Mission

> Never Trust. Always Verify.

## Architecture

- Frontend: Next.js + Tailwind + TypeScript
- Backend: FastAPI + PostgreSQL + MongoDB + Redis
- AI: Scikit-learn and heuristic models for risk/behavior analytics
- Network monitoring: Scapy, PyShark, Zeek-ready modules
- Security: JWT, OAuth2-ready patterns, JWT auth, blast radius mitigation

## Folder Structure

```text
ZeroTrustNG/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── db/
│   │   ├── models/
│   │   ├── services/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/
│   ├── .env.example
│   └── requirements.txt
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── package.json
│   ├── next.config.mjs
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   └── tsconfig.json
├── ai/
├── data/
├── docs/
├── .github/workflows/
├── .gitignore
├── LICENSE
├── README.md
└── docker-compose.yml
```

## Quickstart

### Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### API

Open the API docs at `http://localhost:8000/docs`.

## Key Features

- AI-based user behavior analytics
- Device trust scoring
- Adaptive authentication and session monitoring
- Threat detection hooks
- Risk scoring engine
- Dashboard with SOC-style metrics
- Demo incident automation logic

## Sample Data

Example attack simulations and telemetry samples are available under `data/` and `docs/`.

## Production Considerations

- Enable TLS and certificate management
- Add database migrations and storage policies
- Use KMS/secret manager for keys and tokens
- Move analytics logic to background workers
- Add RBAC/ABAC enforcement at the API layer
- Run monitoring and tracing with OpenTelemetry

## License

MIT

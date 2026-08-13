#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BACKEND_DIR="$ROOT/backend"
FRONTEND_DIR="$ROOT/frontend"

if [ ! -d "$BACKEND_DIR/.venv" ]; then
  python3 -m venv "$BACKEND_DIR/.venv"
fi

"$BACKEND_DIR/.venv/bin/pip" install -r "$BACKEND_DIR/requirements.txt" >/dev/null
"$BACKEND_DIR/.venv/bin/python" -m compileall "$BACKEND_DIR/app" >/dev/null

cd "$FRONTEND_DIR"
npm install >/dev/null
npm run build >/dev/null

pkill -f "uvicorn app.main:app --host 0.0.0.0 --port 8000" || true
pkill -f "next start --hostname 0.0.0.0 --port 3000" || true

nohup bash -lc "cd '$BACKEND_DIR' && '$BACKEND_DIR/.venv/bin/python' -m uvicorn app.main:app --host 0.0.0.0 --port 8000" > /tmp/zerotrustng_backend.log 2>&1 &
nohup bash -lc "cd '$FRONTEND_DIR' && npm run start -- --hostname 0.0.0.0 --port 3000" > /tmp/zerotrustng_frontend.log 2>&1 &

echo "ZeroTrustNG started successfully"
echo "Backend: http://localhost:8000"
echo "Frontend: http://localhost:3000"

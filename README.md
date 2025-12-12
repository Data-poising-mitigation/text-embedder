# text-embedder
Service that holds text embedder(s) to be used in the RAG pipeline

set PYTHONPATH=%cd%\src

python -m uvicorn app.main:app --app-dir src --host 0.0.0.0 --port 8000 --reload
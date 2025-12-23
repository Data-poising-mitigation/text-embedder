from fastapi.testclient import TestClient
from unittest.mock import MagicMock
import pytest

from app.main import create_app
from app.models import factory as embed_factory


@pytest.fixture
def client(monkeypatch):
    app = create_app()

    # Stub embedder
    stub = MagicMock()
    stub.dim = 384
    stub.embed.return_value = [[0.0] * 384]  # one vector

    # Patch the factory to avoid loading sentence-transformers
    monkeypatch.setattr(embed_factory, "get_embedder", lambda model_name: stub)

    return TestClient(app)


def test_embed_happy_path(client):
    r = client.post("/embed", json={"model": "all-minilm-l6-v2", "texts": ["hello"]})
    assert r.status_code == 200
    body = r.json()
    assert body["model"] == "all-minilm-l6-v2"
    assert body["dim"] == 384
    assert len(body["embeddings"]) == 1
    assert len(body["embeddings"][0]) == 384


def test_embed_unknown_model_returns_400(monkeypatch):
    app = create_app()
    client = TestClient(app)

    def raise_unknown(_):
        raise ValueError("Unknown embedding model")

    monkeypatch.setattr(embed_factory, "get_embedder", raise_unknown)

    r = client.post("/embed", json={"model": "nope", "texts": ["hello"]})
    assert r.status_code == 400


def test_embed_limit_exceeded_returns_413(monkeypatch):
    # This assumes your service raises LimitExceededError on too many texts.
    from app.services.embed_service import LimitExceededError

    app = create_app()
    client = TestClient(app)

    stub = MagicMock()
    stub.dim = 384
    stub.embed.return_value = [[0.0] * 384]

    monkeypatch.setattr(embed_factory, "get_embedder", lambda model_name: stub)

    # Make texts exceed your hardcoded MAX_TEXTS_PER_REQUEST (adjust if different)
    too_many = ["x"] * 1000
    r = client.post("/embed", json={"model": "all-minilm-l6-v2", "texts": too_many})
    assert r.status_code == 413

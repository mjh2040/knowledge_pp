import pytest

from landchat.graph import init_graph
from landchat.app.app import app, socketio


@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    ctx = app.test_request_context()
    ctx.push()

    socketio.init_app(app)
    return app


@pytest.fixture
def graph():
    g = init_graph()
    return g
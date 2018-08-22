import wtfrestful
from wtfrestful import pytest

@pytest.fixture
def app():
    from wtfrestful.client.hello import World
    return World.Load()
    
@pytest.fixture
def files_dir():
    from os import path

    return path.join(
        path.dirname(
            path.abspath(__file__)
        ),
        'files'
    )

@pytest.fixture
def tmp_dir():
    return wtfrestful.test_mktmpdir(
        'wtfrestful_client_images'
    )

@pytest.mark.parametrize(
    'name', [
    ('Bob'),
    ('Mary'),
])
def test_hello_world(
    app, name
):
    
    msg = app.hello(
        name
    )

    assert msg == 'Hello {name}!'
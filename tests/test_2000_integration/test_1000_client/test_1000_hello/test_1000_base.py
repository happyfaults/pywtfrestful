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
    'nick_names', [[
    ('b', 'Bob'),
    ('mj', 'Mary Jane'),
    ('kt', 'Knight Rider')
]])
def test_hello_world(
    app, nick_names
):
    
    for nick, name in nick_names:
        app.setName(
            nick, name
        )
        assert app.getName(nick) == name

    stats = app.getStats()

    assert stats['count'] == len(nick_names)
    

    
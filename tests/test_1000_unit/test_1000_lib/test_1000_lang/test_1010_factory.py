from wtfrestful import pytest

def test_1000_factory():

    from wtfrestful.lib.lang.factory import Factory

    config = {
        'root': 1
    }
    f = Factory.Default(config)

    assert f.config is config

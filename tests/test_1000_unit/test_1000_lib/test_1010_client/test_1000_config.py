from wtfrestful import pytest

def test_1000_config_manager():

    from wtfrestful.lib.client.config import Manager
    import wtfrestful_c

    import sys
    from os import path, curdir, environ

    env_bkp = environ.copy()
    sys_path_bkp = list(sys.path)

    environ['PYTHON_CLIENT_CONFIG_DIR'] = path.abspath('fake_pccd')
    environ['PYTHON_ENV_DIR'] = path.abspath('fake_ped')
    environ['HOME'] = path.abspath('home')

    m = Manager.Default(conf_d='test')

    assert path.abspath('test') in sys.path
    assert path.join(curdir, 'config') in sys.path
    assert path.abspath('fake_pccd') in sys.path
    assert path.join(path.abspath('fake_ped'), 'config') in sys.path
    assert path.join(path.abspath('home'), '.pyconfig') in sys.path

    environ.update(env_bkp)
    sys.path.clear()
    sys.path.extend(sys_path_bkp)

    assert m.base_modname == 'wtfrestful_c'

    from wtfrestful.lib.lang.namespace import Type as NSType
    from wtfrestful.lib.client import Context as cls
    
    from datetime import datetime
    now_dt = datetime.utcnow()
    
    NS = NSType(cls.ROOT_NS)

    cfg = {
        cls.ROOT_NS : NS,
        NS.prefix : cls.name,
        NS.now_dt : now_dt,
        NS.working_dir : path.abspath('.'),
        NS.level_code : cls.DEFAULT_LEVEL
    }

    with pytest.raises(ModuleNotFoundError):
        # trying to load wtfrestful_c.lib which doesn't exist
        m.loadConfig(cls, cfg)

    # test later in wtfrestful.client module
    #assert cls.CONFIG_TYPE is wtfrestful_c.Config
    #assert cfg[cls.ROOT_NS] == NS
    #assert cfg.get(NS.logging_dir) is not None
    #assert cfg.get(NS.default_encoding) is not None
    #assert cfg.get(NS.now_str) is not None

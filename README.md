# PyWTFRestful
<img align="right" width=84 height=84 src="https://github.com/happyfaults/site-common/raw/master/images/logo128.png"/>A RESTful microservice for the [PyWatDaFudge](https://github.com/happyfaults/pywatdafudge) project.


## Quick Install
Currently, the library has only been tested with [Python 3.6.6](https://www.python.org/downloads/release/python-366/).

To install everything using [pip](https://pypi.org/project/pip/), issue the following commands from the project root directory:

1. pip install -r requirements.txt
2. pip install -e .
3. pip install -e config/

Leave out the **-e** switch if you want to install the packages into your Python site folder.

You can also use the equivalent Python setup commands:

1. pip install -r requirements.txt
2. python setup.py develop (or install)
3. python config/setup.py develop (or install)

### Features

### Image Utils

From [wtfrestful.client.hello.World](https://github.com/happyfaults/pywtfrestful/blob/master/src/wtfrestful/client/hello/__init__.py)
```python
from wtfrestful.client.hello import World
a = World.Load()
```

### Say Hello

```python
>>> a.hello('Jim')
Hello Jim!
```

## Configuration
All configuration is done using a framework that sets items to a Python dict when the app is loaded. When `App.Load()` is invoked, it will call its [config manager type](https://github.com/happyfaults/pywtfrestful/blob/master/src/wtfrestful/lib/client/config.py) to populate the app's `config` member variable.
```python
>>> from wtfrestful.client.files import App
>>> a = App.Load()
>>> a.config
{'.NS': 'wtfrestful',
 'wtfrestful.prefix': 'files',
 'wtfrestful.now_dt': datetime.datetime(2018, 8, 13, 14, 33, 30, 175158),
 'wtfrestful.working_dir': '/home/hendrix/dev/pywtfrestful',
 'wtfrestful.level_code': 10,
 'wtfrestful.logging_dir': '/home/hendrix/dev/pywtfrestful/logs',
...
}
```
#### Namespaces
For convenience, you can access and update configuration items using a [namespace type](https://github.com/happyfaults/pywtfrestful/blob/master/src/wtfrestful/lib/lang/namespace.py) variable.
```python
>>> NS = a.config['.NS']
>>> NS
'wtfrestful'
>>> RootNS = a.RootNS
>>> assert NS == RootNS
>>> assert NS == 'wtfrestful'
>>> a.config[NS.logging_dir]
'/home/hendrix/dev/pywtfrestful/logs'
>>> NS.logging_dir
'wtfrestful.logging_dir'
>>> a.config['wtfrestful.logging_dir']
'/home/hendrix/dev/pywtfrestful/logs'
```
To access the settings for the regex and whoosh analyzers associated with this app, you can do something like the following:
```python
>>> aNS = NS.analyzers
>>> aNS
'wtfrestful.analyzers'
>>> a.config[aNS.regex]
{}
>>> whoosh_settings = a.config[aNS.whoosh]
>>> whoosh_settings
{'index_dir': 'wtf_index', 'word_ngrams_max': 3, 'slop_factor': 2}
>>> whoosh_settings['index_dir'] = 'new_wtf_index'
```
### Config Modules
From the project directory, you can find the default configuration modules in the subfolder: [config/wtfrestful_c](https://github.com/happyfaults/pywtfrestful/tree/master/config/wtfrestful_c)

So the configuration module for the *interactor app* type: [wtfrestful.client.image.App](https://github.com/happyfaults/pywtfrestful/blob/master/src/wtfrestful/client/image/__init__.py)

Is the corresponding matching *config* type: [wtfrestful_c.client.image.App](https://github.com/happyfaults/pywtfrestful/blob/master/config/wtfrestful_c/client/image/__init__.py)

To update the default values, see file: [config/wtfrestful_c/client/image/\_\_init\_\_.py](https://github.com/happyfaults/pywtfrestful/blob/master/config/wtfrestful_c/client/image/__init__.py)

#### Ensure Config Modules Can Be Imported
If you do not install the **wtfrestful_c** package, the root config path must be included in your **PYTHONPATH** environment variable so that the configuration modules can be imported when `App.Load()` is called.

If running `App.Load()` throws **ModuleNotFoundError** type exceptions, verify that under your environment you can import both these modules without any errors.
```python
>>> import wtfrestful
>>> import wtfrestful_c
>>> 
```

## Logging
When executing the library with an app interactor type, log messages will be outputted to files. The configuration settings for logging can be accessed as follows:
```python
>>> a.config[NS.logging_dir]
'/home/hendrix/dev/pywtfrestful/logs'
>>> a.logger
<Logger wtfrestful.client.files (INFO)>
>>> a.config[NS.logging]
{'version': 1,
 'disable_existing_loggers': False,
 'formatters': {'simple': {'format': '%(asctime)s|%(name)s|%(levelname)s: %(message)s'}},
 'handlers': {'console': {'class': 'logging.StreamHandler',
   'level': 'CRITICAL',
   'formatter': 'simple',
   'stream': 'ext://sys.stdout'},
  'info_file_handler': {'class': 'logging.handlers.RotatingFileHandler',
   'level': 'INFO',
   'formatter': 'simple',
   'filename': '/home/hendrix/dev/pywtfrestful/logs/files-2018_08_13_14_33_30-info.log',
   'maxBytes': 10485760,
   'backupCount': 20,
   'encoding': 'utf8'},
...
}
```
By default, in the log folder there will be two files for critical and non-critical messages respectively.
## TDD & CI

This library is being developed using the agile principles of [test-driven development (TDD)](http://agiledata.org/essays/tdd.html) and [continous integration (CI)](https://www.atlassian.com/continuous-delivery/ci-vs-ci-vs-cd).

Testing is done with [Pytest](https://docs.pytest.org/en/latest/). 

This repository is connected to [Travis-CI](https://travis-ci.org/happyfaults/pywtfrestful).

## Development Roadmap

Features will be added as repetitive daily tasks are encountered. 


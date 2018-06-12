import codecs
import os
import re

from setuptools import setup
from setuptools import find_packages

# Workaround for http://bugs.python.org/issue8876, see
# http://bugs.python.org/issue8876#msg208792
# This can be removed when using Python 2.7.9 or later:
# https://hg.python.org/cpython/raw-file/v2.7.9/Misc/NEWS
if os.path.abspath(__file__).split(os.path.sep)[1] == 'vagrant':
    del os.link


def read_file(filename, encoding='utf8'):
    """Read unicode from given file."""
    with codecs.open(filename, encoding=encoding) as fd:
        return fd.read()


here = os.path.abspath(os.path.dirname(__file__))

# read version number (and other metadata) from package init
init_fn = os.path.join(here, 'certbot', '__init__.py')
meta = dict(re.findall(r"""__([a-z]+)__ = '([^']+)""", read_file(init_fn)))

readme = read_file(os.path.join(here, 'README.rst'))
changes = read_file(os.path.join(here, 'CHANGES.rst'))
version = meta['version']

# This package relies on PyOpenSSL, requests, and six, however, it isn't
# specified here to avoid masking the more specific request requirements in
# acme. See https://github.com/pypa/pip/issues/988 for more info.
install_requires = [
    'acme==0.25.0',
    'asn1crypto==0.24.0',
    'certbot==0.25.0',
    'certifi==2018.4.16',
    'cffi==1.11.5',
    'chardet==3.0.4',
    'ConfigArgParse==0.13.0',
    'configobj==5.0.6',
    'cryptography==2.2.2',
    'enum34==1.1.6',
    'funcsigs==1.0.2',
    'future==0.16.0',
    'idna==2.6',
    'ipaddress==1.0.22',
    'josepy==1.1.0',
    'mock==2.0.0',
    'parsedatetime==2.4',
    'pbr==4.0.4',
    'pycparser==2.18',
    'pyOpenSSL==18.0.0',
    'pyRFC3339==1.1',
    'pytz==2018.4',
    'requests==2.18.4',
    'requests-toolbelt==0.8.0',
    'setuptools==39.2.0',
    'six==1.11.0',
    'urllib3==1.22',
    'wheel==0.31.1',
    'zope.component==4.4.1',
    'zope.event==4.3.0',
    'zope.interface==4.5.0'
]

dev_extras = [
    # Pin astroid==1.3.5, pylint==1.4.2 as a workaround for #289
    'astroid==1.3.5',
    'coverage',
    'ipdb',
    'pytest',
    'pytest-cov',
    'pytest-xdist',
    'pylint==1.4.2',  # upstream #248
    'tox',
    'twine',
    'wheel',
]

dev3_extras = [
    'mypy',
    'typing', # for python3.4
]

docs_extras = [
    'repoze.sphinx.autointerface',
    # autodoc_member_order = 'bysource', autodoc_default_flags, and #4686
    'Sphinx >=1.0,<=1.5.6',
    'sphinx_rtd_theme',
]

setup(
    name='certbot',
    version=version,
    description="ACME client",
    long_description=readme,  # later: + '\n\n' + changes
    url='https://github.com/letsencrypt/letsencrypt',
    author="Certbot Project",
    author_email='client-dev@letsencrypt.org',
    license='Apache License 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Environment :: Console :: Curses',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],

    packages=find_packages(exclude=['docs', 'examples', 'tests', 'venv']),
    include_package_data=True,

    install_requires=install_requires,
    extras_require={
        'dev': dev_extras,
        'dev3': dev3_extras,
        'docs': docs_extras,
    },

    # to test all packages run "python setup.py test -s
    # {acme,certbot_apache,certbot_nginx}"
    test_suite='certbot',

    entry_points={
        'console_scripts': [
            'certbot = certbot.main:main',
        ],
        'certbot.plugins': [
            'manual = certbot.plugins.manual:Authenticator',
            'null = certbot.plugins.null:Installer',
            'standalone = certbot.plugins.standalone:Authenticator',
            'webroot = certbot.plugins.webroot:Authenticator',
        ],
    },
)

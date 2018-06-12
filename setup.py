# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open

from os import path
from redis_ratelimit import __version__

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='redis-ratelimit',
    version=__version__,
    description='A fixed window rate limiter based on Redis',
    long_description=long_description,
    url='https://github.com/romantomjak/redis-ratelimit',
    author='Roman Tomjak',
    author_email='r.tomjaks@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
    keywords='redis rate-limit rate-limiter ratelimit ratelimiter',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['redis'],
    tests_require=['redis', 'coverage'],
    test_suite='tests',
)

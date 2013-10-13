import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="txwatcher",
    version="0.1.2",
    author="Thomas Sileo",
    author_email="thomas.sileo@gmail.com",
    description=".",
    license="MIT",
    keywords="txwatcher bitcoin",
    url="https://github.com/tsileo/txwatcher",
    py_modules=['txwatcher'],
    long_description=read('README.rst'),
    install_requires=['events', 'websocket-client'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
    ],
    test_suite='test_txwatcher',
)

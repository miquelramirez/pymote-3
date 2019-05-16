Distributing to PyPI
====================

http://docs.python.org/2/distutils/index.html#distutils-index
https://python-packaging-user-guide.readthedocs.org/en/latest/current/


Windows
-------

Install required packages::

    > pip install twine wheel

Create ``C:\Users\<user>\.pypirc`` file::

    [distutils]
    index-servers =
        pypi

    [pypi]
    repository: http://pypi.python.org/pypi
    username: <username>
    password: <password>

    [server-login]
    repository: http://pypi.python.org/pypi
    username: <username>
    password: <password>

Issue these commands::

    > setx HOME C:\Users\<user>
    > python setup.py sdist bdist_wheel
    > twine upload dist/*

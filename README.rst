venvgit2
========

`pygit2 <http://www.pygit2.org/>`_ is awesome. pygit2 is hard to install.

Installing this package will try to install matched versions of libgit2 and
pygit2 to your activated virtualenv.


Requirements
------------

- cmake


Installation
------------

::

    $ virtualenv venv
    $ . venv/bin/activate
    (venv) $ pip install venvgit2

You can put it in a ``requirements.txt`` or whatever, as long as you're in a
virtualenv you're set with ``pip`` or ``easy_install``.


Development
-----------

1) Clone this repository 

::

    $ git clone git@github.com:uniphil/venvgit2.git


2) Grab the submodules

::

    $ git submodule update --init

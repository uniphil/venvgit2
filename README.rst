venvgit2
========

`pygit2 <http://www.pygit2.org/>`_ is awesome. pygit2 is hard to install.

Installing this package will try to install matched versions of libgit2 and
pygit2 to your activated virtualenv.


Requirements
------------

- cmake
- python-dev


Installation
------------

::

    $ virtualenv venv
    $ . venv/bin/activate
    (venv)$ pip install venvgit2

You can put it in a ``requirements.txt`` or whatever, as long as you're in a
virtualenv you're set with ``pip`` or ``easy_install``.


Usage
-----

::

    (venv)$ python
    >>> import pygit2

Woo hoo if no errors are raised, it is likely that you are set to go!

``venvgit2`` doesn't give you anything except a convenient install of matched
versions of ``libgit2`` and ``pygit2``. Each project has its own excellent"
documentation:

- `libgit2 docs <http://libgit2.github.com/>`_
- `pygit2 docs <http://www.pygit2.org/>`_


Development
-----------

1) Clone this repository 

::

    $ git clone git@github.com:uniphil/venvgit2.git


2) Grab the submodules

::

    $ git submodule update --init

after the first time, to update submodules it's just

::

    $ git submodule update



What's going on
^^^^^^^^^^^^^^^

Without ``venvgit2``, you might do this:

::

    $ git clone git@github.com:libgit2/libgit2.git
    $ git clone git@github.com:libgit2/pygit2.git
    $ virtualenv venv
    $ . venv/bin/activate
    (venv)$ cd libgit2
    (venv)$ git checkout v0.20.0
    (venv)$ mkdir build && cd build
    (venv)$ cmake .. -DCMAKE_INSTALL_PREFIX=$VIRTUAL_ENV
    (venv)$ cmake --build . --target install
    (venv)$ cd ../../pygit2
    (venv)$ git checkout v0.20.2
    (venv)$ export LIBGIT2=$VIRTUAL_ENV
    (venv)$ export LDFLAGS="-Wl,-rpath='$LIBGIT2/lib',--enable-new-dtags"
    (venv)$ python setup.py build
    (venv)$ python setup.py install


That should set you up with ``pygit2`` ready to roll in your virtual
environment. This command should not fail:

::

    (venv)$ python
    >> import pygit2
    >>

It was a big headache for me to get ``pygit2`` built and linked correctly, out
of a virtualenv. Also, having to clone full git repos and everything is a pain.

``venvgit2`` ships with all the sources for a matched pair of ``libgit2`` and
``pygit2`` baked in, so you only have to download what you need, and
installation is automated in the ``setup.py`` script. Piece of cake.


Versions
^^^^^^^^

Releases of ``venvgit2`` are synchronized with ``pygit2``, which in tern
synchronizes with minor releases of ``libgit2``. All the major/minor versions
should always match, so installing ``venvgit2==0.20.2.0`` will, as of today,
set up ``libgit2==0.20.0`` and ``pygit2==0.20.2``.

Fixes and updates to ``venvgit2`` will (hopefully) be rare apart from updating
the ``py``- and ``libgit2`` submodules to sync up. If there are bugfixes to
``venvgit2`` itself, they will increment an extra version level, like
``venvgit2==0.20.2.1``, ``venvgit2==0.20.2.2``, etc.



License
-------

``venvgit2`` is provided to the Public Domain. It really doesn't do much
anyway.


The libraries used by ``venvgit2`` have licenses you should be aware of. They
are linked here for quick reference:

- ``libgit2``: `GPLv2 with linking exception <https://github.com/libgit2/libgit2/blob/development/COPYING>`_
- ``pygit2``: `also GPLv2 with linking exception <https://github.com/libgit2/pygit2#license>`_

#!/usr/bin/env python
"""
    setup
    ~~~~~
"""

import os
from shutil import rmtree
from tempfile import mkdtemp
from setuptools import setup
from setuptools.command.install import install
from subprocess import check_call, CalledProcessError


class Dirs(object):
    """Get a scratch space for compiling and stuff"""

    def __init__(self):
        self.prefix = os.environ.get('VIRTUAL_ENV')
        if self.prefix is None:
            raise SystemExit('Aborting: please activate a virtualenv')
        self.src = os.getcwd()
        self.libgit2_src = os.path.join(self.src, 'libgit2')  # source
        self.pygit2_src = os.path.join(self.src, 'pygit2')  # source

    def __enter__(self):
        self.work_dir = mkdtemp()
        return self

    def __exit__(self, *args):
        os.chdir(self.src)
        rmtree(self.work_dir)


def cmake_is_installed():
    try:
        check_call(['which', 'cmake'])
        return True
    except CalledProcessError:
        return False


def install_libgit2(dirs):
    os.chdir(dirs.work_dir)
    print('  libgit2 cmake...')
    check_call(['cmake', dirs.libgit2_src,
                '-DCMAKE_INSTALL_PREFIX={}'.format(dirs.prefix)])  #, '-BUILD_CLAR=OFF'])
    print('  libgit2 making...')
    check_call(['cmake', '--build', dirs.work_dir, '--target', 'install'])


def install_pygit2(dirs):
    os.environ['LIBGIT2'] = dirs.prefix
    os.environ['LDFLAGS'] = "-Wl,-rpath='{}/lib',--enable-new-dtags {}".format(dirs.prefix, os.environ.get('LDFLAGS', ''))
    script = os.path.join(dirs.pygit2_src, 'setup.py')
    os.chdir(dirs.pygit2_src)
    print('  pygit2 clean...')
    check_call(['python', script, 'clean'])
    print('  pygit2 build...')
    check_call(['python', script, 'build'])
    print('  pygit2 install...')
    check_call(['python', script, 'install'])


class InstallEverything(install):
    """Install everything..."""
    def run(self):
        if not cmake_is_installed():
            raise SystemExit("Aborting: please install cmake")
        with Dirs() as dirs:
            install_libgit2(dirs)
            install_pygit2(dirs)
        # super(InstallEverything, self).run()  # noop?


setup(
    name="venvgit2",
    version="0.0.1",
    # include_package_data=True,
    # package_data={
    #   '': ['README.rst'],
    # },
    cmdclass={
      'install': InstallEverything,
    },
    author='uniphil',
    author_email='uniphil@gmail.com',
    description=open('README.rst').read(),
    license='MPL',
    url='http://github.com/Queens-Hacks/venvgit2',
)

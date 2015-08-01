#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import re
import os
import sys

try:
    import pypandoc
    readme = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    readme = ''


package = 'tapioca_github'
requirements = [
    'tapioca-wrapper==0.4.1',
    'requests-oauthlib==0.4.2',
]
test_requirements = [

]

def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


# python setup.py register
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print "You probably want to also tag the version now:"
    print "  git tag -a %(version)s -m 'version %(version)s'" % args
    print "  git push --tags"
    sys.exit()


setup(
    name='tapioca-github',
    version=get_version(package),
    description='Github API wrapper using tapioca',
    long_description=readme,
    author='Gileno Filho',
    author_email='contato@gilenofilho.com.br',
    url='https://github.com/gileno/tapioca-github',
    packages=[
        'tapioca_github',
    ],
    package_dir={'tapioca_github': 'tapioca_github'},
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='tapioca-github',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
    ],
)

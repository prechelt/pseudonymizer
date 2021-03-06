# based on https://github.com/pypa/sampleproject/blob/master/setup.py
# see http://packaging.python.org/en/latest/tutorial.html#creating-your-own-project

from setuptools import setup, find_packages
from  setuptools.command.install import install  as  stdinstall
import codecs
import os
import re
import sys


def find_version(*file_paths):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
        version_file = f.read()
    # The version line must have the form
    # __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

def get_file_contents(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        contents = f.read()
    return contents


package_name = "pseudonymizer"


setup(
    # basic information:
    name=package_name,
    version=find_version('pseudonymizer', '__init__.py'),
    description="consistently replacing strings with meaningful pseudonyms",
    long_description=get_file_contents("README.rst"),

    # The project URL:
    url='http://github.com/prechelt/' + package_name,

    # Author details:
    author='Lutz Prechelt',
    author_email='prechelt@inf.fu-berlin.de',

    # Classification:
    license='MIT License',
    classifiers=[
        'License :: OSI Approved :: MIT License',

        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing :: Data Generation',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='test data generation',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages.
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),

    # List run-time dependencies here. These will be installed by pip when your
    # project is installed.
    install_requires = [],

    # If there are data files included in your packages that need to be
    # installed, specify them here. If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        # 'typecheck': ['package_data.dat'],
    },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages.
    # see http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    ###data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    ### entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
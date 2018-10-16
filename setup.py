import os
import pwd
import grp

from setuptools import setup, Command
from setuptools.command.install import install
from distutils.util import convert_path

def get_version():
    d = {}
    with open('bin/stdict') as fp:
        exec(fp.read(), d)

    return d["__version__"]

setup(name="stdict",
      description="Console tool to lookup words in Oxford Dictionary ",
      license="MIT",
      version=get_version(),
      maintainer="Andrey Zhidenkov",
      maintainer_email="pensnarik@gmail.com",
      url="http://parselab.ru",
      scripts=['bin/stdict'],
      packages=[],
      install_requires=["requests", "lxml"],
)

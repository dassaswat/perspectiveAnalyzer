from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.2'
DESCRIPTION = 'A simple python wrapper for perspective API'
LONG_DESCRIPTION = 'Use the simplicity of the perspectiveAnalyzer to make powerful api calls to analyze texts toxicity. This package will help you build better software in lesser time!'

# Setting up
setup(
    name="perspectiveAnalyzer",
    version=VERSION,
    author="Saswat Das",
    author_email="saswatd19@gmail.com",
    description=DESCRIPTION,
    url="https://github.com/dassaswat/perspectiveAnalyzer",
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['google-api-python-client==2.6.0'],
    keywords=['python', 'api', 'discord',
              'perspective api', 'text analyzer', 'google api client'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

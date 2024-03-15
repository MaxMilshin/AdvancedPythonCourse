from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Simple LATEX generation'

# Setting up
setup(
    name="latexgen",
    version=VERSION,
    author="Maxonchik2003",
    author_email="Maxonchik2003@yandex.ru",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'latex'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
from setuptools import setup

setup(
    name = 'booklover',
    version = '0.1.0',
    author = 'Doruk Ozar',
    author_email = 'dorukozar@gmail.com',
    packages = ['booklover'],
    url = 'https://github.com/Dorukozar/HW-M09',
    license = 'MIT',
    description = 'creates booklover class and tests it',
    long_description = open('README.md').read(),
    install_requires = ["pandas", "numpy"],
)
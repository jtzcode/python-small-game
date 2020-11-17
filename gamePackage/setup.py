from distutils.core import setup

with open('README') as file:
    readme = file.read()

setup(
    name='Game of Thrones - Cartoons',
    version='2.0.0',
    packages=['game'],
    url='',
    license='LICENSE.txt',
    description='',
    long_description=readme,
    author='Eggy',
    author_email='eggy@pupu.com'
)
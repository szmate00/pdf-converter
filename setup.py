from setuptools import setup, find_packages

setup(
    name='pdf-converter',
    version='1.0',
    description='A PDF converter app',
    author='Máté Szűcs',
    author_email='mate.szucs@tum.com',
    url='https://github.com/szmate00/pdf-converter',
    packages=find_packages(),
    install_requires=[
        'pdf2image',
    ],
    entry_points={
        'console_scripts': [
            'pdf-converter=pdf_converter.main:main',
        ],
    },
)
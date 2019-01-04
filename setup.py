from setuptools import setup, find_packages
import secret_key


setup(
    name             = 'DjangoSecretKey',
    version          = secret_key.__version__,
    description      = 'Django SECRET_KEY management',
    license          = 'MIT',
    long_description = open('README.rst').read(),
    author           = 'Min Choro',
    author_email     = 'blinglnav@gmail.com',
    url              = 'https://github.com/blinglnav/djangosecretkey',
    install_requires = [
        'pytest',
    ],
    packages         = find_packages(exclude = ['tests*']),
    keywords         = ['django', 'secret_key', 'secret'],
    python_requires  = '>=3.6',
    zip_safe=False,
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6'
    ]
)
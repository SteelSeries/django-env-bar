from io import open
from setuptools import setup

import env_bar

setup(
    name='django-env-bar',
    version=env_bar.__version__,
    description='A basic panel displaying the name of the current environment.',
    long_description=open('README.rst', encoding='utf-8').read(),
    keywords='django, development, devtools',
    author='Michael Pedersen',
    author_email='pypi@steelseries.com',
    url='https://github.com/steelseries/django-env-bar',
    download_url='https://pypi.python.org/pypi/django-env-bar',
    license='MIT',
    packages=['env_bar'],
    install_requires=[
        'Django>=1.7',
    ],
    include_package_data=True,
    zip_safe=False,                 # because we're including static files
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django :: 1.7',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

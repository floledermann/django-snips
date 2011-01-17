# Copyright (C) 2010 Florian Ledermann ledermann@ims.tuwien.ac.at

from setuptools import setup, find_packages
 
setup(
    name='django-snips',
    version='0.1',
    description='A minimal CMS app for Django.',
    author='Flo Ledermann',
    author_email='ledermann@ims.tuwien.ac.at',
    url='http://bitbucket.org/floledermann/django-snips/',
    license='GPL',
    package_dir = {'': 'src/python'},
    packages=['snippets'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
)

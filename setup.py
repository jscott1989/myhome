from setuptools import setup, find_packages

setup(
    name='myhome',
    version="0.3",
    license="MIT",

    install_requires = [
        "requests",
    ],

    description='Screen scraping based API for British Gas MyHome',
    long_description=open('README.txt').read(),

    author='Jonathan Scott',
    author_email='jonathan@jscott.me',

    url='http://github.com/jscott1989/myhome',
    download_url='http://github.com/jscott1989/myhome/downloads',

    include_package_data=True,

    packages=['myhome'],

    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
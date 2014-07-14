from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='drchen.theme',
    version=version,
    description="DrChen Theme",
    long_description=open("README.rst").read() + "\n" +
                     open(os.path.join("docs", "HISTORY.rst")).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='web zope plone theme diazo',
    author='TsungWei Hu',
    author_email='marr.tw@gmail.com',
    url='http://github.com/l34marr/drchen.theme/',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['drchen'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
    ],
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
    )

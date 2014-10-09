from setuptools import setup, find_packages
import os

version = '0.2.1.dev0'

setup(name='rt.zptformfield',
      version=version,
      description="Some ZPT macros for Zope/Plone HTML forms development",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Zope2",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        ],
      keywords='plone zpt zope form macro',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='http://github.com/RedTurtle/rt.zptformfield',
      license='GPL',
      namespace_packages=['rt'],
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

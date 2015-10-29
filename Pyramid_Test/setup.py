from setuptools import setup

requires = [
    'pyramid',
    'pyramid_chameleon',
    'deform',
    'pyramid_debugtoolbar',
    'ZODB3',
    'pyramid_tm',
    'pyramid_zodbconn',
]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)

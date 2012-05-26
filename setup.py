from setuptools import setup, find_packages

version = '0.1'

setup(name='dataissues',
      version=version,
      description="Reporting platform for data wranglers",
      long_description="",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Topic :: Database"],
      keywords='rest api errors logging data wrangling',
      author='Open Knowledge Foundation',
      author_email='info@okfn.org',
      url='http://okfn.org',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )

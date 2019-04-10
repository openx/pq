"""PQ is a transactional queue for PostgreSQL."""

from setuptools import setup, find_packages

import pq

setup(
    name=pq.__title__,
    version=pq.__version__,
    license=pq.__license__,
    author=pq.__author__,
    url='https://github.com/malthe/pq/',
    author_email='mborch@gmail.com',
    description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        #  As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
    ],
    tests_require=['psycopg2cffi'],
    test_suite="pq.tests"
)

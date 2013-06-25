from setuptools import setup, find_packages
from distutils.core import setup
from distutils.extension import Extension

try:
    # this import fixes strange issues with nose testing !
    import multiprocessing
except:
    pass

import pyprophet.version

ext_modules = [Extension("pyprophet._optimized", ["pyprophet/optimized.c"])]

setup(name='pyprophet',
    version=pyprophet.version.version,
    author="Uwe Schmitt",
    author_email="rocksportrocker@gmail.com",
    description="Python reimplementation of mProphet peak scoring",
    license="BSD",
    url="http://github.com/uweschmitt/pyprophet",
    packages=find_packages(exclude=['ez_setup',
                        'examples', 'tests']),
    include_package_data=True,
    classifiers = [
         'Development Status :: 3 - Alpha',
         'Environment :: Console',
         'Intended Audience :: Science/Research',
         'License :: OSI Approved :: BSD License',
         'Operating System :: OS Independent',
         'Topic :: Scientific/Engineering :: Bio-Informatics',
         'Topic :: Scientific/Engineering :: Chemistry',
        ],
    zip_safe=False,
    install_requires=[
        "numpy >= 1.7.0",
        "pandas >= 0.10.0",
        "scipy >= 0.9.0",
        "numexpr >= 2.1",
        "scikit-learn >= 0.13",
        ],
    test_suite="nose.collector",
    tests_require="nose",
    entry_points = {
        'console_scripts' : [
            "pyprophet=pyprophet.main:main",
            ]
        },
    #cmdclass = { 'build_ext': build_ext },
    ext_modules = ext_modules,
)
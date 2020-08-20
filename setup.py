from setuptools import setup
from setuptools import find_packages

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.

test_requires = [
    'pytest',
    'pytest-coverage',
    'pytest-mock'
]

setup(
    name="Clean Arch",
    version='0.1.0',
    install_requires=[
        "fastapi>=0.60.1,<1.0.0",
        "SQLAlchemy>=1.3.18,<1.4",
        'requests>=2.24.0,<2.25'
    ],
    package_dir={'': 'src'},
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
    tests_require=test_requires,
    setup_requires=['pytest-runner'],
    extras_require={
        'tests': test_requires,
    },
)

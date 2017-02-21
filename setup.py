from setuptools import setup

setup(
    name="codewars katas",
    description="this module holds all katas for kyus 5 or higher",
    version=0.9,
    author="Marc Kessler-Wenicker",
    author_email="",
    license="MIT",
    package_dir={'': './kyu5/src'},
    py_modules=["find_sum"],
    install_requires=[],
    extras_require={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={}
)

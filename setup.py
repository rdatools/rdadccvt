from setuptools import setup, find_packages

"""
https://python-packaging.readthedocs.io/en/latest/minimal.html
https://packaging.python.org/en/latest/specifications/declaring-project-metadata/

Once:

$ python3 -m pip install --upgrade build
$ python3 -m pip install --upgrade twine

Each iteration:

$ python3 -m build
$ python3 -m twine upload --repository pypi dist/rdadccvt-x.y.z*.*

"""

setup(
    name="rdadccvt",
    version="1.0.0",
    description="Balzer's algorithm (DCCVT) to find a maximally population compact map",
    url="https://github.com/rdatools/rdadccvt",
    author="alecramsay",
    author_email="a73cram5ay@gmail.com",
    license="MIT",
    packages=[
        "rdadccvt",
    ],
    install_requires=["rdabase", "scipy"],
    zip_safe=False,
)

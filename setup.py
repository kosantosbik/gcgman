import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gcgman",
    version="0.0.3",
    author="N.Ahmet BASTUG",
    author_email="bastugn@itu.edu.tr",
    description="A package to write any letter you want in the github graph",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kosantosbik/gcgman",
    scripts=['bin/gcgman'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Unix",
    ],
)

from setuptools import setup, find_packages

with open("./README.md", "r") as f:
    long_description = f.read()

setup(
    name="pyURControl",
    version="0.0.1",
    description="Python package for controling an Universal Robots",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hganchev/python-ur-control",
    author="hganchev",
    author_email="hrist0.ganchew@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    install_requires=[""],
    extras_require={
        "dev": ["pytest>=7.4", "twine>=4.0.2"],
    },
    python_requires=">=3.11",
)
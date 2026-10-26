from setuptools import find_packages, setup


setup(
    name="bu-cascade",
    version="3.20",
    description="Cascade Server web services integration",
    long_description="Python package for integrating with Cascade Server web services.",
    author="Caleb Schwarze",
    author_email="c-schwarze@bethel.edu",
    url="https://github.com/betheluniversity/cascade/",
    license="Apache-2.0",
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=[
        "suds-community>=1.1.2,<1.2",
        "beautifulsoup4<4.13",
    ],
    extras_require={
        "test": [
            "pytest>=6.2,<7",
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)

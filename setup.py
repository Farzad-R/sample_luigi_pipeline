import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "sample_luigi_pipeline",
    version = "0.1.0",
    description = "A sample pipeline using luigi, pip, and os",
    authors = ["Farzad Roozitalab <farzadroozitalab@cmail.carleton.ca>"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Farzad-R/sample_luigi_pipeline",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: linux",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.8.5',
)

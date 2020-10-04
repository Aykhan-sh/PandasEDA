import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PandasEDA", # Replace with your own username
    version="0.0.1",
    author="Aykhan-sh",
    author_email="a.turlasov@gmail.com",
    description="Set of functions for pandas datafraym EDA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aykhan-sh/Pandas-EDA",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
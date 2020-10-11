import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws",
    version="0.0.1",
    author="Pradham Kuchipudi",
    author_email="pradhamk@gmail.com",
    description="An amazon webscraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PKyahhh/aws",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independant"
    ],
    python_requires = '>=3.6',   
)

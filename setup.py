import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-h1bp",
    version="0.1.0",
    author="rangulvers",
    description="Check if you have been pwned",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rangulvers/h1bp",
    project_urls={
        "Bug Tracker": "https://github.com/rangulvers/h1bp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

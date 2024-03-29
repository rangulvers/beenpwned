import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="beenpwned",
    version="0.1.1",
    author="rangulvers",
    description="Check if you have been pwned",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rangulvers/beenpwned",
    project_urls={
        "Bug Tracker": "https://github.com/rangulvers/beenpwned/issues",
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

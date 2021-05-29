import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="ga-project-RobbyB97",
    version="0.0.1",
    author="Robby Bergers",
    author_email="bergersr97@gmail.com",
    description="Genetic Algorithm vs. 8 Queens",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.3'
)
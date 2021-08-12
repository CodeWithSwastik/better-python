from setuptools import setup

version = "1.0.0"
 
with open("README.md", "r", encoding="utf-8") as readme_file:
    long_description = readme_file.read()

setup(
    name="better-python",
    version=version,
    description="Add more functionality to Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Swas.py",
    author_email="cwswas.py@gmail.com",
    py_modules = ['betterpython'],
    url = "https://github.com/CodeWithSwastik/better-python", 
    project_urls={
    "Issue tracker": "https://github.com/CodeWithSwastik/better-python/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    install_requires=['forbiddenfruit'],
    python_requires=">=3.6",
)

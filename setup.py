import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyhtmltext", # Replace with your username
    version="0.0.4",
    author="Maksim Prilepsky",
    author_email="maksimprilepsky@yandex.ru",
    description="Usefull tool for extracting text and sentences from html",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaksimJames/pyhtmltext",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['razdel==0.5.0']
)
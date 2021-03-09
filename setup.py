import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="h3converter", # Replace with your own username
    version="0.0.1",
    author="Kapil Gauravan V",
    author_email="kapilgrv@gmail.com",
    description="This package helps you convert h3 hec code directly to geojson and a GeoJSON entity to h3 hex code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kapil-grv/h3converter",
    project_urls={
        "Bug Tracker": "https://github.com/kapil-grv/h3converter/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    package_data={'h3converter': ['*.dylib', '*.so', '*.1']},
    install_requires=['geojson'],
    include_package_data=True,
    python_requires=">=3.6",
)
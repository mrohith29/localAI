import setuptools 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="localgpt",
    version="0.1.1",
    description="Enables you to chat with AI locally",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrohith29/localgpt",
    author="Mariyala Rohith",
    author_email="mariyalarohith29@gmail.com",
    license="MIT",
    project_urls={
        "Homepage": "https://github.com/mrohith29/localgpt",
        "Issues": "https://github.com/mrohith29/localgpt/issues",
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=["rich"],
    entry_points={
        "console_scripts": [
            "sweety=run.__init__",
        ]
    },
)
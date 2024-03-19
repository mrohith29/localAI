import setuptools 

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="chatlocalai",
    version="0.1.5",
    description="Enables you to chat with AI locally without internet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrohith29/nonetchat",
    author="Mariyala Rohith",
    author_email="mariyalarohith29@gmail.com",
    license="MIT",
    project_urls={
        "Homepage": "https://github.com/mrohith29/nonetchat",
        "Issues": "https://github.com/mrohith29/nonetchat/issues",
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
    install_requires=["rich", "ollama"],
    entry_points={
        "console_scripts": [
            "hey=hey.__init__",
        ]
    },
)
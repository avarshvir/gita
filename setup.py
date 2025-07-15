from setuptools import setup, find_packages

setup(
    name="gita-py",
    version="0.1.2",
    description="A Python package providing Bhagavad Gita summaries and verses.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Arshvir",
    author_email="avarshvir@gmail.com",
    url="https://github.com/avarshvir/gita",
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Religion",
        "Topic :: Education",
        "Intended Audience :: Education",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

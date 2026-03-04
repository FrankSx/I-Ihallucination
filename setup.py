from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ml-hallucination-toolkit",
    version="1.0.0",
    author="frankSx",
    author_email="fixes.it.frank@googlesmail.com",
    description="ML Hallucination Generator Toolkit for Adversarial Research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frankSx/ml-hallucination-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    entry_points={
        'console_scripts': [
            'mlhallucination=attacks.coordinator:main',
        ],
    },
    keywords="adversarial-ml hallucination security research ghostbyte",
    project_urls={
        "Bug Reports": "https://github.com/frankSx/ml-hallucination-toolkit/issues",
        "Source": "https://github.com/frankSx/ml-hallucination-toolkit",
        "Blog": "https://frankhacks.blogspot.com",
    },
)

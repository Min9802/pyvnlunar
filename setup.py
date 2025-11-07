from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="vnlunar",
    version="1.0.3",
    author="Min",
    author_email="hieumin9802@gmail.com",
    description="Vietnamese Lunar Calendar Library for Python - Thư viện Âm lịch Việt Nam",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/min9802/pyvnlunar",
    packages=find_packages(exclude=["examples", "examples.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Astronomy",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Natural Language :: Vietnamese",
    ],
    keywords="vietnamese lunar calendar amlich lich am vietnam astronomy",
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=0.990",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/yourusername/vnlunar/issues",
        "Source": "https://github.com/yourusername/vnlunar",
        "Documentation": "https://github.com/yourusername/vnlunar#readme",
    },
    include_package_data=True,
    zip_safe=False,
)

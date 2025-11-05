"""
Setup configuration for Apriori Recommendation System.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read requirements
requirements = []
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="apriori-recommendation-system",
    version="1.1.0",
    author="Fernanda Flores, Kevin Arciniegas, Giussepe Marreros",
    author_email="",
    description="Sistema de Recomendaciones Personalizadas con Apriori y R",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kevarci/Apriori-Latex-Project-Final",
    packages=find_packages(exclude=["tests", "tests.*", "notebooks", "docs"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "apriori-app=app:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="apriori, recommendation system, data mining, association rules, machine learning",
    project_urls={
        "Bug Reports": "https://github.com/kevarci/Apriori-Latex-Project-Final/issues",
        "Source": "https://github.com/kevarci/Apriori-Latex-Project-Final",
        "Documentation": "https://github.com/kevarci/Apriori-Latex-Project-Final#readme",
    },
)

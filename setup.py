from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="browser-history-analytics-2",
    version="1.0.0",
    author="Arpit Sengar (arpy8)",
    description="A package to visualize your browser history :D",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'browser_history_analytics_2': ['*.py'],
    },
    install_requires=[
        "streamlit", 
        "plotly", 
        "pandas", 
        "browser-history", 
        "numpy", 
        "seaborn", 
        "matplotlib", 
        "urllib3",
        "setuptools==66.1.1",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "bha=browser_history_analytics_2.main:main",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
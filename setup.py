from setuptools import setup, find_packages

setup(
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    description="Python Client wrapper for Steam Web API",
    keywords=[
        "steam",
        "steam api",
        "steam community",
        "steam web api"
    ],
    name='py-steam-web-api',
    url="https://github.com/sylas00/py-steam-web-api",
    version='0.2',
    author="sylas00",
    author_email="xyjy5247@gmail.com",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'requests >= 2.31.0',
    ],
)
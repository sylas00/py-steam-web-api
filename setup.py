from setuptools import setup, find_packages

setup(
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    name='py-steam-web-api',
    version='0.1',
    author="sylas00",
    author_email="xyjy5247@gmail.com",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'requests >= 2.31.0',
    ],
)
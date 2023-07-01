from setuptools import setup

setup(
    name="markplotlib",
    version="0.1",
    description="my personal plotting style",
    url="https://github.com/markmbaum/markplotlib",
    author="Mark Baum",
    packages=["markplotlib"],
    install_requires=["matplotlib>=3.7"],
    include_package_data=True,
)

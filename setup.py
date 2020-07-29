from setuptools import setup

with open("README") as f:
    long_description = f.read()

setup(
    name="tiktok_scraper",
    version="1.1.0",
    description="Scrapes tiktok video list for frequent comment section",
    license="MIT",
    long_description=long_description,
    author="Maximillian Rampulla",
    author_email="maxrampulla@gmail.com",
    py_modules=["main"]
)

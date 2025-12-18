from setuptools import find_packages, setup

setup(name = "e-commerce-bot",
      version = "0.1",
      author = "Ravi Kumar",
      author_email = "ravi14thakur@gmail.com",
      packages=find_packages(),
      install_requires=["langchain","langchain-astradb"]) 

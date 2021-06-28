from setuptools import setup

requeriments = []

try:
    content = None
    with open("requeriments.txt") as f:
        content = f.readlines()
    requeriments = [x.strip() for x in content] 
except Exception as error:
    print(f"Error parsing requeriments.txt: {error}")


setup(
    name='Base App',
    version='1.0',
    description='Flask base app boilerplate',
    author='Marcos Fuenmayor',
    author_email='marcos.fuenmayorhtc@gmail.com',
    packages=['src'],  
    install_requires=requeriments
)
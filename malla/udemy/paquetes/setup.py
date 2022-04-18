from setuptools import setup

setup (
    name = "paquete",
    version = "0.1",
    description="este es un paquete de ejemplo",
    author="Miguel Herrera",
    author_email="miguelh1299@gmail.com",
    url="http://hcosta.info",
    scripts=[],
    packages=["paquete","paquete.Adios","paquete.Hola"],
)


from setuptools import setup, find_packages
setup(
    name="etaledger",
    version="0.1.0",
    description="Thermodynamic efficiency measurement for computation — η = useful_joules / human_joules",
    author="Jesse Ray (OpenRoot)",
    license="GPL-3.0",
    packages=find_packages(),
    python_requires=">=3.8",
)

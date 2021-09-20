from setuptools import setup

setup(
    name="pim",
    version="1.0.0",
    install_requires=["wxPython"],
    entry_points={
        "console_scripts": [
            "pim = main:main"
        ]
    }
)

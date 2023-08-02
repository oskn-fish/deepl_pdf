from setuptools import setup

setup(
    name="deepl_pdf",
    install_requires=["deepl"],
    entry_points={
        "console_scripts":["deepl_pdf=deepl_pdf:main"]
    }
)
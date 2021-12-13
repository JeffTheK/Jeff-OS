from setuptools import setup

setup(
    name = "jeffos",
    version = "1.0.0",
    description = "Essential Jeff-OS library",
    author = "JeffTheK",
    packages = ["jeffos"],
    package_data = {
        "ary": [
            "data/*/*"
        ]
    }
)
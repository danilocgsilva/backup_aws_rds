from setuptools import setup

VERSION = '1.0.0'

def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="backup-rds",
    version=VERSION,
    description="Make a database backup from RDS",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keyword="Download Amazon AWS RDS",
    url="https://github.com/danilocgsilva/backup_aws_rds",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["backup_rds"],
    entry_points={"console_scripts": ["rdsaccess=backup_rds.__main__:main"]},
    include_package_data=True
)

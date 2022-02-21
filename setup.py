import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='pgsql_connector',
    version='0.0.1',
    author='Oleg Maslennikov',
    author_email='maslolpavl@gmail.com',
    description='Test',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Ilwapoi/pgsql_connector',
    license='MIT',
    packages=['pgsql_connector'],
    install_requires=['pandas','psycopg2','numpy'],
)
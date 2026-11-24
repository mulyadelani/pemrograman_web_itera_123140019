from setuptools import find_packages, setup


setup(
    name="pyramid-mahasiswa",
    version="0.1.0",
    description="RESTful API mahasiswa dan mata kuliah dengan Pyramid",
    packages=find_packages(),
    include_package_data=True,
    package_data={"pyramid_mahasiswa": ["alembic/*.mako"]},
    install_requires=[
        "alembic>=1.13",
        "psycopg2-binary>=2.9",
        "pyramid>=2.0",
        "pyramid_tm>=2.5",
        "SQLAlchemy>=2.0",
        "transaction>=4.0",
        "waitress>=3.0",
        "zope.sqlalchemy>=3.1",
    ],
    extras_require={"testing": ["pytest>=8.0"]},
    entry_points={
        "paste.app_factory": [
            "main = pyramid_mahasiswa:main",
        ],
    },
)

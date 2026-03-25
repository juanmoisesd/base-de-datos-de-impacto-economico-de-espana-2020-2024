from setuptools import setup, find_packages
setup(
    name="base-de-datos-de-impacto-economico-de-espana-2020-2024",
    version="1.0.0",
    description="Este dataset recopila indicadores macroecon&oacute;micos y financieros clave de Espa&ntilde;a para e",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="cc0, citation, dataset, development-economics, economics, europe, fair-data, gdp, juan-moises-de-la-serna, latin-america, macroeconomics, open-data, open-science, orcid, research, spain, zenodo, zenodo, open-data",
)
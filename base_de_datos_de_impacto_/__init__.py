"""Este dataset recopila indicadores macroecon&oacute;micos y financieros clave de Espa&ntilde;a para e
DOI: https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024 | GitHub: https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Este dataset recopila indicadores macroecon&oacute;micos y financieros clave de . Zenodo. https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024'
def info():print(f"Dataset: Este dataset recopila indicadores macroecon&oacute;micos y financieros clave de \nDOI: https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024\nGitHub: https://github.com/juanmoisesd/base-de-datos-de-impacto-economico-de-espana-2020-2024")
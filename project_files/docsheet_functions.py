# %% Imports
import pandas as pd
from time_functions import get_current_month


def load_csv(path: str = None):
    df = pd.read_csv(path)
    pass


def export_to_excel(df: pd.DataFrame = None, name: str = None):
    assert df is not None

    if name == None:
        name = get_current_month()

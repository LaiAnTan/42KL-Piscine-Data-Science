import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Loads a csv into a Pandas DataFrame and returns it.

    @return df: pandas DataFrame containing data from the csv.
    @raise Exception: file not found
    """
    try:
        df = pd.read_csv(path)
    except Exception:
        print(f"Error: bad file")
        return

    print(f"Loading DataFrame of size {df.shape}")
    return df

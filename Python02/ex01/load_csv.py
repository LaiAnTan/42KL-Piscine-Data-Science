import pandas as pd

def load(path: str) -> pd.DataFrame:
    
    try:
        df = pd.read_csv(path)
    except Exception as err:
        print(f"Error: {err.args[0]}")
    
    print(f"Loading DataFrame of size {df.shape}")
    return df
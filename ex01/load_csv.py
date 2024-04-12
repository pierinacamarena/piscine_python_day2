import pandas as pd
from typing import Optional


def load(path: str) -> Optional[pd.DataFrame]:
    try:
        if not path.lower().endswith('csv'):
            raise ValueError("File must be a .csv")

        # Load dataset into a dataframe
        df = pd.read_csv(path)

        # Retrieve dimensions and print them
        dimensions = df.shape
        print(f"Loading dataset of dimensions {dimensions}")
        return df

    except (
        FileNotFoundError,
        pd.errors.EmptyDataError,
        pd.errors.ParserError,
        pd.errors.EmptyDataError,
        ValueError
    ) as error:
        print(f"Error: {error}")
        return None

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return None

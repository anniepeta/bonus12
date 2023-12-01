import pandas as pd
import numpy as np


def pandas_random_data():
    """Print a pandas df with random data."""
    # random number generator
    rng = np.random.default_rng()

    # create random nrows for dataframe
    nrows = rng.integers(1, 150)

    # col 1 of random ints
    col_one = rng.integers(low=0, high=100000, size=nrows)
    # col 2 of random flotas
    col_two = rng.random(size=nrows)

    # create df and print the result
    df = pd.DataFrame({"column_1": col_one, "column_2": col_two})

    print(df)

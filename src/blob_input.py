from datetime import datetime
from typing import List, Optional

import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from adlfs import AzureBlobFileSystem


def get_data() -> pd.DataFrame:
    """Generate random data"""

    N_ROWS = 1000
    UNITS = ["a", "b", "c", "d", "e"]
    ids = np.repeat(UNITS, N_ROWS)
    data = np.random.randint(
        0,
        100,
        size=(len(UNITS) * N_ROWS),
    )

    df = pd.DataFrame({"id": ids, "value": data, "created": datetime.now()})

    print("Generated data")

    return df


def df_to_pyarrow(df: pd.DataFrame, schema: pa.Schema):
    """Convert Pandas dataframe to Pyarrow table"""

    df_pyarrow = pa.Table.from_pandas(df, schema=schema)

    return df_pyarrow


def write_parquet_to_blob(
    table: pa.Table,
    container: str,
    pq_name: str,
    conn_str: str,
    partition_cols: Optional[List[str]] = None,
):
    """Write Pyarrow table to Azure Blob Storage"""
    print("Inserting to blob storage...")
    abfs = AzureBlobFileSystem(connection_string=conn_str)
    pq.write_to_dataset(
        table,
        f"{container}/{pq_name}",
        filesystem=abfs,
        partition_cols=partition_cols,
    )
    print("Done")

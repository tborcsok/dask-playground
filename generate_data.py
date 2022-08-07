from src.blob_input import df_to_pyarrow, get_data, write_parquet_to_blob
from src.constants import CONN_STR_LOCAL, DATA_SCHEMA_V1


def main():
    df = get_data()

    df_pa = df_to_pyarrow(df, DATA_SCHEMA_V1)

    write_parquet_to_blob(
        df_pa,
        container="daskdata",
        pq_name="random.parquet",
        conn_str=CONN_STR_LOCAL,
        partition_cols=["id", "created"],
    )


if __name__ == "__main__":

    main()

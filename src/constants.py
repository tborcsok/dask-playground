import pyarrow as pa

# define the data schema we wish to collect
DATA_SCHEMA_V1 = pa.schema(
    [("id", pa.string()), ("value", pa.int64()), ("created", pa.timestamp("ns"))]
)

# https://docs.microsoft.com/en-us/azure/storage/common/storage-use-azurite?tabs=visual-studio#well-known-storage-account-and-key
CONN_STR_LOCAL = (
    "DefaultEndpointsProtocol=https;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=https://127.0.0.1:10000/devstoreaccount1"
)

CONN_STR_DOCKER = (
    "DefaultEndpointsProtocol=https;"
    "AccountName=devstoreaccount1;"
    "AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;"
    "BlobEndpoint=https://azurite:10000/devstoreaccount1"
)

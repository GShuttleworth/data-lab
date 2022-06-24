import pandas as pd

# Read in parquet file
df = pd.read_parquet("yellow_tripdata_2022-01.parquet")

# Format/rename columns
df.rename(
    columns={
        "tpep_pickup_datetime": "pickup_datetime",
        "tpep_dropoff_datetime": "dropoff_datetime",
    },
    inplace=True,
)

# Add measurement column data
df["_measurement"] = "taxi_data"
df.set_index("pickup_datetime")
# Limit number of rows
# df = df.head(500000)

# Output to CSV
df.to_csv("yellow_tripdata_2022-01.csv", index=False)

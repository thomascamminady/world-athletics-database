import glob

import polars as pl

from world_athletics_database import logger


def transform_times(s: str | float):
    if isinstance(s, float):
        return s
    y = s.split(":")
    if not y[-1].isalnum():
        y[-1] = y[-1][:-1]
    if len(y) == 3:  # hh:mm:ss
        return 3600 * float(y[0]) + 60 * float(y[1]) + float(y[2])
    elif len(y) == 2:  # mm:ss
        return 60 * float(y[0]) + float(y[1])
    elif len(y) == 1:  # s.ms
        return float(y[0])
    else:
        raise Exception(f"Could not convert {s}")


def transform_score(s):
    return float(s)


def transform_rank(s):
    return float(s)


def postprocess():
    for sex in ["women", "men"]:
        csv_files = glob.glob(f"./data/{sex}/*.csv")
        logger.info(csv_files)
        df_list = []

        for csv in csv_files:
            if "relay" in csv:
                continue
            df = pl.read_csv(csv, infer_schema_length=10000)
            if "decathlon" in csv or "heptathlon" in csv:
                df = df.take_every(2)  # every second row is the individual marks
                cols = df.columns
                df = df.select(c for c in cols[:11])  # throw away all individual marks

            df = df.with_columns(
                pl.col("Mark").apply(transform_times).cast(float),
                pl.col("Rank").apply(transform_rank).cast(int),
                pl.col("Results Score").apply(transform_score).cast(int),
                pl.col("Pos").cast(str),
                pl.lit(
                    csv.split("/")[-1].replace(".csv", "").replace("-", " ").title()
                ).alias("Event"),
            )
            df_list.append(df)

        df = (
            pl.concat(df_list, how="diagonal")
            .drop("Unnamed: 6", "Unnamed: 7")
            .rename(mapping={"WIND": "Wind"})
            .with_columns(
                pl.col("DOB").str.strptime(pl.Date, format="%d %b %Y", strict=False),
                pl.col("Date").str.strptime(pl.Date, format="%d %b %Y", strict=False),
            )
        )
        df.write_parquet(f"./data/{sex}.parquet")


if __name__ == "__main__":
    postprocess()

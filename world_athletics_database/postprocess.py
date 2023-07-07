import dataclasses
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


def postprocess_step1():
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

            if "Unnamed: 6" in df.columns:
                df = df.drop("Unnamed: 6")
            if "Unnamed: 7" in df.columns:
                df = df.drop("Unnamed: 7")
            df.write_csv(csv)

            df = df.with_columns(pl.col("Mark").cast(str)).with_columns(
                pl.col("Mark")
                .apply(transform_times)
                .cast(float)
                .alias("Mark [meters or seconds]"),
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
            # .drop("Unnamed: 6", "Unnamed: 7")
            .rename(mapping={"WIND": "Wind"}).with_columns(
                pl.col("DOB").str.strptime(pl.Date, format="%d %b %Y", strict=False),
                pl.col("Date").str.strptime(pl.Date, format="%d %b %Y", strict=False),
            )
        )
        df.write_parquet(f"./data/{sex}.parquet")


def postprocess_step2():
    df = pl.concat(
        [
            pl.read_parquet("data/men.parquet").with_columns(
                pl.lit("male").alias("Sex")
            ),
            pl.read_parquet("data/women.parquet").with_columns(
                pl.lit("female").alias("Sex")
            ),
        ]
    ).drop(columns=[""])
    # info = {
    #     "5 Kilometres Race Walk": ("Race Walking", "Metres", 5000),
    #     "30 Kilometres Race Walk": ("Race Walking", "Metres", 30000),
    #     "100 Metres Hurdles": ("Sprint", "Metres", 100),
    #     "3000 Metres Steeplechase": ("Middle Distance", "Metres", 3000),
    #     "400 Metres Hurdles": ("Sprint", "Metres", 400),
    #     "Javelin Throw": ("Throwing", "Metres", None),
    #     "Discus Throw": ("Throwing", "Metres", None),
    #     "1000 Metres": ("Middle Distance", "Metres", 1000),
    #     "35 Kilometres Race Walk": ("Race Walking", "Metres", 35000),
    #     "600 Metres": ("Sprint", "Metres", 600),
    #     "800 Metres": ("Middle Distance", "Metres", 800),
    #     "One Mile": ("Middle Distance", "Metres", 1609),
    #     "3000 Metres": ("Middle Distance", "Metres", 3000),
    #     "10000 Metres Race Walk": ("Race Walking", "Metres", 10000),
    #     "Heptathlon": ("Multi-events", "Points", None),
    #     "Triple Jump": ("Jumping", "Metres", None),
    #     "10 Miles Road": ("Road Running", "Metres", 16093),
    #     "20 Kilometres Race Walk": ("Race Walking", "Metres", 20000),
    #     "2000 Metres": ("Middle Distance", "Metres", 2000),
    #     "2000 Metres Steeplechase": ("Middle Distance", "Metres", 2000),
    #     "20 Kilometres": ("Road Running", "Metres", 20000),
    #     "5000 Metres": ("Long Distance", "Metres", 5000),
    #     "50 Kilometres Race Walk": ("Race Walking", "Metres", 50000),
    #     "Two Miles": ("Middle Distance", "Metres", 3218),
    #     "Shot Put": ("Throwing", "Metres", None),
    #     "110 Metres Hurdles": ("Sprint", "Metres", 110),
    #     "5 Kilometres": ("Road Running", "Metres", 5000),
    #     "Long Jump": ("Jumping", "Metres", None),
    #     "Pole Vault": ("Jumping", "Metres", None),
    #     "15 Kilometres": ("Road Running", "Metres", 15000),
    #     "Hammer Throw": ("Throwing", "Metres", None),
    #     "10 Kilometres": ("Road Running", "Metres", 10000),
    #     "Decathlon": ("Multi-events", "Points", None),
    #     "5000 Metres Race Walk": ("Race Walking", "Metres", 5000),
    #     "300 Metres": ("Sprint", "Metres", 300),
    #     "High Jump": ("Jumping", "Metres", None),
    #     "100 Metres": ("Sprint", "Metres", 100),
    #     "20000 Metres Race Walk": ("Race Walking", "Metres", 20000),
    #     "Half Marathon": ("Road Running", "Metres", 21097),
    #     "400 Metres": ("Sprint", "Metres", 400),
    #     "200 Metres": ("Sprint", "Metres", 200),
    #     "10000 Metres": ("Long Distance", "Metres", 10000),
    #     "1500 Metres": ("Middle Distance", "Metres", 1500),
    #     "Marathon": ("Road Running", "Metres", 42195),
    #     "10 Kilometres Race Walk": ("Race Walking", "Metres", 10000),
    #     "3000 Metres Race Walk": ("Race Walking", "Metres", 3000),
    # }

    # @dataclasses.dataclass
    # class EventInfo:
    #     event_type: str
    #     unit: str
    #     distance: int
    #     on_track: bool
    #     on_road: bool
    #     is_running: bool
    #     is_walking: bool
    #     performance: str

    # updated_info = {}
    # for event, details in info.items():
    #     # Determine the boolean attributes based on the event details
    #     on_track = (
    #         "Race Walk" not in event
    #         and "Road" not in event
    #         and "Kilometres" not in event
    #         and "Marathon" not in event
    #     )
    #     on_road = "Road" in event or "Marathon" in event
    #     is_running = (
    #         "Race Walk" not in event
    #         and "Throw" not in event
    #         and "Jump" not in event
    #         and "Heptathlon" not in event
    #         and "Decathlon" not in event
    #         and "Pole" not in event
    #         and "Shot" not in event
    #     )
    #     is_walking = "Race Walk" in event
    #     # Determine the performance measure based on the event type
    #     performance = (
    #         "lower is better" if details[1] == "Metres" else "higher is better"
    #     )
    #     # Create a new EventInfo instance
    #     updated_info[event] = EventInfo(
    #         details[0],
    #         details[1],
    #         details[2],
    #         on_track,
    #         on_road,
    #         is_running,
    #         is_walking,
    #         performance,
    #     )

    # df = df.with_columns(
    #     pl.col("Event")
    #     .apply(lambda e: updated_info[str(e)].event_type)
    #     .alias("Event Type"),
    #     pl.col("Event").apply(lambda e: updated_info[str(e)].unit).alias("Event Unit"),
    #     pl.col("Event")
    #     .apply(lambda e: updated_info[str(e)].distance)
    #     .alias("Event Distance"),
    #     pl.col("Event")
    #     .apply(lambda e: updated_info[str(e)].on_track)
    #     .alias("On Track"),
    #     pl.col("Event").apply(lambda e: updated_info[str(e)].on_road).alias("On Road"),
    #     pl.col("Event")
    #     .apply(lambda e: updated_info[str(e)].is_running)
    #     .alias("Is Running"),
    #     pl.col("Event")
    #     .apply(lambda e: updated_info[str(e)].is_walking)
    #     .alias("Is Walking"),
    #     pl.col("Event")
    #     .apply(lambda e: updated_info[str(e)].performance)
    #     .alias("Performance"),
    # )

    # df = df.with_columns(
    #     (pl.col("Mark") / pl.col("Mark").first())
    #     .over("Event", "Sex")
    #     .alias("Relative Mark")
    # )
    # df = df.drop("")
    df.write_parquet("./data/data.parquet")
    df.write_csv("./data/data.csv", separator=";")
    # df.write_csv("./data/data.csv", separator=";")


if __name__ == "__main__":
    postprocess_step1()
    postprocess_step2()

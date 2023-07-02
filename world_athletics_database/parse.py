import json
from multiprocessing import Pool

import pandas as pd

from world_athletics_database import logger


def parse_event(event, sex):
    logger.info(event)
    page = 0
    df_list = []
    while True:
        page += 1
        url = f"""https://worldathletics.org/records/all-time-toplists/sprints/{event}/outdoor/{sex}/senior?regionType=world&timing=electronic&windReading=regular&page={page}&bestResultsOnly=false&firstDay=1900-01-01&lastDay=2023-07-01"""
        try:
            df = pd.read_html(url)
            df_list.append(df[0])
        except Exception:
            logger.info(len(df_list))
            df = pd.concat(df_list)
            df.to_csv(f"data/{sex}/{event}.csv")
            logger.info(f"Written {event} to csv")
            break


def parse_event_men(event):
    parse_event(event, "men")


def parse_event_women(event):
    parse_event(event, "women")


if __name__ == "__main__":
    with open("data/options.json") as f:
        data = json.load(f)

    events_male = data[7]["cases"][0]["values"]
    event_male_urls = [ev["disciplineNameUrlSlug"] for ev in events_male]
    # with Pool(8) as p:
    #     print(p.map(parse_event_men, event_male_urls))
    events_female = data[7]["cases"][24]["values"]
    event_female_urls = [ev["disciplineNameUrlSlug"] for ev in events_female]
    with Pool(8) as p:
        print(p.map(parse_event_women, event_female_urls))

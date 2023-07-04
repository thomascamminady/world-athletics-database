# World Athletics Database

Some 400k athlete performances for various events scraped from [World Athletics](https://worldathletics.org/records/all-time-toplists/sprints/100-metres/outdoor/women/senior).

Get the data using `pandas`

```python
import pandas as pd

pd.read_csv(
    "https://raw.githubusercontent.com/thomascamminady/world-athletics-database/main/data/data.csv",
    delimiter=";",
    parse_dates=True
)
```

See https://world-athletics-database.camminady.dev/ for more

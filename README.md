# World Athletics Database
Some 400k athlete performances for various events scraped from https://worldathletics.org.

## TL;DR

Get the data using `pandas`
```python
import pandas as pd

pd.read_csv(
    "https://raw.githubusercontent.com/thomascamminady/world-athletics-database/main/data/data.csv",
    delimiter=";",
)
```


## Getting Started

First, clone the repository and navigate to the project directory. Then, install the necessary dependencies:

```bash
make init
```

Next, you can parse and post-process the data:

```python
poetry run python world_athletics_database/parse.py
poetry run python world_athletics_database/postprocess.py
```

**Note:** Parsing the data may take up to 20 minutes.

## Data Dictionary

- **Rank**: The rank of the record.
- **Mark**: The mark or result of the event.
- **Competitor**: The name of the competitor.
- **DOB**: The date of birth of the competitor.
- **Nat**: The nationality of the competitor.
- **Pos**: The position of the competitor.
- **Venue**: The venue where the event took place.
- **Date**: The date when the record was made.
- **Results Score**: The score of the results.
- **Mark [metres or seconds]**: The mark of the event in metres or seconds.
- **Event**: The name of the event.
- **Wind**: The wind speed during the event.
- **Sex**: The competitor's sex.

## Data Sample

Here's all the world record performances that are stored in the data set.

|    |   Rank | Mark       | Competitor               | DOB                 | Nat   | Pos   | Venue                                          | Date                |   Results Score |   Mark [meters or seconds] | Event                    |   Wind | Sex    |
|---:|-------:|:-----------|:-------------------------|:--------------------|:------|:------|:-----------------------------------------------|:--------------------|----------------:|---------------------------:|:-------------------------|-------:|:-------|
|  0 |      1 | 2:03:06    | Daniel BAUTISTA          | 1952-08-04 00:00:00 | MEX   | 1     | Cherkassy (URS)                                | 1980-04-27 00:00:00 |            1227 |                     7386   | 30 Kilometres Race Walk  |  nan   | male   |
|  1 |      1 | 1:53.28    | Jarmila KRATOCHVÍLOVÁ    | 1951-01-26 00:00:00 | TCH   | 1     | München (GER)                                  | 1983-07-26 00:00:00 |            1286 |                      113.2 | 800 Metres               |  nan   | female |
|  2 |      1 | 47.6       | Marita KOCH              | 1957-02-18 00:00:00 | GDR   | 1     | Bruce Stadium, Canberra (AUS)                  | 1985-10-06 00:00:00 |            1304 |                       47   | 400 Metres               |  nan   | female |
|  3 |      1 | 1:12.81    | Johnny GRAY              | 1960-06-19 00:00:00 | USA   | 1     | Santa Monica, CA (USA)                         | 1986-05-24 00:00:00 |            1239 |                       72.8 | 600 Metres               |  nan   | male   |
|  4 |      1 | 74.08      | Jürgen SCHULT            | 1960-05-11 00:00:00 | GDR   | 1     | Neubrandenburg (GDR)                           | 1986-06-06 00:00:00 |            1320 |                       74   | Discus Throw             |  nan   | male   |
|  5 |      1 | 86.74      | Yuriy SEDYKH             | 1955-06-11 00:00:00 | URS   | 1     | Neckarstadion, Stuttgart (GER)                 | 1986-08-30 00:00:00 |            1307 |                       86.7 | Hammer Throw             |  nan   | male   |
|  6 |      1 | 22.63      | Natalya LISOVSKAYA       | 1962-07-16 00:00:00 | URS   | 1.0   | Moskva (URS)                                   | 1987-06-07 00:00:00 |            1372 |                       22.6 | Shot Put                 |  nan   | female |
|  7 |      1 | 2.09       | Stefka KOSTADINOVA       | 1965-03-25 00:00:00 | BUL   | 1     | Stadio Olimpico, Roma (ITA)                    | 1987-08-30 00:00:00 |            1309 |                        2   | High Jump                |  nan   | female |
|  8 |      1 | 7.52       | Galina CHISTYAKOVA       | 1962-07-26 00:00:00 | URS   | 1     | Leningrad (URS)                                | 1988-06-11 00:00:00 |            1333 |                        7.5 | Long Jump                |    1.4 | female |
|  9 |      1 | 76.8       | Gabriele REINSCH         | 1963-09-23 00:00:00 | GDR   | 1.0   | Neubrandenburg (GDR)                           | 1988-07-09 00:00:00 |            1382 |                       76   | Discus Throw             |  nan   | female |
| 10 |      1 | 10.49      | Florence GRIFFITH-JOYNER | 1959-12-21 00:00:00 | USA   | 1qf1  | Indianapolis, IN (USA)                         | 1988-07-16 00:00:00 |            1314 |                       10.4 | 100 Metres               |    0   | female |
| 11 |      1 | 7291       | Jackie JOYNER-KERSEE     | 1962-03-03 00:00:00 | USA   | 1     | Olympic Stadium, Jamsil, Seoul (KOR)           | 1988-09-24 00:00:00 |            1331 |                     7291   | Heptathlon               |  nan   | female |
| 12 |      1 | 21.34      | Florence GRIFFITH-JOYNER | 1959-12-21 00:00:00 | USA   | 1     | Olympic Stadium, Jamsil, Seoul (KOR)           | 1988-09-29 00:00:00 |            1308 |                       21.3 | 200 Metres               |    1.3 | female |
| 13 |      1 | 18:21      | Robert KORZENIOWSKI      | 1968-07-30 00:00:00 | POL   |       | Bad Salzdefürth (GER)                          | 1990-09-15 00:00:00 |            1194 |                     1101   | 5 Kilometres Race Walk   |  nan   | male   |
| 14 |      1 | 8.95       | Mike POWELL              | 1963-11-10 00:00:00 | USA   | 1     | National Stadium, Tokyo (JPN)                  | 1991-08-30 00:00:00 |            1346 |                        8.9 | Long Jump                |    0.3 | male   |
| 15 |      1 | 2.45       | Javier SOTOMAYOR         | 1967-10-13 00:00:00 | CUB   | 1     | Salamanca (ESP)                                | 1993-07-27 00:00:00 |            1314 |                        2.4 | High Jump                |  nan   | male   |
| 16 |      1 | 8:06.11    | Junxia WANG              | 1973-01-09 00:00:00 | CHN   | 1     | Beijing (CHN)                                  | 1993-09-13 00:00:00 |            1293 |                      486.1 | 3000 Metres              |  nan   | female |
| 17 |      1 | 41:37.9h   | Hongmiao GAO             | 1974-03-17 00:00:00 | CHN   | 1     | Beijing (CHN)                                  | 1994-04-07 00:00:00 |            1207 |                     2497.9 | 10000 Metres Race Walk   |  nan   | female |
| 18 |      1 | 1:17:25.6h | Bernardo SEGURA          | 1970-02-11 00:00:00 | MEX   | 1     | Fana (NOR)                                     | 1994-05-07 00:00:00 |            1247 |                     4645.6 | 20000 Metres Race Walk   |  nan   | male   |
| 19 |      1 | 18.29      | Jonathan EDWARDS         | 1966-05-10 00:00:00 | GBR   | 1.0   | Ullevi Stadium, Göteborg (SWE)                 | 1995-08-07 00:00:00 |            1303 |                       18.2 | Triple Jump              |    1.3 | male   |
| 20 |      1 | 41:04      | Yelena NIKOLAYEVA        | 1966-02-01 00:00:00 | RUS   | 1.0   | Sochi (RUS)                                    | 1996-04-20 00:00:00 |            1228 |                     2464   | 10 Kilometres Race Walk  |  nan   | female |
| 21 |      1 | 98.48      | Jan ŽELEZNÝ              | 1966-06-16 00:00:00 | CZE   | 1     | Jena (GER)                                     | 1996-05-25 00:00:00 |            1365 |                       98.4 | Javelin Throw            |  nan   | male   |
| 22 |      1 | 2:28.98    | Svetlana MASTERKOVA      | 1968-01-17 00:00:00 | RUS   | 1     | Bruxelles (BEL)                                | 1996-08-23 00:00:00 |            1251 |                      148.9 | 1000 Metres              |  nan   | female |
| 23 |      1 | 7:20.67    | Daniel KOMEN             | 1976-05-17 00:00:00 | KEN   | 1     | Rieti (ITA)                                    | 1996-09-01 00:00:00 |            1299 |                      440.6 | 3000 Metres              |  nan   | male   |
| 24 |      1 | 18:05.49   | Hatem GHOULA             | 1973-06-07 00:00:00 | TUN   | 1     | Tunis (TUN)                                    | 1997-05-01 00:00:00 |            1217 |                     1085.4 | 5000 Metres Race Walk    |  nan   | male   |
| 25 |      1 | 3:26.00    | Hicham EL GUERROUJ       | 1974-09-14 00:00:00 | MAR   | 1     | Stadio Olimpico, Roma (ITA)                    | 1998-07-14 00:00:00 |            1302 |                      206   | 1500 Metres              |  nan   | male   |
| 26 |      1 | 11:41.85   | Norica CÎMPEAN           | 1972-03-22 00:00:00 | ROU   | 1     | Bucureşti (ROU)                                | 1999-02-06 00:00:00 |            1199 |                      701.8 | 3000 Metres Race Walk    |  nan   | female |
| 27 |      1 | 3:43.13    | Hicham EL GUERROUJ       | 1974-09-14 00:00:00 | MAR   | 1     | Stadio Olimpico, Roma (ITA)                    | 1999-07-07 00:00:00 |            1292 |                      223.1 | One Mile                 |  nan   | male   |
| 28 |      1 | 2:11.96    | Noah NGENY               | 1978-11-02 00:00:00 | KEN   | 1     | Rieti (ITA)                                    | 1999-09-05 00:00:00 |            1250 |                      131.9 | 1000 Metres              |  nan   | male   |
| 29 |      1 | 4:44.79    | Hicham EL GUERROUJ       | 1974-09-14 00:00:00 | MAR   | 1.0   | Olympiastadion, Berlin (GER)                   | 1999-09-07 00:00:00 |            1290 |                      284.7 | 2000 Metres              |  nan   | male   |
| 30 |      1 | 37:11      | Roman RASSKAZOV          | 1979-04-28 00:00:00 | RUS   | 1     | Saransk (RUS)                                  | 2000-05-28 00:00:00 |            1252 |                     2231   | 10 Kilometres Race Walk  |  nan   | male   |
| 31 |      1 | 1:26:52.3h | Olimpiada IVANOVA        | 1970-08-29 00:00:00 | RUS   | 1     | Brisbane (AUS)                                 | 2001-09-06 00:00:00 |            1193 |                     5212.3 | 20000 Metres Race Walk   |  nan   | female |
| 32 |      1 | 2:21:31    | Vladimir KANAYKIN        | 1985-03-21 00:00:00 | RUS   | 1.0   | Adler, Sochi (RUS)                             | 2006-02-19 00:00:00 |            1257 |                     8491   | 35 Kilometres Race Walk  |  nan   | male   |
| 33 |      1 | 19:46      | Kjersti TYSSE-PLÄTZER    | 1972-01-18 00:00:00 | NOR   | 1     | Hildesheim (GER)                               | 2006-08-27 00:00:00 |            1239 |                     1186   | 5 Kilometres Race Walk   |  nan   | female |
| 34 |      1 | 8:58.58    | Meseret DEFAR            | 1983-11-19 00:00:00 | ETH   | 1.0   | Boudewijnstadion, Bruxelles (BEL)              | 2007-09-14 00:00:00 |            1238 |                      538.5 | Two Miles                |  nan   | female |
| 35 |      1 | 72.28      | Barbora ŠPOTÁKOVÁ        | 1981-06-30 00:00:00 | CZE   | 1     | Gottlieb-Daimler Stadion, Stuttgart (GER)      | 2008-09-13 00:00:00 |            1306 |                       72.2 | Javelin Throw            |  nan   | female |
| 36 |      1 | 9.58       | Usain BOLT               | 1986-08-21 00:00:00 | JAM   | 1     | Olympiastadion, Berlin (GER)                   | 2009-08-16 00:00:00 |            1356 |                        9.5 | 100 Metres               |    0.9 | male   |
| 37 |      1 | 19.19      | Usain BOLT               | 1986-08-21 00:00:00 | JAM   | 1     | Olympiastadion, Berlin (GER)                   | 2009-08-20 00:00:00 |            1352 |                       19.1 | 200 Metres               |   -0.3 | male   |
| 38 |      1 | 5.06       | Yelena ISINBAYEVA        | 1982-06-03 00:00:00 | RUS   | 1     | Letzigrund, Zürich (SUI)                       | 2009-08-28 00:00:00 |            1290 |                        5   | Pole Vault               |  nan   | female |
| 39 |      1 | 55:21      | Zersenay TADESE          | 1982-01-01 00:00:00 | ERI   |       | Lisboa (POR)                                   | 2010-03-21 00:00:00 |            1241 |                     3321   | 20 Kilometres            |  nan   | male   |
| 40 |      1 | 5:10.68    | Mahiedine MEKHISSI       | 1985-03-15 00:00:00 | FRA   | 1     | Reims (FRA)                                    | 2010-06-30 00:00:00 |            1248 |                      310.6 | 2000 Metres Steeplechase |  nan   | male   |
| 41 |      1 | 1:40.91    | David RUDISHA            | 1988-12-17 00:00:00 | KEN   | 1     | Olympic Stadium, London (GBR)                  | 2012-08-09 00:00:00 |            1301 |                      100.9 | 800 Metres               |  nan   | male   |
| 42 |      1 | 12.8       | Aries MERRITT            | 1985-07-24 00:00:00 | USA   | 1     | Boudewijnstadion, Bruxelles (BEL)              | 2012-09-07 00:00:00 |            1294 |                       12   | 110 Metres Hurdles       |    0.3 | male   |
| 43 |      1 | 20:01.80   | Eleonora Anna GIORGI     | 1989-09-14 00:00:00 | ITA   | 1     | Misterbianco (ITA)                             | 2014-05-18 00:00:00 |            1219 |                     1201.8 | 5000 Metres Race Walk    |  nan   | female |
| 44 |      1 | 3:32:33    | Yohann DINIZ             | 1978-01-01 00:00:00 | FRA   | 1     | Letzigrund, Zürich (SUI)                       | 2014-08-15 00:00:00 |            1269 |                    12753   | 50 Kilometres Race Walk  |  nan   | male   |
| 45 |      1 | 1:16:36    | Yusuke SUZUKI            | 1988-01-02 00:00:00 | JPN   | 1     | Nomi (JPN)                                     | 2015-03-15 00:00:00 |            1266 |                     4596   | 20 Kilometres Race Walk  |  nan   | male   |
| 46 |      1 | 43.03      | Wayde VAN NIEKERK        | 1992-07-15 00:00:00 | RSA   | 1     | Estádio Olímpico, Rio de Janeiro (BRA)         | 2016-08-14 00:00:00 |            1321 |                       43   | 400 Metres               |  nan   | male   |
| 47 |      1 | 82.98      | Anita WŁODARCZYK         | 1985-08-08 00:00:00 | POL   | 1     | Stadion PGE Narodowy, Warszawa (POL)           | 2016-08-28 00:00:00 |            1303 |                       82.9 | Hammer Throw             |  nan   | female |
| 48 |      1 | 1:01:25    | Joyciline JEPKOSGEI      | 1993-12-08 00:00:00 | KEN   |       | Praha (CZE)                                    | 2017-04-01 00:00:00 |            1237 |                     3685   | 20 Kilometres            |  nan   | female |
| 49 |      1 | 30.81      | Wayde VAN NIEKERK        | 1992-07-15 00:00:00 | RSA   | 1     | Mestský Stadion, Ostrava (CZE)                 | 2017-06-28 00:00:00 |            1274 |                       30.8 | 300 Metres               |  nan   | male   |
| 50 |      1 | 1:21.77    | Caster SEMENYA           | 1991-01-07 00:00:00 | RSA   | 1     | Olympiastadion, Berlin (GER)                   | 2017-08-27 00:00:00 |            1244 |                       81.7 | 600 Metres               |  nan   | female |
| 51 |      1 | 1:23:39    | Yelena LASHMANOVA        | 1992-04-09 00:00:00 | RUS   | 1     | Cheboksary (RUS)                               | 2018-06-09 00:00:00 |            1251 |                     5019   | 20 Kilometres Race Walk  |  nan   | female |
| 52 |      1 | 8:44.32    | Beatrice CHEPKOECH       | 1991-07-06 00:00:00 | KEN   | 1     | Stade Louis II, Monaco (MON)                   | 2018-07-20 00:00:00 |            1285 |                      524.3 | 3000 Metres Steeplechase |  nan   | female |
| 53 |      1 | 10:43.84   | Tom BOSWORTH             | 1990-01-17 00:00:00 | GBR   | 1.0   | Olympic Stadium, London (GBR)                  | 2018-07-21 00:00:00 |            1217 |                      643.8 | 3000 Metres Race Walk    |  nan   | male   |
| 54 |      1 | 9126       | Kevin MAYER              | 1992-02-10 00:00:00 | FRA   | 1     | Stade Pierre Paul Bernard, Talence (FRA)       | 2018-09-16 00:00:00 |            1302 |                     9126   | Decathlon                |  nan   | male   |
| 55 |      1 | 41:05      | Joshua CHEPTEGEI         | 1996-09-12 00:00:00 | UGA   | 1.0   | Nijmegen (NED)                                 | 2018-11-18 00:00:00 |            1248 |                     2465   | 15 Kilometres            |  nan   | male   |
| 56 |      1 | 34.41      | Shaunae MILLER-UIBO      | 1994-04-15 00:00:00 | BAH   | 1f1   | Mestský Stadion, Ostrava (CZE)                 | 2019-06-20 00:00:00 |            1269 |                       34.4 | 300 Metres               |  nan   | female |
| 57 |      1 | 4:12.33    | Sifan HASSAN             | 1993-01-01 00:00:00 | NED   | 1     | Stade Louis II, Monaco (MON)                   | 2019-07-12 00:00:00 |            1250 |                      252.3 | One Mile                 |  nan   | female |
| 58 |      1 | 5:52.80    | Gesa Felicitas KRAUSE    | 1992-08-03 00:00:00 | GER   | 1     | Olympiastadion, Berlin (GER)                   | 2019-09-01 00:00:00 |            1219 |                      352.8 | 2000 Metres Steeplechase |  nan   | female |
| 59 |      1 | 50:32      | Evaline CHIRCHIR         | 1998-02-02 00:00:00 | KEN   | 1     | Amsterdam (NED)                                | 2019-09-22 00:00:00 |            1190 |                     3032   | 10 Miles Road            |  nan   | female |
| 60 |      1 | 2:14:04    | Brigid KOSGEI            | 1994-02-20 00:00:00 | KEN   | 1     | Chicago, IL (USA)                              | 2019-10-13 00:00:00 |            1295 |                     8044   | Marathon                 |  nan   | female |
| 61 |      1 | 44:20      | Letesenbet GIDEY         | 1998-03-20 00:00:00 | ETH   | 1.0   | Nijmegen (NED)                                 | 2019-11-17 00:00:00 |            1274 |                     2660   | 15 Kilometres            |  nan   | female |
| 62 |      1 | 26:24      | Rhonex KIPRUTO           | 1999-10-12 00:00:00 | KEN   | 1     | Valencia (ESP)                                 | 2020-01-12 00:00:00 |            1285 |                     1584   | 10 Kilometres            |  nan   | male   |
| 63 |      1 | 12:35.36   | Joshua CHEPTEGEI         | 1996-09-12 00:00:00 | UGA   | 1     | Stade Louis II, Monaco (MON)                   | 2020-08-14 00:00:00 |            1302 |                      755.3 | 5000 Metres              |  nan   | male   |
| 64 |      1 | 3:50:42    | Yelena LASHMANOVA        | 1992-04-09 00:00:00 | RUS   | 1.0   | Voronovo (RUS)                                 | 2020-09-05 00:00:00 |            1295 |                    13842   | 50 Kilometres Race Walk  |  nan   | female |
| 65 |      1 | 26:11.00   | Joshua CHEPTEGEI         | 1996-09-12 00:00:00 | UGA   | 1     | Estadio de Atletismo del Turia, Valencia (ESP) | 2020-10-07 00:00:00 |            1306 |                     1571   | 10000 Metres             |  nan   | male   |
| 66 |      1 | 37:25.21   | Eiki TAKAHASHI           | 1992-11-19 00:00:00 | JPN   | 1.0   | Juntendo University Stadium, Inzai (JPN)       | 2020-11-14 00:00:00 |            1241 |                     2245.2 | 10000 Metres Race Walk   |  nan   | male   |
| 67 |      1 | 29:01.03   | Letesenbet GIDEY         | 1998-03-20 00:00:00 | ETH   | 1     | FBK Stadium, Hengelo (NED)                     | 2021-06-08 00:00:00 |            1303 |                     1741   | 10000 Metres             |  nan   | female |
| 68 |      1 | 15.67      | Yulimar ROJAS            | 1995-10-21 00:00:00 | VEN   | 1     | National Stadium, Tokyo (JPN)                  | 2021-08-01 00:00:00 |            1290 |                       15.6 | Triple Jump              |    0.7 | female |
| 69 |      1 | 45.94      | Karsten WARHOLM          | 1996-02-28 00:00:00 | NOR   | 1     | National Stadium, Tokyo (JPN)                  | 2021-08-03 00:00:00 |            1341 |                       45.9 | 400 Metres Hurdles       |  nan   | male   |
| 70 |      1 | 5:21.56    | Francine NIYONSABA       | 1993-05-05 00:00:00 | BDI   | 1.0   | Sports Park Mladost, Zagreb (CRO)              | 2021-09-14 00:00:00 |            1241 |                      321.5 | 2000 Metres              |  nan   | female |
| 71 |      1 | 1:02:52    | Letesenbet GIDEY         | 1998-03-20 00:00:00 | ETH   | 1     | Valencia (ESP)                                 | 2021-10-24 00:00:00 |            1281 |                     3772   | Half Marathon            |  nan   | female |
| 72 |      1 | 57:31      | Jacob KIPLIMO            | 2000-11-14 00:00:00 | UGA   | 1     | Lisboa (POR)                                   | 2021-11-21 00:00:00 |            1288 |                     3451   | Half Marathon            |  nan   | male   |
| 73 |      1 | 12:49      | Berihu AREGAWI           | 2001-02-28 00:00:00 | ETH   | 1.0   | Barcelona (ESP)                                | 2021-12-31 00:00:00 |            1250 |                      769   | 5 Kilometres             |  nan   | male   |
| 74 |      1 | 14:19      | Ejgayehu TAYE            | 2000-02-10 00:00:00 | ETH   | 1     | Barcelona (ESP)                                | 2021-12-31 00:00:00 |            1244 |                      859   | 5 Kilometres             |  nan   | female |
| 75 |      1 | 29:14      | Yalemzerf YEHUALAW       | 1999-08-03 00:00:00 | ETH   | 1     | Castellón (ESP)                                | 2022-02-27 00:00:00 |            1290 |                     1754   | 10 Kilometres            |  nan   | female |
| 76 |      1 | 50.68      | Sydney MCLAUGHLIN        | 1999-08-07 00:00:00 | USA   | 1     | Hayward Field, Eugene, OR (USA)                | 2022-07-22 00:00:00 |            1312 |                       50.6 | 400 Metres Hurdles       |  nan   | female |
| 77 |      1 | 6.21       | Armand DUPLANTIS         | 1999-11-10 00:00:00 | SWE   | 1     | Hayward Field, Eugene, OR (USA)                | 2022-07-24 00:00:00 |            1325 |                        6.2 | Pole Vault               |  nan   | male   |
| 78 |      1 | 12.12      | Tobi AMUSAN              | 1997-04-23 00:00:00 | NGR   | 1sf1  | Hayward Field, Eugene, OR (USA)                | 2022-07-24 00:00:00 |            1272 |                       12.1 | 100 Metres Hurdles       |    0.9 | female |
| 79 |      1 | 2:01:09    | Eliud KIPCHOGE           | 1984-11-05 00:00:00 | KEN   | 1     | Berlin (GER)                                   | 2022-09-25 00:00:00 |            1312 |                     7269   | Marathon                 |  nan   | male   |
| 80 |      1 | 44:04      | Benard KIBET             | 1999-11-25 00:00:00 | KEN   | 1     | Kosa (JPN)                                     | 2022-12-04 00:00:00 |            1257 |                     2644   | 10 Miles Road            |  nan   | male   |
| 81 |      1 | 2:37:11    | Klavdiya AFANASYEVA      | 1996-01-15 00:00:00 | RUS   | 1.0   | Saransk (RUS)                                  | 2023-05-20 00:00:00 |            1263 |                     9431   | 35 Kilometres Race Walk  |  nan   | female |
| 82 |      1 | 23.56      | Ryan CROUSER             | 1992-12-18 00:00:00 | USA   | 1     | Drake Stadium, Los Angeles, CA (USA)           | 2023-05-27 00:00:00 |            1334 |                       23.5 | Shot Put                 |  nan   | male   |
| 83 |      1 | 3:49.11    | Faith KIPYEGON           | 1994-01-10 00:00:00 | KEN   | 1     | Stadio Luigi Ridolfi, Firenze (ITA)            | 2023-06-02 00:00:00 |            1295 |                      229.1 | 1500 Metres              |  nan   | female |
| 84 |      1 | 7:52.11    | Lamecha GIRMA            | 2000-11-26 00:00:00 | ETH   | 1     | Stade Charléty, Paris (FRA)                    | 2023-06-09 00:00:00 |            1295 |                      472.1 | 3000 Metres Steeplechase |  nan   | male   |
| 85 |      1 | 7:54.10    | Jakob INGEBRIGTSEN       | 2000-09-19 00:00:00 | NOR   | 1     | Stade Charléty, Paris (FRA)                    | 2023-06-09 00:00:00 |            1304 |                      474.1 | Two Miles                |  nan   | male   |
| 86 |      1 | 14:05.20   | Faith KIPYEGON           | 1994-01-10 00:00:00 | KEN   | 1     | Stade Charléty, Paris (FRA)                    | 2023-06-09 00:00:00 |            1272 |                      845.2 | 5000 Metres              |  nan   | female |

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and [thomascamminady/cookiecutter-pypackage](https://github.com/thomascamminady/cookiecutter-pypackage), a fork of the [audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage) project template.

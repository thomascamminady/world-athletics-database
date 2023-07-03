========================
World Athletics Database
========================


This is a dataset consisting of the world records in athletics. The data contains details about each record such as rank, mark, competitor's name, date of birth, nationality, position, venue, date of the record, results score, mark in metres or seconds, event, wind speed during the event, and the sex of the competitor.


.. code-block:: bash

   poetry run python world_athletics_database/parse.py # takes 20 minutes
   poetry run python world_athletics_database/postprocess.py # fast






Data Dictionary
-------------------

* **Rank**: The rank of the record.
* **Mark**: The mark or result of the event.
* **Competitor**: The name of the competitor.
* **DOB**: The date of birth of the competitor.
* **Nat**: The nationality of the competitor.
* **Pos**: The position of the competitor.
* **Venue**: The venue where the event took place.
* **Date**: The date when the record was made.
* **Results Score**: The score of the results.
* **Mark [metres or seconds]**: The mark of the event in metres or seconds.
* **Event**: The name of the event.
* **Wind**: The wind speed during the event.
* **Sex**: The sex of the competitor.

Data Sample
----------------
Here is a sample of the dataset:


======================  =========  ===================  ==========  ===  =====  ===============================  ==========  ==============  =======================  ====================  ====  ======
Rank                    Mark       Competitor           DOB         Nat  Pos    Venue                           Date        Results Score   Mark [metres or seconds]  Event                Wind  Sex  
======================  =========  ===================  ==========  ===  =====  ===============================  ==========  ==============  =======================  ====================  ====  ======
1                       2:03:06    Daniel BAUTISTA      1952-08-04  MEX  1      Cherkassy (URS)                 1980-04-27  1227            7386.0                    30 Kilometres Race Walk  NaN  male  
1                       1:53.28    Jarmila KRATOCHVÍLOVÁ1951-01-26  TCH  1      München (GER)                   1983-07-26  1286            113.2                     800 Metres              NaN  female
1                       47.6       Marita KOCH          1957-02-18  GDR  1      Bruce Stadium, Canberra (AUS)  1985-10-06  1304            47.0                      400 Metres              NaN  female
======================  =========  ===================  ==========  ===  =====  ===============================  ==========  ==============  =======================  ====================  ====  ======

**Note**: The full dataset contains much more data.


Development
--------
To set up the project, simply run

.. code-block:: bash

   make init


Credits
-------

This package was created with Cookiecutter_ and `thomascamminady/cookiecutter-pypackage`_, a fork of the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`thomascamminady/cookiecutter-pypackage`: https://github.com/thomascamminady/cookiecutter-pypackage
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

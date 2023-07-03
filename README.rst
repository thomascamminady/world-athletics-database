========================
World Athletics Database
========================

.. code-block:: bash

   poetry run python world_athletics_database/parse.py # takes 20 minutes
   poetry run python world_athletics_database/postprocess.py # fast




Data
--------

.. csv-table:: Table Title
   :file: data/worldrecords.csv
   :widths: 30, 70
   :header-rows: 1

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

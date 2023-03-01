# sqlalchemy-challenge
Module 10 Challenge

This challenge includes analysis of climate or weather data related to Honolulu, Hawaii.


Included in SurfsUp directory:
1. 'climate_starter.ipynb':
- In climate_starter.ipynb we undertake both precipitation analysis and weather station analysis.
- In the Precipitation Analysis we analyse and present precipitation data for the last 12 months in both a pandas dataframe and in a matplotlib plot.
- In the Station Analysis we analyse the activity of each station, gather min, max and average temperature data from the most active station, and then display this temperature data using a histogram.

2. 'app.py':
- In app.py were have created a Flask API to allow the user to investigate the following in the given dataset (see 'Resources/'):
    - Precipitation by date
    - List of weather stations
    - Temperature by date
    - Min, max, and average temperature by specified date range (using a start date only or a start and end date).
    - NOTE: when querying temperature data using the specified date range URL, ensure dates are in YYYYMMDD format.

3. 'Resources/':
- Included in the Resources directory is:
    - 'hawaii.sqlite' - the database from which all queries were drawn to drive the aforementioned analysis about dates, stations, precipitation and temperature observations.
    - 'hawaii_measurements.csv' - a csv file that includes dates, stations, precipitation and temperature observations from the various weather stations.
    - 'hawaii_stations.csv' - a csv file that includes details about the weather stations in the dataset, namely the station code, station name, longitude, latitude and elevation.
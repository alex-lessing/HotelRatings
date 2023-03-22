# Overview
The city of Munich built six stations to measure bike traffic and weather conditions at different locations. 

This data is taken from https://www.kaggle.com/datasets/lucafrance/bike-traffic-in-munich via an API call.

The data is provided monthly as follows:

- traffic data for each station in 15 minutes intervals,
- daily weather and traffic data for each station,
- list of measuring stations with coordinates.
This dataset provides all available data consolidated starting from the first month available (January 2017).

## Content
The data is split in three files. Some columns are shared.

```rad_15min.csv```: Traffic data at different stations divided in 15 minutes intervals. 

```rad_tage.csv:``` The same data as in rad_15min.csv summed by day with additional weather information.

```radzaehlstellen.csv:``` Detailed information about the measuring stations (in German).
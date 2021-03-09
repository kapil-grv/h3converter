# Convert H3 spatial index

A little about H3:
H3 Geospatial Indexing System by UBER
Installation of H3 library and other details of H3 could be found in this Git Repo - https://github.com/uber/h3

-----

This package helps you convert h3 hec code directly to geojson and a GeoJSON entity to h3 hex code.

Sample:

H3 to GeoJSON:

`from h3converter import h3converter`

`h3converter.h3_to_geojson(['89be455030bffff','89be455030cffff'])`

GeoJSON to H3:

`from h3converter import h3converter`

`h3converter.polyfill({'type':'Polygon','coordinates':[[[144.244589, -36.810689], [144.244246, -36.808741], [144.241989, -36.807999], [144.240075, -36.809205], [144.240418, -36.811153], [144.242676, -36.811895], [144.244589, -36.810689]]]},9)`

where polyfill has (geojson, precision).


Sample Images of H3 (Resolution 12 and 13)

![Test Image 4](https://github.com/kapil-grv/H3/blob/master/H3-lv12_13_sample.png)

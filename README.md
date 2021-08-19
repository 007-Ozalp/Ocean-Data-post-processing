# Ocean-Data-Post-Processing

[AdriaClim Project](https://www.italy-croatia.eu/web/adriaclim): Climate change information, monitoring, and management tools for adaptation strategies in Adriatic coastal areas.

Therefore, in [Ocean-Data-Processing](https://github.com/007-Ozalp/Ocean-Data-post-processing) you will find some examples of how the climate model data is post-processed in the Adriatic Sea in the field of Climate, Ocean, and Coastal Areas.

CMEMS-Data examples:

You can download an Ocean Product from [CMEMS](https://resources.marine.copernicus.eu/?option=com_csw&view=order&record_id=eec7a997-c57e-4dfa-9194-4c72154f5cc5):
Then you can use the following Jupyter notebooks to manipulate the files (or download the ocean_data.nc):

.["interpolation.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing-xarray-graphs/blob/main/interpolation.ipynb) explaines how to do a Vertical profile interpolation for selected levels with using [numpy.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html) function.

.["temperature_by_depth.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing-xarray-graphs/blob/main/temperature_by_depth.ipynb) shows a graph to see the Vertical Profondity in the ocean_data.nc file through [xarray](http://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) function.

. [Mediterranean_Sea_Physics_Analysis_and_Forecast_Ocean_Product_Temperature_at5m.png](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/Mediterranean_Sea_Physics_Analysis_and_Forecast_Ocean_Product_Temperature_at5m.png) is the result of the GeoCAT visualization example through [cmems_Geocat_visualization_temperature.py](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/cmems_Geocat_visualization_temperature.py) 
by reading [2020-11 16T12_00_00_Daily_temp_2020_AdriaticSea_Z10_CF.nc](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/2020-11-16T12_00_00_Daily_temp_2020_AdriaticSea_Z10_CF.nc) CMEMS Ocean Product. 

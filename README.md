  # CMEMS Ocean Data

[AdriaClim Project](https://www.italy-croatia.eu/web/adriaclim): Climate change information, monitoring, and management tools for adaptation strategies in Adriatic coastal areas.

Therefore, in [Ocean-Data-Processing](https://github.com/007-Ozalp/Ocean-Data-post-processing) you will find some examples of how the climate model data is post-processed in the Adriatic Sea in the field of Climate, Ocean, and Coastal Areas.

  # Data post-processing:

  You can download an Ocean Product from [CMEMS](https://resources.marine.copernicus.eu/?option=com_csw&task=results):
  Then you can use the following Jupyter notebooks to manipulate the files (or download the ocean_data.nc):

. ["interpolation.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing-xarray-graphs/blob/main/interpolation.ipynb) explaines how to do a Vertical profile interpolation for selected levels with using [numpy.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html) function.

. ["temperature_by_depth.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing-xarray-graphs/blob/main/temperature_by_depth.ipynb) shows a graph to see the Vertical Profondity in the ocean_data.nc file through [xarray](http://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) function.

. ["read_file_temperature.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/read_file_temperature.ipynb) describes the statistics of the [2020-11-16T12_00_00_Daily_temp_2020_AdriaticSea_Z10_CF.nc](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/2020-11-16T12_00_00_Daily_temp_2020_AdriaticSea_Z10_CF.nc) file.

  In the following scripts there are examples of  ocean data visualization by using [GeoCAT](https://geocat.ucar.edu/pages/software.html) module and [Cartography](https://pypi.org/project/cartography/) library.

  Reading file is : [2020-11-16T12_00_00_Daily_temp_2020_AdriaticSea_Z10_CF.nc](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/2020-11-16T12_00_00_Daily_temp_2020_AdriaticSea_Z10_CF.nc) post-processed [CMEMS](https://resources.marine.copernicus.eu/?option=com_csw&task=results) Ocean file. 

. ["Mediterranean_Sea_Physics_Analysis_and_Forecast_Ocean_Product_Temperature_at5m.png"](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/Mediterranean_Sea_Physics_Analysis_and_Forecast_Ocean_Product_Temperature_at5m.png) is the result of the [GeoCAT](https://geocat.ucar.edu/) visualization example through ["cmems_Geocat_visualization_temperature.py"](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/cmems_Geocat_visualization_temperature.py) 

. The  visualization by using Cartography library has been shown through ["cmems_cartography_visualization_temperature.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing/blob/main/cmems_cartography_visualization_temperature.ipynb) 


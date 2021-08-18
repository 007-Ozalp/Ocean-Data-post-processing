# Ocean-Data-Post-Processing-xarray

[AdriaClim Project](https://www.italy-croatia.eu/web/adriaclim): Climate change information, monitoring, and management tools for adaptation strategies in Adriatic coastal areas.

Therefore, in 007-Ozalp/Ocean-Data-Processing you will find some examples of how the climate model data is post-processed in the Adriatic Sea in the field of Climate, Ocean, and Coastal Areas.

CMEMS-Data examples:

You can download an Ocean Product from [CMEMS](https://resources.marine.copernicus.eu/?option=com_csw&view=order&record_id=eec7a997-c57e-4dfa-9194-4c72154f5cc5):
Then you can use the following Jupyter notebooks to manipulate the files (or download the ocean_data.nc):

.["interpolation.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing-xarray-graphs/blob/main/interpolation.ipynb) explaines how to do a Vertical profile interpolation for selected levels with using [numpy.interp](https://numpy.org/doc/stable/reference/generated/numpy.interp.html) function.

.["temperature_by_depth.ipynb"](https://github.com/007-Ozalp/Ocean-Data-post-processing-xarray-graphs/blob/main/temperature_by_depth.ipynb) shows a graph to see the Vertical Profondity in the ocean_data.nc file through [xarray](http://xarray.pydata.org/en/stable/generated/xarray.DataArray.html) function.

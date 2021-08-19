import numpy as np
import xarray as xr
import cartopy.feature as cfeature
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import os,sys
import pandas as pd
import geocat.datafiles as gdf
from geocat.viz import cmaps as gvcmaps
from geocat.viz import util as gvutil


##################################################################

# Read a netCDF data file using xarray default engine and load the data into xarrays

fn_temp = '2020-11-16T12:00:00_Daily_temp_2020_AdriaticSea_Z10_CF.nc'

nut_nc=[os.path.join(fn_temp) for f in fn_temp]

nut_ds=[xr.open_dataset(nc) for nc in nut_nc]
j=0

##################################################################

# Extract a slice of the data

t = nut_ds[j].thetao.isel(time=0,depth=0).sel(lat=slice(37, 46), lon=slice(12, 22))

##################################################################

fig = plt.figure(figsize=(10, 10), dpi=200)

##################################################################


#  coastlines, and adding features

m = plt.axes(projection=ccrs.PlateCarree())


land_resolution = '10m'
land_def = cfeature.NaturalEarthFeature('physical', 'land', land_resolution,
                                        edgecolor='k',
                                        facecolor=cfeature.COLORS['land'], color ='g')


states_provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='10m',
    facecolor='none')

boundry_lines = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_0_boundary_lines_land',
    scale='10m',
    facecolor='none')


##################################################################

m.add_feature(land_def,linewidth=0.5)
m.add_feature(cfeature.COASTLINE,linewidths=0.5,alpha=0.9999)
m.add_feature(cfeature.OCEAN,color='turquoise', linewidth=0.3)
m.add_feature(boundry_lines, edgecolor='k', linewidth=0.3)
m.add_feature(states_provinces, edgecolor='k', linewidth=0.3)
m.add_feature(cfeature.RIVERS,color='aqua',linewidth=0.7)
m.add_feature(cfeature.LAKES, color="b")

##################################################################


newcmp = gvcmaps.BlAqGrYeOrReVi200


# heat map creation based on temperature at given date and statistics

heatmap = t.plot.contourf(m=m,
                          levels=50,
                          vmin=11,
                          vmax=23,
                          cmap=newcmp,
                          add_colorbar=False)

##################################################################

#internal contour per Temperature
# alpha is the transparency value for each color levels(small islands contours= VMAX-VMIN)

lines=t.plot.contour(m=m,alpha=1,linewidths=0.3,colors = 'k',linestyles='None',levels=12)

##################################################################

#projection extent

m.set_extent([12, 22, 37, 46], crs=ccrs.PlateCarree())

##################################################################

cbar = plt.colorbar(heatmap, ticks=np.arange(11, 24, 1))


cbar.ax.set_yticklabels([str(i) for i in np.arange(11, 24, 1)])

##################################################################


# Set axes limits, and tick values

gvutil.set_axes_limits_and_ticks(m,
                                 xlim=(5, 26),
                                 ylim=(35, 48),
                                 xticks=np.linspace(5, 26, 3),
                                 yticks=np.linspace(35, 48, 3))

# Use geocat.viz.util convenience function to make plots 

gvutil.add_lat_lon_ticklabels(m)

# Use geocat.viz.util convenience function to add minor and major tick lines

gvutil.add_major_minor_ticks(m, labelsize=10)


##################################################################

# Use geocat.viz.util convenience function to set titles and labels 

gvutil.set_titles_and_labels(
    m,
    maintitle="MEDITERRANEAN SEA PHYSICS\nANALYSIS AND FORECAST\nOCEAN PRODUCT\nTemperature at 5 m",
    maintitlefontsize=16,
    lefttitle="16-November-2020",
    lefttitlefontsize=14,
    righttitle="T[degC]",
    righttitlefontsize=14,
    xlabel="",
    ylabel="")

m.xlabel_style = {'size': 16, 'color': 'k'}
m.ylabel_style = {'size': 16, 'color': 'k'}

##################################################################

plt.savefig('temperature_november_2020_at5.png')



plt.show()

"""
Compiles the hydrological database required for modelling streamflow based on
meteorological variables, using era5 data retrieval script and hydrological
data handling functions from the apollo library.

@author: robertrouse
"""

# Import cdsapi and create a Client instance
import xarray as xr
from apollo import era5 as er


### Specify meteorological variables and spatiotemporal ranges
area = ['60.00/-8.00/48.00/4.00']
yyyy = [str(y) for y in range(1979,1980,1)]
mm = [str(m) for m in range(1,13,1)]
dd = [str(d) for d in range(1,32,1)]
hh = [str(t).zfill(2) + ':00' for t in range(0, 24, 1)]
met = ['total_precipitation','temperature','u_component_of_wind',
       'v_component_of_wind','relative_humidity',
       'volumetric_soil_water_layer_1','volumetric_soil_water_layer_2',
       'volumetric_soil_water_layer_3','volumetric_soil_water_layer_4',]


### Download meteorological variable sets from Copernicus Data Store
for yy in yyyy:
    filename = 'Rainfall_' + str(yy)
    rain_query = er.query(filename, 'reanalysis-era5-single-levels', met[0],
                          area, yy, mm, dd, hh)
    rain_data = er.era5(rain_query).download()
    er.aggregate_mean(str(rain_query['file_stem']) + '.nc',
              str(rain_query['file_stem']) + '_aggregated.nc')
combined = xr.open_mfdataset('Rainfall_*_aggregated.nc', concat_dim='time')
combined.to_netcdf(path='Rainfall.nc')

pressure_query = er.query('Pressure','reanalysis-era5-pressure-levels',
                          met[1:5], area, yyyy, mm, dd, '12:00', ['1000'])
pressure_data = er.era5(pressure_query).download()

soil_query = er.query('Soil_Moisture','reanalysis-era5-land', met[5:],
                      area, yyyy, mm, dd, '12:00')
soil_data = er.era5(soil_query).download()
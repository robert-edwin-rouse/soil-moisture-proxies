"""
Variable names can be found in the api guide.

If variable is single level, then the product is "reanalysis-era5-single-levels"
and no pressure level field is required.  If variable is on a pressure level,
then the product is "reanalysis-era5-pressure-levels" and a pressure level
field is required.

For global data, no area field is required.  Otherwise, specify the required
area by latitude and longitude coordinates.

Recommend netcdf (.nc) format - easy to use with xarray for array manipulation.
Subsets can be saved to csv once read into python if needs be.

@author: robertrouse
"""

# Import cdsapi and create a Client instance
import cdsapi
import xarray as xr

c = cdsapi.Client()

### Variables
area = ['60.00/-8.00/48.00/4.00']
years = [str(y) for y in range(1979,2020,1)]
months = [str(m) for m in range(1,13,1)]
days = [str(d) for d in range(1,32,1)]

### Retrieve hourly precipitation data using for loop to reduce data burden
for year in years:
    filename1  = str("Hourly Rainfall " + str(year) + ".nc")
    filename2  = str("Daily Rainfall " + str(year) + ".nc")
    print(filename1)
    c.retrieve("reanalysis-era5-single-levels", {
            "product_type":   "reanalysis",
            "format":         "netcdf",
            "variable":       ["total_precipitation"],
            "area":           area,
            "year":           year,
            "month":          months,
            "day":            days,
            "time":           ['00:00','01:00','02:00','03:00','04:00','05:00',
                                '06:00','07:00','08:00','09:00','10:00','11:00',
                                '12:00','13:00','14:00','15:00','16:00','17:00',
                                '18:00','19:00','20:00','21:00','22:00','23:00']
        }, filename1)
    ds_nc = xr.open_dataset(filename1)
    daily_precipitation = ds_nc.tp.resample(time='24H').sum('time')*1000
    daily_precipitation.to_netcdf(filename2)

### Conversion from hourly to cummulative daily precipitation data
dataset = xr.open_dataset('Daily Rainfall ' + str(1979) + '.nc')
years = [x for x in range(1979,2020,1)]
for year in years:
    rh_file = 'Daily Rainfall ' + str(year) + '.nc'
    rh = xr.open_dataset(rh_file)
    dataset = xr.concat([dataset, rh],dim='time')
dataset.to_netcdf(path='Daily Precipitation Full.nc')

### Retrieve pressure level data
pressure_set = [1000,]
for p in pressure_set:
    filename = 'UK_ERA5_' + str(p) + 'hPa.nc'
    c.retrieve('reanalysis-era5-pressure-levels', {
            "product_type":   "reanalysis",
            "format":         "netcdf",
            "variable":       ['relative_humidity','temperature','u_component_of_wind',
                'v_component_of_wind'],
            "pressure_level": [str(p)],
            "area":           area,
            "year":           years,
            "month":          months,
            "day":            days,
            "time":           "12"
        }, filename)

### Retrieve pressure level data
c.retrieve('reanalysis-era5-land', {
        "format":         "netcdf",
        "variable":       ['volumetric_soil_water_layer_1','volumetric_soil_water_layer_2',
                            'volumetric_soil_water_layer_3','volumetric_soil_water_layer_4'],
            "area":           area,
            "year":           years,
            "month":          months,
            "day":            days,
        "time":           "12",
    }, "VSMa.nc")
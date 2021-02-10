NetCDF extraction util
----------------------

This is a simple script to extract time-series from a NetCDF file to a Comma Separated Value (CSV) file.

To use:

    netcdf_extraction_util.py <input_netcdf_file> <selected_reach>

This will produce a <selected_reach>.csv file with columns date and value for the selected reach. If the
reach does not exist on <input_netcdf_file>, there will be an error.



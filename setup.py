from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name="netcdf_extraction", version="0.1", 
      description="Script to extract time-series from Netcdf",
      long_description=readme(),
      author="Daniel Lagrava",
      author_email="daniel.lagravasandoval@niwa.co.nz",
      license="GNU",
      scripts=['bin/extract_time_series.py'],
      install_requires=['numpy','netCDF4','xarray'],
      include_pachage_data=True,
      zip_safe=False
)


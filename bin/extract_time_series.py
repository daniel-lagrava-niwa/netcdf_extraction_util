#!/usr/bin/env python

import xarray as xr
import numpy as np
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_nc", help="netcdf file containing the time-series")
    parser.add_argument("reach_id", help="reach id to extract", type=int)
    return parser.parse_args()

def main():
    args = parse_args()
    input_nc = args.input_nc
    reach_id = args.reach_id
    output_file_csv = "{}.csv".format(reach_id)
    DS = xr.open_dataset(input_nc)
    variable_name = "mod_streamq"
    # See if we have that reach
    reach_location = DS.rchid.values == reach_id
    if (~reach_location).all():
        print("Reach not found, try an existing reach: ", DS.rchid.values)
        exit(1)

    index_rch = np.argmax(DS.rchid.values == reach_id)
    print(index_rch)
    values = DS[variable_name][:, index_rch, 0, 0].to_pandas()
    values.to_csv(output_file_csv)
    
if __name__ == "__main__":
    main()


    

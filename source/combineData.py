#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:17:00 2023

@author: danikam
"""

# Import needed modules
import sys
import os
import numpy as np
import pandas as pd
import geopandas as gpd
import geopy
from pathlib import Path

def get_top_dir():
    '''
    Gets the path to the top level of the git repo (one level up from the source directory)
        
    Parameters
    ----------
    None

    Returns
    -------
    top_dir (string): Path to the top level of the git repo
        
    NOTE: None
    '''
    source_path = Path(__file__).resolve()
    source_dir = source_path.parent
    top_dir = os.path.dirname(source_dir)
    return top_dir
    
def mergeShapefile(data_df, shapefile_path, on):
    '''
    Merges the input shapefile with the data in data_df

    Parameters
    ----------
    data_df (pd.DataFrame): A pandas dataframe containing the data to be merged with the shapefile

    shapefile_path (string): Path to the shapefile to be joined with the dataframe

    Returns
    -------
    merged_Dataframe (pd.DataFrame): Joined dataframe
    '''
    shapefile = gpd.read_file(shapefile_path)
    
    # Merge the dataframes based on the subregion name
    merged_dataframe = shapefile.merge(data_df, on=on, how='left')
            
    return merged_dataframe
    
def saveShapefile(file, name):
    '''
    Saves a pandas dataframe as a shapefile

    Parameters
    ----------
    file (pd.DataFrame): Dataframe to be saved as a shapefile

    name (string): Filename to the shapefile save to (must end in .shp)

    Returns
    -------
    None
    '''
    # Make sure the filename ends in .shp
    if not name.endswith('.shp'):
        print("ERROR: Filename for shapefile must end in '.shp'. File will not be saved.")
        exit()
    # Make sure the full directory path to save to exists, otherwise create it
    dir = os.path.dirname(name)
    if not os.path.exists(dir):
        os.makedirs(dir)
    file.to_file(name)

def readData(data_path, data_type='xlsx', sheet_name=0, selected_columns='all', common_column_rename=None):
    '''
    Reads in the data file for the eGrids data
    
    Parameters
    ----------
    top_dir (string): Path to data to be read in
    
    data_type (string): Specifies the data type, either xlsx or csv
    
    sheet_name (int or string): Specifies the sheet to read, in case an xlsx is provided
    
    selected_columns (list or string): If a list is provided, the data will be filtered to only include the selected columns. If 'all' is provided, all columns will be kept.
    
    common_column_rename (list of strings or None): If a list is provided, the column specified by the first element of the list will be renamed to the string specified by the second element.

    Returns
    -------
    data_df (pd.DataFrame): A pandas dataframe containing the 2021 eGrid data for each subregion
        
    NOTE: None.

    '''
    
    # Read in the data associated with each region
    if data_type == 'xlsx':
        data = pd.ExcelFile(data_path)
        data_df = pd.read_excel(data, sheet_name, skiprows=[0])
        
    elif data_type == 'csv':
        data_df = pd.read_csv(data_path)
        
    else:
        print('ERROR: File type must be xlsx or csv. Returning without reading.')
        return
    
    # Select the columns of interest
    if not selected_columns == 'all':
        data_df = data_df.filter(selected_columns, axis=1)
    
    # Rename the subregion name to match the shapefile
    if not common_column_rename is None:
        if not isinstance(common_column_rename, list) or len(common_column_rename) != 2:
            print('ERROR: common_column_rename must be a list with two elements. No filtering performed.')
        if not common_column_rename[0] in data_df.columns:
            print('ERROR: First element of common_column_rename must be one of the data columns. No filtering performed.')
        else:
            data_df = data_df.rename(columns={common_column_rename[0]: common_column_rename[1]})

    return data_df

def main():

    # Get the path to the top level of the Git repo
    top_dir = get_top_dir()
    
    data_path = f'{top_dir}/data/eGRID2021_data.xlsx'
    
    # Read in the data
    egrid_data = readData(data_path, 'xlsx', 'SRL21', ['SUBRGN', 'SRCO2EQA', 'SRC2ERTA'], ['SUBRGN', 'ZipSubregi'])
    
    # Merge the eGrids data in with the shapefile with subregion borders
    merged_dataframe = mergeShapefile(egrid_data, f'{top_dir}/shapefile/eGRID_Subregions.shp', 'ZipSubregi')
        
    # Save the merged shapefile
    saveShapefile(merged_dataframe, f'{top_dir}/merged_shapefile/egrid2020_subregions_merged.shp')
    
main()

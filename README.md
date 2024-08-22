# Mapping tool example

This example code demonstrates how I currently combine a shapefile with a csv or xlsx file in python to produce a merged shapefile.

## Setup

To install python dependencies:

```bash
pip install -r requirements.txt
```

## Instructions to create geojson from shapefile

The script `convert_to_geojson.py` converts an input shapefile to an equivalent geojson file. To run:

```bash
python source/convert_to_geojson.py --shapefile_path [/path/to/input/shapefile] --geojson_path [/path/to/output/geojson]
```

where `--shapefile_path` defaults to the default available shapefile `shapefile/eGRID_Subregions.shp`, and `--geojson_path` defaults to `geojson/eGRID_Subregions.geojson`.

So if you just run 

```bash
python source/convert_to_geojson.py
```

this should create a geojson equivalent of `eGRID_Subregions.shp` in `geojson/eGRID_Subregions.geojson`.

## General Instructions to combine geospatial file with input data

To run the code to combine the input xlsx file with either a `.geojson` file or a  in the `data` with the shapefile in the `shapefile dir` based on the shared subregion identifier (`SUBRGN` in the xlsx and `ZipSubregi` in the geospatial file):

```bash
python source/combineData.py --geo_file_path [/path/to/input/geospatial/file] --output_file_path [/path/to/output/merged/geojson/file]
```

where `--geo_file_path` defaults to `shapefile/eGRID_Subregions.shp` and `output_file_path` defaults to `merged_geojson/egrid2020_subregions_merged.geojson`. 

## Combining input shapefile and geojson and comparing the result

The following separately combines the default shapefile and geojson input files and compares the resulting output files to confirm that they're identical:

```bash
# Combine input shapefile with .xlsx file
python source/combineData.py -g shapefile/eGRID_Subregions.shp -o output_from_shapefile/merged.geojson

# Separately combine input geojson file with .xlsx file
python source/combineData.py -g geojson/eGRID_Subregions.geojson -o output_from_geojson/merged.geojson

# Compare the results to ensure they're identical
diff output_from_geojson/merged.geojson output_from_shapefile/merged.geojson
```

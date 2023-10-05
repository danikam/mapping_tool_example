# Mapping tool example

This example code demonstrates how I currently combine a shapefile with a csv or xlsx file in python to produce a merged shapefile.

## Setup

To install python dependencies:

```bash
pip install -r requirements.txt
```

## Instructions to run

To run the code to combine the input xlsx file in the `data` with the shapefile in the `shapefile dir` based on the shared subregion identifier (`SUBRGN` in the xlsx and `ZipSubregi` in the ):

```bash
python source/combineData.py
```

This should produce a merged shapefile in the `merged_shapefile` dir. 

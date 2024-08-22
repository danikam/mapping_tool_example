import argparse
import geopandas as gpd

def convert_shapefile_to_geojson(shapefile_path, geojson_path):
    # Load the shapefile
    gdf = gpd.read_file(shapefile_path)
    
    # Save the data as a GeoJSON file
    gdf.to_file(geojson_path, driver='GeoJSON')
    print(f"GeoJSON file saved to {geojson_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert a shapefile to a GeoJSON file.")
    
    parser.add_argument("--shapefile_path", "-s", default="shapefile/eGRID_Subregions.shp", help="Path to the input shapefile. Default is shapefile/eGRID_Subregions.shp")
    parser.add_argument("--geojson_path", "-g", default="geojson/eGRID_Subregions.geojson", help="Path to the output GeoJSON file. Default is geojson/eGRID_Subregions.geojson")
    
    args = parser.parse_args()
    
    convert_shapefile_to_geojson(args.shapefile_path, args.geojson_path)

if __name__ == "__main__":
    main()

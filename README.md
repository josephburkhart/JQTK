# JQTK: Joseph's QGIS Toolkit

This is currently a catch-all repository for my scripts to automate various QGIS tasks. Eventually, I may consolidate these scripts into a QGIS plugin.

## Scripts
1. `create-small-grid.py`: This script takes an input layer and generates a small n x n grid inside each input layer feature. Each output grid cell is given a unique grid ID value that includes the parent input feature's grid ID. This script was used to create the minor reference grid in my Master's thesis.
2. `clean-grid-cell-location-list.py`: This script takes a csv file of intersections between two layers and condenses the labels in one column into a list based on duplicate values in another column. It then sorts the lists by ascending feature ID values.
3. `sort-long-grid-cell-location.py`: This script sorts long-form grid cell location IDs by row, column, and then number.
4. `shorten-grid-cell-location.py`: This script takes a list of long-form grid cell IDs and abbreviates them to a more human-readable format.
5. `max-side-length.py`: This script takes a polygon feature and calculates the length of the longest side.
6. `top-left-rotation.py`: This script takes a polygon feature and calculates the angle of its top-left side.

## Usage
The following scripts can be run directly from QGIS's python console and code editor:
- `create-small-grid.py`
- `clean-grid-cell-location-list.py`
- `sort-long-grid-cell-location.py`
- `shorten-grid-cell-location.py`

The following scripts are intended for use in the QGIS Field Calculator and must be saved as individual functions in the Function Editor:
- `max-side-length.py`
- `top-left-rotation.py`

## Compatibility
- QGIS 3.16

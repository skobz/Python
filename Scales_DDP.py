# Name: Scale from Data Driven Pages
# Created: May 5, 2015
# Author: Sven Koberwitz
# Purpose: Populate an Index feature used by Data Driven Pages 
# with scale values from layout view
# Note: The order of the driven pages must be the same as the Index table. Best to set order to ObjectID.

import arcpy

# Refer to current map document
mxd = arcpy.mapping.MapDocument('CURRENT')

# Set which feature class is used as the INDEX for the Data Driven Pages
fc = 'INDEX'

arcpy.AddField_management("INDEX", "Scale", "DOUBLE", 10)

# List used to hold all the scale values
scalelist = []

# Cursor to populate the feature class 
cursor = arcpy.UpdateCursor(fc)

# Set data frame (The first one in this case from the list)
df = arcpy.mapping.ListDataFrames(mxd)[0]

# Iterate through all the DDP's and get the scale of each data frame.
for i in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = i
    curscale = df.scale
    scalelist.append(curscale) # Append the scale list
    
i = 0 # iteration variable to go through scale list

# Iterate through each row and populate with the equivalent scale list item at position [i]
for row in cursor:
    row.setValue("Scale", float(scalelist[i]))
    cursor.updateRow(row)
    i += 1

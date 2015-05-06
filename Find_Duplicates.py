# Name: Pre-Logic Script Code
# Created: April, 27, 2015
# Author: Sven Koberwitz
# Purpose: Find the number of occurrences of a value in a Field using Field Calculator.

## Pre-Logic Script Code

import arcpy

uniqueList = {}

## Set the name of the feature class here
fc = "feature_class"
rows = arcpy.SearchCursor(fc)

for row in rows:
  ## Set the name of the attribute here
  value = row.getValue("field_name")
  if value not in uniqueList:
    uniqueList[value] = 1
  else:
    uniqueList[value] = uniqueList[value] + 1

def duplicates(inValue):  
  return uniqueList[inValue]
  

## Use this as the calculation formula
duplicates(!field_name!)

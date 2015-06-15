import arcpy
import fileinput
import string
import os
from arcpy import env
print "start"
env.workspace = "C:/Users/shaohu.zhang@sdstate.edu/Desktop/pythontry/CreatPolyline"
env.overwriteOutput = True
outpath = "C:/Users/shaohu.zhang@sdstate.edu/Desktop/pythontry/CreatPolyline"
newfc = "newPolyline100.shp"
infile="C:/Users/shaohu.zhang@sdstate.edu/Desktop/pythontry/CreatPolyline/coordinates30.txt"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    X, Y = string.split(line," ")
    array.add(arcpy.Point(float(X),float(Y)))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor
print"end"

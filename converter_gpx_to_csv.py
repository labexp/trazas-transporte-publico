from datetime import datetime
from pathlib import Path
from datetime import datetime
import pandas as pd
import os
import gpxpy.gpx
import gpxpy
import csv
from collections import namedtuple

# Parsing an existing file:
# -------------------------

def datetime_to_str(date):

    date_time = date.strftime("%Y-%m-%dT%H:%M:%SZ")
    return date_time

def gpx_to_csv(file_path):

    output = file_path[:-4]+'.csv'

    gpx_file = open(file_path, 'r')

    gpx = gpxpy.parse(gpx_file)

    waypoints = []
    for waypoint in gpx.waypoints:
        wpt = [waypoint.latitude,waypoint.longitude,waypoint.elevation,datetime_to_str(waypoint.time),waypoint.name,waypoint.satellites]
        waypoints.append(wpt)
    
    gpx_file.close()

    #with open('output.csv','w',newline='') as f:
    #    writer = csv.writer(f)
    #    writer.writerows(waypoints)
    
    df = pd.DataFrame(waypoints)
    df.to_csv(output, index=False, header= ["lat","lon","ele","time","name","sat"])


def converter():

    files = []
    
    p = Path('/home/labexp/....') ###Agregar la ruta de la carpeta

    for item in p.glob('**/*'):
        if(item.suffix=='.gpx'):
            gpx_to_csv(str(item))
       
converter()

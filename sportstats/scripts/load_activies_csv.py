import csv
import os

def load_activities():
    file = open('/home/loic/projects/sport-stats-garmin/sportstats/scripts/Activities.csv')
    read_file = csv.reader(file)
    print(read_file)

file = open('/home/loic/projects/sport-stats-garmin/sportstats/scripts/Activities.csv')
read_file = csv.reader(file)
print(read_file)
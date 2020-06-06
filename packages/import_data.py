import os
import csv

def import_data(filename):

    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = f'{fileDir}\census-2011-Households by Roof of Housing Units\{filename}'
    
    #reading from file

    list_from_file = []
    header = []

    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)
        list_from_file = list(csv_reader)
    header = list_from_file.pop(0)
    return list_from_file, header

def import_Dev_region_data(list_from_program,n):

    Dev_list = list_from_program[n]
    Dev_list.pop(1)
    Dev_list.pop(0)
    Region_list = [int(i) for i in Dev_list]
    return Region_list
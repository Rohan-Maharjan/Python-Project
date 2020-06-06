#importing methods from modules present in packages directory
from packages.bargraph import bargraph_Dev_region, bargraph_types_of_roofs, stacked_bargraph
from packages.import_data import import_data, import_Dev_region_data

#reading data from file

Dev_region_list, header = import_data('Development_region.csv') 
#module which takes filename as argument and returns the list and header from csv file

header.pop(1)
header.pop(0)
type_of_roof = header #list containing type of roof


#list comprehension

region = [i[0] for i in Dev_region_list]
total = [int(i[1]) for i in Dev_region_list]
#data of types of roofs
Thatch_Straw = [int(i[2]) for i in Dev_region_list]
Galvanized_iron = [int(i[3]) for i in Dev_region_list]
Tile_Slate = [int(i[4]) for i in Dev_region_list]
RCC = [int(i[5]) for i in Dev_region_list]
Wood_Planks = [int(i[6]) for i in Dev_region_list]
Mud = [int(i[7]) for i in Dev_region_list]
Others = [int(i[8]) for i in Dev_region_list]
Not_stated = [int(i[9]) for i in Dev_region_list]

#new list of data of different development region
Eastern = import_Dev_region_data(Dev_region_list, 0)
Central = import_Dev_region_data(Dev_region_list, 1)
Western = import_Dev_region_data(Dev_region_list, 2)
Mid_Western = import_Dev_region_data(Dev_region_list, 3)
Far_Western = import_Dev_region_data(Dev_region_list, 4)


bargraph_Dev_region(region, total) #module which takes list of x values, list of y values and category(str) to be plotted in bargraph
stacked_bargraph(region,total,Thatch_Straw,Galvanized_iron,Tile_Slate,RCC,Wood_Planks,Mud,Others,Not_stated) 
#module which takes list of values to be plotted in the stacked bar graph

#plotting Bar graphs of each development region
bargraph_types_of_roofs(type_of_roof, Eastern, region[0]) #module which takes list of x values, list of y values and Development region name(str) to be plotted in bargraph
bargraph_types_of_roofs(type_of_roof, Central, region[1])
bargraph_types_of_roofs(type_of_roof, Western, region[2])
bargraph_types_of_roofs(type_of_roof, Mid_Western, region[3])
bargraph_types_of_roofs(type_of_roof, Far_Western, region[4])

#plotting Bar graphs comparing Development regions on basis of each type of roof 
bargraph_Dev_region(region, Thatch_Straw, type_of_roof[0]) #module which takes list of x values, list of y values and type of roof(str) to be plotted in bargraph
bargraph_Dev_region(region, Galvanized_iron, type_of_roof[1])
bargraph_Dev_region(region, Tile_Slate, type_of_roof[2])
bargraph_Dev_region(region, RCC, type_of_roof[3])
bargraph_Dev_region(region, Wood_Planks, type_of_roof[4])
bargraph_Dev_region(region, Mud, type_of_roof[5])
bargraph_Dev_region(region, Others, type_of_roof[6])
bargraph_Dev_region(region, Not_stated, type_of_roof[7])

print('\nBar graphs have been plotted')
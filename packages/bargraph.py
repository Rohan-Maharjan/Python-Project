import matplotlib.pyplot as plt
import numpy as np 

#method for autolabeling above the bars
def autolabel(rects, ax):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', #str that is to be written in the label
                    xy=(rect.get_x() + rect.get_width() / 2, height), #The point (x, y) to annotate
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points", #Offset (in points) from the xy value
                    ha='center', va='bottom') #ha, va = horizontal and vertical allignments

#method that plots bar graphs of each category/column on the basis of Development Region
def bargraph_Dev_region(x_values, y_values, category = 'Total'):
    
    fig, ax = plt.subplots()
    graph = ax.bar(x_values, y_values, width = 0.5, color = 'blue', edgecolor = 'red')
    roof = 'with roof type'

    if category == 'Total':
        graph_name = f'{category} houses on the basis of Development Region in Nepal'

    else:
        graph_name = f'Houses {roof} {category.upper()} on the basis of Development Region in Nepal'

    #plot description

    plt.xlabel('Development Region', fontsize=15)
    plt.ylabel('Number of houses', fontsize=15)
    plt.title(f'{graph_name}', fontsize = 20, va = 'bottom')
    ax.ticklabel_format(style = 'plain', axis = 'y') #converts 1e6 to 10^6
    autolabel(graph, ax)
    
    plt.savefig(f'Graphs (Outputs)\{graph_name}', bbox_inches = 'tight')
    print(f'{graph_name} has been saved')




#method that plots bar graphs of each Development region on the basis of types of roofs
def bargraph_types_of_roofs(x_values, y_values, Dev_region):
    
    fig, ax = plt.subplots()
    graph = ax.bar(x_values, y_values, width = 0.5, color = 'yellow', edgecolor = 'orange')
    graph_name = f'Houses on the basis of roof types in {Dev_region} Development Region'

    #plot description
    plt.xlabel('Types of Roofs', fontsize=15)
    plt.ylabel('Number of houses', fontsize=15)
    plt.title(f'{graph_name}', fontsize = 20, va = 'bottom')
    for tick in ax.get_xticklabels():
        tick.set_rotation(90)
    autolabel(graph, ax)
    
    plt.savefig(f'Graphs (Outputs)\{graph_name}', bbox_inches = 'tight')
    print(f'{graph_name} has been saved')



#method for autolabeling above the bars in stacked bar graph
def autolabel_stacked(rects, ax, Total):
    """Attach a text label above each bar in *rects*, displaying its height."""
    i = 0
    for rect in rects:
        height = Total[i]
        ax.annotate(f'{Total[i]}', #str that is to be written in the label
                    xy=(rect.get_x() + rect.get_width() / 2, height), #The point (x, y) to annotate
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points", #Offset (in points) from the xy value
                    ha='center', va='bottom', #ha, va = horizontal and vertical allignments
                    fontsize = 50) 
        i += 1

        
#method that plots stacked bar graph of each type of roof on the basis of Development region
def stacked_bargraph(region,total,Thatch_Straw,Galvanized_iron,Tile_Slate,RCC,Wood_Planks,Mud,Others,Not_stated):
    
    plt.rcParams['figure.figsize'] = (30,50) #increase figure size to make the layers of plot for visible
    fig, ax = plt.subplots()
    
    #to be used in the 'bottom' parameter in ax.bar to form the stacked bar graph
    r12 = list(np.add(Thatch_Straw, Galvanized_iron))
    r123 = list(np.add(r12, Tile_Slate))
    r1234 = list(np.add(r123, RCC))
    r12345 = list(np.add(r1234, Wood_Planks))
    r123456 = list(np.add(r12345, Mud))
    r1234567 = list(np.add(r123456, Others))
    
    
    rect1 = ax.bar(region, Thatch_Straw, width = 0.5, color = 'violet', label = 'Thatch or Straw', edgecolor='black')
    rect2 = ax.bar(region, Galvanized_iron, bottom = Thatch_Straw, width = 0.5, color = 'indigo', label = 'Galvanized iron', edgecolor='black')
    rect3 = ax.bar(region, Tile_Slate, bottom = r12, width = 0.5, color = 'blue', label = 'Tile or Slate', edgecolor='black')
    rect4 = ax.bar(region, RCC, bottom = r123, width = 0.5, color = 'green', label = 'RCC', edgecolor='black')
    rect5 = ax.bar(region, Wood_Planks, bottom = r1234, width = 0.5, color = 'yellow', label = 'Wood or Planks', edgecolor='black')
    rect6 = ax.bar(region, Mud, bottom = r12345, width = 0.5, color = 'orange', label = 'Mud', edgecolor='black')
    rect7 = ax.bar(region, Others, bottom = r123456, width = 0.5, color = 'red', label = 'Others', edgecolor='black')
    rect8 = ax.bar(region, Not_stated, bottom = r1234567, width = 0.5, color = 'cyan', label = 'Not stated', edgecolor='black')

    graph_name = f'Total houses with roof types on the basis of Development Region in Nepal'

    #plot description
    
    plt.xlabel('Development Region', fontsize=75)
    plt.ylabel('Number of houses', fontsize=75)
    plt.title(f'{graph_name}', fontsize = 125, va = 'bottom')
    plt.xticks(fontsize = 50) 
    ax.yaxis.set_tick_params(length = 20, width = 5)
    plt.yticks(np.arange(0,2.1*10**6,10**5), fontsize = 50) 
    ax.ticklabel_format(style = 'plain', axis = 'y') 
    autolabel_stacked(rect7, ax, total)
    ax.legend(fontsize = 60)
    plt.savefig(f'Graphs (Outputs)\{graph_name}', bbox_inches = 'tight')
    print(f'{graph_name} has been saved')
    plt.rcParams['figure.figsize'] = (6.4, 4.8) #set figure size to default

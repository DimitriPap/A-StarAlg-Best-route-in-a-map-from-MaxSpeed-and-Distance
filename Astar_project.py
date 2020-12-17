#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
""" Finding the best path in a map with max speed and distance routes """
__author__ = 'Dimitri Papadakis'

import math
import sys

if(sys.argv[1] == 'help'):
    print("\nWelcome to the Super Navigation 3000")
    print()
    print('To run type in terminal: python3 Astar_project.py start')
    print()
    print('The program is going to ask you for a starting point and a destination.')
    print('After you shoose the numeric value coresponding to the city, the navigation system will display')
    print('the optimal route, in terms of distance and maxspeed.')
    print('Do not drink and drive.')


elif(sys.argv[1] == 'start'):
    map_MaxSpeed = [[999, 88, 9, 999, 999, 999],
                    [88, 999, 999, 999, 999, 48],
                    [9, 999, 999, 999, 48,999],
                    [999, 999, 999, 999, 78, 73],
                    [999, 999, 48, 78, 999, 999],
                    [999, 48, 999,73 ,999, 999]]

    print("1. Valparaiso\n2. San antonio\n3. Vina\n4. Santiago\n5. Casablanca\n6. Melipilla")

    start = input("Pick a starting point: ")
    start = int(start)
    destination_Value = input("Pick a destination point: ")
    destination_Value = int(destination_Value )
    Visited_Vertex = {}
    closed_Vertex = []
    temp_vertex_info = [start, 0]
    keep_track = {}

    #Added Melipilla into cities and into citis for calc
    cities = ['Valparaiso', 'San antonio', 'Vina', 'Santiago', 'Casablanca', 'Melipilla']
    citis_for_calc = [[1,5],[1.2 , 4.8], [1 , 5.5], [2, 3], [1.5 , 4], [3.1, 1.2]]
    """ 
    Valparaiso 1,5
    San antonio 1.2, 4.8
    Vina 1,5.5
    Santiago 2,3
    Casablanca 1.5, 4
    Melipilla 3.1 , 1.2
    """

    h_miles = {}
    for i in range(len(cities)):
        if i != start-1:
            h_miles[i+1] = math.sqrt( (citis_for_calc[start-1][0] - citis_for_calc[i][0])**2 + (citis_for_calc[start-1][1] -  citis_for_calc[i][1])**2 )
        if i == start-1:
            h_miles[i+1] = -1


    def add_info(Vertex, MaxSpeed=0, miles=0, previousVertex=0, ):
        """ Adds each vertexes info into the dictionary for tracing purposes. """
        keep_track[Vertex] = {'MaxSpeed': MaxSpeed,
                              'miles': miles,
                              'g+h': MaxSpeed + miles,
                              'previousVertex': previousVertex}


    def import_to_visited(vertix, sumOfMaxSpeed):
        """ This imports the vertex and the sum of the speed into the visited list. """
        Visited_Vertex[int(vertix)] = sumOfMaxSpeed


    def delet_visited(node):
        """ It deletes the given vertix from the dictionary. """
        del Visited_Vertex[node]


    def getTemp_vertex_info():
        return temp_vertex_info


    def editTemp_vertex_info(node, maxspeedCurrent):
        """ It updates the value of the current node """
        temp_vertex_info[0] = node
        temp_vertex_info[1] = maxspeedCurrent


    def Add_closed_Vertex(node):
        """ Adds node into closed vertex """
        closed_Vertex.append(node)


    def look_for_neighboors_updateVisitedList_updateCurrentValue():
        """ Scans neighboors, and adds them into Visited_Vertex  """
        currentNode = getTemp_vertex_info()

        for i in range (len(map_MaxSpeed[temp_vertex_info[0]-1])):

            if i + 1 in Visited_Vertex.keys() and map_MaxSpeed[temp_vertex_info[0]-1][i] != 999:
                if keep_track[i + 1]['g+h'] > map_MaxSpeed[currentNode[0] - 1][i] + currentNode[1] + h_miles[i + 1]:
                    keep_track[i + 1]['g+h'] = map_MaxSpeed[currentNode[0] - 1][i] + currentNode[1] + h_miles[i + 1]
                    keep_track[i + 1]['previousVertex'] = currentNode[0]

            if map_MaxSpeed[temp_vertex_info[0]-1][i] != 999:
                if i+1 not in closed_Vertex and i+1 not in Visited_Vertex.keys():
                    add_info(i+1, map_MaxSpeed[currentNode[0]-1][i] + currentNode[1],h_miles[i+1],currentNode[0])
                    import_to_visited(i+1, h_miles[i+1])


    def pick_best_Neighboor():
        """ It expends and picks the best neighbor  """
        compare = {}
        for k in Visited_Vertex.keys():
                compare[k]= keep_track[k]['g+h']

        min1 = min(compare.values())
        for k in compare.keys():
            if compare[k] == min1:

                closed_Vertex.append(temp_vertex_info[0])

                editTemp_vertex_info(k, keep_track[k]['MaxSpeed'])
                delet_visited(k)


    def directions():
        """ It prints the path of the best route. """
        counter = 0
        temp = []
        b = destination_Value
        while (b != start):

            for k in keep_track.keys():
                if k == b:
                    temp.append(str(keep_track[k]['previousVertex']))
                    b = keep_track[k]['previousVertex']


        temp.insert(0, str(destination_Value))
        #print('Directions:')
        print()
        print(f'The optimal route from {cities[start-1]} to {cities[destination_Value-1]} is the following:')

        count = len(temp)-1
        while count > -1:
            a = int(temp[count])
            if count > 0:
                print(cities[a-1], end=' --> ')
                count -= 1
            else:
                print(cities[a - 1], end='')
                count -= 1
                print()


    def AstarALg(destination):
        """ Magic happens here """
        while(temp_vertex_info[0]!= destination):
            look_for_neighboors_updateVisitedList_updateCurrentValue()
            pick_best_Neighboor()


    AstarALg(destination_Value)
    directions()
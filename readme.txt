Objective:

The program is a navigation system which gives you the optimal route from point A to point B. This program interacts with the user by asking for starting point, and final destination.

Implementation Details:

The code implements the A* Algorithm. The way that it works is the following:
Everything begins with the start and destination_Value. are the Temp_vertex_info which stores the current node when the program begins it will have the name of the starting point city, and the int 0 for heuristics since the distance is 0 from itself. The map_Maxspeed matrix helps the code to address the maxspeed between nodes, row is node – Colum is neighbor. The h_miles is a dictionary which stores the name of the cities and the straight line distance from the starting point. The point on the graph for each city is stores in cities_for_calc list. At line 54 it uses the mathematical formula to find the accurate straight distance from the graph. The function AstarAlg take a parameter which is the destination point and everything continues form there. It calls the look_for_neighboors_updateVisitedList_updateCurrentValue() this method looks the neighboors and stores it in a dictionary with the name Keep_track that I am using for keeping track of the process. It stores the vertex number, distance, g+h which is maxspeed + miles for heuristics, and previous vertex. Also, this method adds the name of the city and current miles info into the visited list. Then after all neighbors, and their info are saved in the dictionary the code continues with the pick_best_neighboor() function. This function looks the visited list to see the chaises, then it looks in the dictionary to find their g+h individually and pick the best. If it finds a better node in terms of g+h the Temp_vertex_info becomes the new node and the old node is pushed into the closed_vertix list. It runs till it reach the destination.

Running the program:

To start the program, you need to type in terminal:
python3 Astar_project.py start
For help type in terminal:
python3 Astar_project.py help

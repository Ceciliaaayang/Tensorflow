"""
Solution stub for the River Problem.

Fill in the implementation of the `River_problem` class to match the
representation that you specified in problem XYZ.
"""
from searchProblem import Search_problem, Arc

class River_problem(Search_problem):
    def start_node(self):
        """returns start node"""
        #two tuples represent two side of river 
        return (["Farmer","Hen","Fox","Grain"],[])

    
    def is_goal(self,node):
        """is True if node is a goal"""
        #goal is all the 4 things move to right side of river 
        return len(node[1]) == 4 

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        
        if "Farmer" in node[0]:
            index = 0
        else:
            index = 1

        neighbors = []
        for item in node[index]:
            new_opposite = node[1 - index] + [ item ]
            new_origin  = node[index][:]
            new_origin.remove(item)

            if item != "Farmer":
                new_opposite.append("Farmer")
                new_origin.remove("Farmer")
     

            if index == 0:
                new_node = (new_origin,new_opposite)
            else:
                new_node = (new_opposite,new_origin)

            # invalid situations
            if "Hen" in new_origin and ("Fox" in new_origin or "Grain" in new_origin):
                continue
            
            if item == "Farmer":
                action = "Move along"
            else:
                action = "Move " + item

            neighbors.append(Arc(node,new_node,1,action))

        return neighbors

    def heuristic(self,n):
        """Gives the heuristic value of node n."""
        #The more things that left side of river have, the further to the goal 
        return len(n[0]) 
from common import *

class Node:
    def __init__(self, ID, networksimulator, costs):
        self.myID = ID
        self.ns = networksimulator
        num = self.ns.NUM_NODES        
        self.distanceTable = [[0 for i in range(num)] for j in range(num)]
        self.routes = [0 for i in range(num)]

        # you implement the rest of constructor

    def recvUpdate(self, pkt):
        
        self.distanceTable[pkt.sourceid] = pkt.mincosts
        
        # you implement the rest of it  
              
        return 

    
    def printdt(self):
        print("   D"+str(self.myID)+" |  ", end="")
        for i in range(self.ns.NUM_NODES):
            print("{:3d}   ".format(i), end="")
        print()
        print("  ----|-", end="")
        for i in range(self.ns.NUM_NODES):            
            print("------", end="")
        print()    
        for i in range(self.ns.NUM_NODES):
            print("     {}|  ".format(i), end="" )
            
            for j in range(self.ns.NUM_NODES):
                print("{:3d}   ".format(self.distanceTable[i][j]), end="" )
            print()            
        print()
        

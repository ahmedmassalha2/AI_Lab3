


class backTracking:
    def __init(self, state):
        self.state = state
        self.colors = []
        for i in range(self.state.colors):
            self.colors.append(i+1)
        
    def MRV(self):
        #All the nodes without colors
        freeNodes = [ (self.state.vertices[i],i) for i in range(len(self.state.vertices)) 
                     if self.state.vertices[i].color == None]
        colors = [i+1 for i in range(self.colors)]
        maxR, mostRistrected = float('inf'), None
        for node in freeNodes:
            #get the colors that can be used
            usedColors = node[0].getNeighborsColors()

            set_difference = set(colors) - set(usedColors)
            print(set_difference)
            canUse = list(set_difference)
            if len(canUse) < maxR:
                maxR = len(canUse)
                mostRistrected = node[1]
        return mostRistrected
    
    
    def LCV(self, current):
        colorsCount = dict()
        usedColors = self.state.getNeighborsColors()
        for color in usedColors:
            if color not in colorsCount.keys():
                colorsCount[color] = 1
            else:
                colorsCount[color] += 1
        
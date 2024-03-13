class Vertex:
    def __init__(self, id, name):
        self.id = id #numerický identifikátor vrcholu (celočíselný typ)
        self.name = name #jméno vrcholu (znakový řetězec)
        self.edges = [] #hrany, které začínají v tomto vrcholu (seznam typu Edge)
        self.minDistance = float('inf')# minimální vzdálenost, za kterou se lze dostat do tohoto vrcholu z vrcholu, nad kterým byla provedena funkce computePath() (celočíselný typ)
        self.previousVertex = None #předchozí vrchol - vrchol, přes který vede cesta do tohoto vrcholu pro minimální cestu (typ Vertex)
 
        
class Edge:
    def __init__(self, source, target, weight):
        self.source = source #numerický identifikátor vrcholu, v kterém hrana začíná (celočíselný typ)
        self.target = target #numerický identifikátor vrcholu, v kterém hrana končí (celočíselný typ)
        self.weight = weight #váha hrany (celočíselný typ)


class Dijkstra:
    def __init__(self):
        self.vertexes = {} #vrcholy grafu, nad kterými chceme provádět Dijkstrův algoritmus

    def createGraph(self, vertexes, edgesToVertexes):
        for vertex in vertexes:
            self.vertexes[vertex] = []

        for edge in edgesToVertexes:
            for key in self.vertexes:
                if key.id == edge.source:
                    key.edges.append(edge)


    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.previousVertex = None


    def getVertexes(self):  
        ret = []
        for vertex in self.vertexes:
            ret.append(vertex)
        return ret


    def getGraphDict(self): #vrati zjednoduseny neobjektovy model grafu
        graphDict = {} 
        for vertex in self.vertexes:
            graphDict[vertex.id] = []
            for edge in vertex.edges:
                graphDict[vertex.id].append((edge.target,edge.weight))
        return graphDict


    def getWeights(self,sourceId):
        weights = {}
        for vertex in self.vertexes:
            weights[vertex.id] = float('inf')
        weights[sourceId] = 0
        self.setNewWeight(sourceId, 0)
        return weights


    def getMinIndex(self,vertexesToExplore): #pro vraceni indexu tuple s nejnizsi weight
        minValue = vertexesToExplore[0][0]
        minIndex = 0
        for i in range(0,len(vertexesToExplore)):
            if vertexesToExplore[i][0] < minValue:
                minValue = vertexesToExplore[i][0]
                minIndex = i
        return i

    def setNewWeight(self, connectedVertex, newWeight):
        for vertex in self.vertexes:
            if vertex.id == connectedVertex:
                vertex.minDistance = newWeight
                return

    def setNewpreviousVertex(self,currentVertex,connectedVertex):
        for vertex in self.vertexes:
            if vertex.id == connectedVertex:
                for vertexForSet in self.vertexes:
                    if vertexForSet.id == currentVertex:
                        vertex.previousVertex = vertexForSet
                        return

    def computePath(self, sourceId):
        graphDict = self.getGraphDict()
        weights = self.getWeights(sourceId)  
        vertexesToExplore = [(0,sourceId)]

        while vertexesToExplore:
            currentWeight, currentVertex = vertexesToExplore.pop(self.getMinIndex(vertexesToExplore))

            for connectedVertex, connectedWeight in graphDict[currentVertex]:
                newWeight = currentWeight + connectedWeight

                if newWeight < weights[connectedVertex]:
                    weights[connectedVertex] = newWeight
                    self.setNewWeight(connectedVertex, newWeight)
                    self.setNewpreviousVertex(currentVertex,connectedVertex)
                    vertexesToExplore.append((newWeight,connectedVertex))

    def getShortestPathTo(self, targetId):
        path = []
        for vertex in self.vertexes:
            if vertex.id == targetId:
                target = vertex    
                path = [target]    
        while target.previousVertex != None:
            path.append(target.previousVertex)
            target = target.previousVertex
        path.reverse()
        
        return path














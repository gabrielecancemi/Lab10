import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._g = nx.Graph()
        self._stati = DAO.getStati()
        self._IdStati = dict()

        for s in self._stati:
            self._IdStati[s.CCode] = s


    def createGraph(self, anno):
        self._g.clear()
        print(self.numEdges())
        archi = DAO.getConfiniAnno(anno)

        for a in archi:
            u = self._IdStati.get(a[0])
            v = self._IdStati.get(a[1])
            t = a[2]
            if int(t) != 1:
                self._g.add_node(u)
                self._g.add_node(v)
                continue
            if u is not None and v is not None:
                self._g.add_edge(u, v)

        print(self._g.nodes())
        #print(self.numEdges())
        res = []
        for n in self._g.nodes():
            res.append((n, self._g.degree(n)))
        res.sort(key = lambda x : x[0].StateNme)
        return(res)

    def statiRaggiungibili(self, p):
        daVisitare = [p]
        visitati = self.ricorsione(daVisitare, [])
        return visitati

    def statiRaggiungibili2(self, p):
        tree = nx.dfs_tree(self._g, p)
        return tree.nodes()

    def ricorsione(self, daVisitare, visitati):
        #if daVisitare:
            #print(len(visitati))
        for n in daVisitare:
        #n = daVisitare[-1]
            daVisitare.remove(n)
            visitati.append(n)
            vicini = self._g.neighbors(n)
            for v in vicini:
                if v not in visitati and v not in daVisitare:
                    daVisitare.append(v)
            self.ricorsione(daVisitare, visitati)

        return visitati

    def conComponents(self):
        return nx.number_connected_components(self._g)

    def numEdges(self):
        return len(self._g.edges())

    def numNodes(self):
        return len(self._g.nodes())
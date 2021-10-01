import unittest

class Graph:                
    def __init__(self, graph):
        node_connections = graph.split(",")
        
        self.init = []
        
        for data in node_connections:
            self.init.append(data[0])
            
        self.node_values = sorted(set(self.init))
        self.nodes = {}
        
        for node in self.node_values:
            self.nodes[node] = {}
            for data in node_connections:
                if node == data[0]:
                    self.nodes[data[0]][data[1]] = int(data[2])
    
    def find_total_distance(self, path):
        dist = 0
        for i in range(len(path) - 1):
            dist += self.nodes[path[i]][path[i + 1]]
        return dist
    
    def search(self, min_dist, curr_dist, prev_dist, src, dest):
        # print (f'min_dist = {min_dist}, curr_dist = {curr_dist}, src = {src}, dest = {dest}')
        
        if len(self.nodes[src]) > 1:
            prev_dist = curr_dist
            
        # self.shift_neighbors()
        
        for neighbor in self.nodes[src]:
            if curr_dist > min_dist:
                break
            
            curr_dist += self.nodes[src][neighbor]
            
            if neighbor == dest:
                min_dist = min(curr_dist, min_dist)
                break
            
            min_dist = self.search(min_dist, curr_dist, prev_dist, neighbor, dest)
            
            curr_dist = prev_dist
            
        return min_dist
        
    def shortest_distance(self, src, dest):
        print (self.nodes)
        return self.search(float('inf'), 0, 0, src, dest)
            
class test(unittest.TestCase):
    # def test_one(self):
    #     graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
    #     self.assertEqual(graph.find_total_distance("ABC"), 9)
        
    # def test_two(self):
    #     graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
    #     self.assertEqual(graph.shortest_distance("A", "C"), 9)
        
    # def test_three(self):
    #     graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
    #     self.assertEqual(graph.shortest_distance("C", "C"), 9)
        
    # def test_four(self):
    #     graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
    #     self.assertEqual(graph.shortest_distance("A", "D"), 5)
        
    # def test_five(self):
    #     graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
    #     self.assertEqual(graph.shortest_distance("E", "E"), 9)
        
    def test_six(self):
        graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
        self.assertEqual(graph.shortest_distance("D", "D"), 16)
        
    def test_seven(self):
        graph = Graph("AB5,BC4,CD8,DC8,DE6,AD5,CE2,EB3,AE7")
        self.assertEqual(graph.shortest_distance("A", "E"), 7)

if __name__ == '__main__':
    unittest.main()
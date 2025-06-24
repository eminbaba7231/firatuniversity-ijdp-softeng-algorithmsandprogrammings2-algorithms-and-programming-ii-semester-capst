import unittest

def bellman_ford(edges, nodes, source):
    dist = {node: float('inf') for node in nodes}
    dist[source] = 0

    for _ in range(len(nodes) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Negative weight cycle detected.")

    return dist

class TestBellmanFord(unittest.TestCase):

    def test_simple_graph(self):
        edges = [("A", "B", 4), ("A", "C", 5), ("B", "C", -2)]
        nodes = ["A", "B", "C"]
        source = "A"
        expected = {"A": 0, "B": 4, "C": 2}
        result = bellman_ford(edges, nodes, source)
        self.assertEqual(result, expected)

    def test_no_path(self):
        edges = [("A", "B", 2)]
        nodes = ["A", "B", "C"]
        source = "A"
        expected = {"A": 0, "B": 2, "C": float('inf')}
        result = bellman_ford(edges, nodes, source)
        self.assertEqual(result, expected)

    def test_negative_cycle(self):
        edges = [("A", "B", 1), ("B", "C", -1), ("C", "A", -1)]
        nodes = ["A", "B", "C"]
        source = "A"
        with self.assertRaises(ValueError):
            bellman_ford(edges, nodes, source)

if __name__ == '__main__':
    unittest.main()


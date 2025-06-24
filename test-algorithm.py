import unittest
from algorithm import bellman_ford

class TestBellmanFord(unittest.TestCase):
    def test_shortest_paths(self):
        vertices = 5
        edges = [(0, 1, 6), (0, 2, 7), (1, 2, 8), (1, 3, 5), (2, 3, -3)]
        steps, has_cycle, final_dist = bellman_ford(vertices, edges, 0)
        self.assertFalse(has_cycle)
        self.assertEqual(final_dist[3], 4)

    def test_negative_cycle(self):
        vertices = 3
        edges = [(0, 1, 1), (1, 2, -1), (2, 0, -1)]
        steps, has_cycle, _ = bellman_ford(vertices, edges, 0)
        self.assertTrue(has_cycle)

if __name__ == '__main__':
    unittest.main()

# import unittest 
# import networkx as nx
# import dgraph 

# class TestTopologicalSort(unittest.TestCase):

#     def setUp(self):
#         self.graph1 = dgraph.DiGraph()
#         self.graph1.add_edges_from([
#           ("CSC3100", "CSC2200"),
#           ("CSC2200", "CSC2110"),
#           ("CSC4410", "CSC2200"),
#           ("CSC4410", "CSC3100"),
#           ("CSC2200", "CSC1500"),
#           ("CSC2110", "CSC1500"),
#           ("CSC5000", "CSC3100"),
#           ("CSC1500", "CSC1100"),
#           ("CSC4710", "CSC2200"),
#           ("CSC4710", "CSC3020")
#         ])
#         self.graph2 = nx.DiGraph()
#         self.graph2.add_edges_from([
          
#         ("A", "B"),
#           ("A", "C"),
#           ("B", "D"),
#           ("C", "D")
#         ])
      
#     def test_priority_queue(self):
#         expected_res = {
#             'CSC3100': {'CSC3100', 'CSC1500', 'CSC2110', 'CSC2200', 'CSC1100'},
#             'CSC2200': {'CSC1500', 'CSC2200', 'CSC2110', 'CSC1100'}, 
#             'CSC4410': {'CSC3100', 'CSC1500', 'CSC2110', 'CSC2200', 'CSC1100'}, 
#             'CSC2110': {'CSC1500', 'CSC2110', 'CSC1100'}, 
#             'CSC4710': {'CSC3100', 'CSC1500', 'CSC2110', 'CSC2200', 'CSC1100', 'CSC3020'}, 
#             'CSC1500': {'CSC1500', 'CSC1100'}, 
#             'CSC5000': {'CSC3100', 'CSC1100'}, 
#             'CSC1100': {'CSC1100'}, 'CSC3020': {'CSC3020'}
#         }
#         memo = make_priority_queue(self.graph1)
#         self.assertDictEqual(memo, expected_res)
       
#     def test_topological_sort(self):
#         expected_res1 = ['CSC1500', 'CSC1100', 'CSC2110', 'CSC2200', 'CSC3100', 'CSC5000', 'CSC4410', 'CSC4710', 'CSC3020']
#         expected_res2 = ['A', 'B', 'C', 'D']
#         self.assertEqual(topological_sort(self.graph1), expected_res1)
#         self.assertEqual(topological_sort(self.graph2), expected_res2)
                  
                
# if __name__ == '__main__':
#     unittest.main()

import unittest
from a4 import *

class Test(unittest.TestCase):

	def test_MatrixRank(self):
		self.assertEqual(MatrixRank([[0,0,0],[0,0,0],[0,0,0]]),0)
		self.assertEqual(MatrixRank([[0,0,0,5],[4,9,12,3],[0,0,0,0],[2,9,7,8]]),3)
		self.assertEqual(MatrixRank([[10,20,10],[-20,-30,10],[30,50,0]]),2)
		self.assertEqual(MatrixRank([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]),2)
		self.assertEqual(MatrixRank([[0,1,2],[1,2,1],[2,7,8]]),3)
		self.assertEqual(MatrixRank([[1,-1,1,-1],[-1,1,-1,1],[1,-1,1,-1],[-1,1,-1,1]]),1)
		self.assertEqual(MatrixRank([[3,2,4,1],[1,1,0,2],[1,-1,1,3],[-1,2,4,2],[0,1,-1,3]]),4)

if __name__=='__main__':
	unittest.main()

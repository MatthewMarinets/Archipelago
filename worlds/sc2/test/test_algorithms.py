import unittest
from .. import algorithms

class TestAlgorithms(unittest.TestCase):
    def test_dfs_pool_finds_valid_selection(self) -> None:
        pools = [
            [1,2,3,4],
            [2,3,4,5],
            [3,4,5,6],
            [4,5,6,7],
            [5,6,7,8],
            [9,]
        ]
        selection = algorithms.random_dfs_pool_select(pools)
        self.assertIsNotNone(selection)
        self.assertEqual(len(selection), len(pools))
        for index in range(len(pools)):
            self.assertIn(selection[index], pools[index])
    
    def test_dfs_pool_returns_none_if_no_solution_exists(self) -> None:
        pools = [
            [1,2,3],
            [1,2,3],
            [1,2],
            [1,2],
        ]
        selection = algorithms.random_dfs_pool_select(pools)
        self.assertIsNone(selection)
    
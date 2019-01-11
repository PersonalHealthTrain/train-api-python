import unittest
from pht.formula import CNF, Clause


class CnfTests(unittest.TestCase):

    def test_str_1(self):
        cnf = CNF(Clause(3, 4), Clause(1, 2))
        self.assertEqual('[[1, 2], [3, 4]]', str(cnf))

    def test_str_2(self):
        cnf = CNF(Clause(1))
        self.assertEqual('[[1]]', str(cnf))

    def test_str_3(self):
        cnf = CNF(Clause(1), Clause(1, 2))
        self.assertEqual('[[1], [1, 2]]', str(cnf))

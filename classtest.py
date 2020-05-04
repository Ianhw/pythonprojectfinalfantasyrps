import unittest
from game.gameclass import Person
from game.gameclass import computer

                                                                 # unit testing


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Player = Person(1, 20, 2)

    def test_inital_all_attributes(self):
        Player = Person(1, 20, 2) # this is not self.person from setUp, but local
        assert Player.level == 1                 # note no self here on person or assert
        assert Player.maxhealth == 20
        assert Player.attack == 2

    def test_inital_all_attributes_computer(self):
        Comp = computer(1, 20, 2)  # this is not self.person from setUp, but local
        assert Comp.level == 1  # note no self here on person or assert
        assert Comp.maxhealth == 20
        assert Comp.attack == 2




if __name__ == '__main__':
    unittest.main()

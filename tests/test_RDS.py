import unittest
import sys
sys.path.insert(1, "..")
from backup_rds.RDS import RDS

class test_RDS(unittest.TestCase):

    def setUp(self):
        self.rds = RDS()

    def test_is_have_database_name(self):
        self.rds.set_database_name("my_database_name")
        self.assertTrue(self.rds.is_have_database_name())

    def test_is_have_database_name_false(self):
        self.assertFalse(self.rds.is_have_database_name())

    def test_is_have_rds_name(self):
        self.rds.set_rds_name("my_rds_name_instance")
        self.assertTrue(self.rds.is_have_rds_name())

    def test_is_have_rds_name_false(self):
        self.assertFalse(self.rds.is_have_rds_name())

    def test_set_database_name_fluent_interface(self):
        my_rds = self.rds.set_database_name("another_database_name")
        self.assertTrue(isinstance(my_rds, RDS))

    def test_set_rds_name_fluent_interface(self):
        my_rds = self.rds.set_rds_name("rds_name_instance")
        self.assertTrue(isinstance(my_rds, RDS))


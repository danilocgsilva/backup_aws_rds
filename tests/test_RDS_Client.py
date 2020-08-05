import unittest
import sys
sys.path.insert(1, "..")
from backup_rds.RDS_Client import RDS_Client
from tests.ClientRDSMock import ClientRDSMock


class test_RDS_Client(unittest.TestCase):

    def setUp(self):
        self.rds_client = RDS_Client()

    def test_get_sg_list(self):
        vpc_security_group_id = "sg-abc123409ef"
        client = ClientRDSMock(SecurityGroupId=vpc_security_group_id)
        sg_list = self.rds_client.get_sg_list(client)
        self.assertEqual(vpc_security_group_id, sg_list[0]["VpcSecurityGroupId"])

    def test_get_sg_list_type(self):
        client = ClientRDSMock()
        sg_list = self.rds_client.get_sg_list(client)
        self.assertTrue(isinstance(sg_list, list))

    def test_get_sg_list_member_type(self):
        client = ClientRDSMock()
        sg_list = self.rds_client.get_sg_list(client)
        member_one = sg_list[0]
        self.assertTrue(isinstance(member_one, dict))

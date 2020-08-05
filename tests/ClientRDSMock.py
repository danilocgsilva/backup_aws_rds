import json
from awsapimock.RDS_Data_Generator import RDS_Data_Generator

class ClientRDSMock:

    def __init__(self, SecurityGroupId=None):
        self.securityGroupId = None
        if SecurityGroupId:
            self.securityGroupId = SecurityGroupId

    def describe_db_instances(self, Filters=None) -> dict:

        rds_generator = RDS_Data_Generator()
        if self.securityGroupId:
            rds_generator.set_security_group_id(self.securityGroupId)

        return rds_generator.generate()

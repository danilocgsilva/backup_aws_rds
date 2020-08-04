import boto3

class RDS_Client:

    def __init__(self):
        self.sgid = None
        self.instance_name = None

    def set_sgid(self, sgid: str):
        self.sgid = sgid
        return self

    def set_instance_name(self, instance_name: str):
        self.instance_name = instance_name
        return self

    def communicate_assign_sg(self):
        client = boto3.client('rds')
        sg_list = self.get_sg_list(client)

    def get_sg_list(self, client):
        instances = client.describe_db_instances(Filters=[
            {'Name': 'db-instance-id', 'Values': [self.instance_name]}
        ])


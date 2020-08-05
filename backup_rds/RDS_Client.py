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
        sg_list.append(self.generate_security_group_data_from_sgid())
        self.assign_multiple_sgs(sg_list, client)

    def get_sg_list(self, client):
        response = client.describe_db_instances(Filters=[
            {'Name': 'db-instance-id', 'Values': [self.instance_name]}
        ])

        db_instances_result = response["DBInstances"]

        if len(db_instances_result) > 1:
            raise Exception("This method supposes that only one database instance are returned, but several ones has been returned.")

        return db_instances_result[0]["VpcSecurityGroups"]

    def assign_multiple_sgs(self, sg_list: list, client):

        sg_list_ids = []

        for sgid in sg_list:
            sg_list_ids.append(sgid["VpcSecurityGroupId"])

        client.modify_db_instance(
            DBInstanceIdentifier=self.instance_name,
            VpcSecurityGroupIds=sg_list_ids,
            ApplyImmediately=True,
        )

    def generate_security_group_data_from_sgid(self) -> dict:
        return {
            "VpcSecurityGroupId": self.sgid,
            "Status": "active"
        }


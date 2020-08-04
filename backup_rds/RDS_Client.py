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

    def assing(self):



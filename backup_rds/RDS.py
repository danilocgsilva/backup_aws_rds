class RDS():

    def __init__(self):
        self.database_name = None
        self.rds_name = None

    def set_database_name(self, name):
        self.database_name = name
        return self

    def set_rds_name(self, name):
        self.rds_name = name
        return self

    def set_password(self, password):
        self.password = password
        return self

    def get_rds_name(self):
        return self.rds_name

    def get_database_name(self):
        return self.database_name

    def is_have_rds_name(self) -> bool:
        return self.rds_name != None

    def is_have_database_name(self) -> bool:
        return self.database_name != None

from backup_rds.RDS import RDS
from getpass import getpass

def ask_database_values(rds: RDS):

    if not rds.is_have_rds_name():
        rds.set_rds_name(input("What is the RDS instance name? "))

    if not rds.is_have_database_name():
        rds.set_database_name(input("What is the database name? "))

    rds.set_password(getpass("Please, type here the database password: "))

    print("You ar going make a backup from a rds name " + rds.get_rds_name() + ", and the database named as " + rds.get_database_name())

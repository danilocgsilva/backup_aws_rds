import argparse
from backup_rds.functions import ask_database_values
from backup_rds.RDS import RDS
from backup_rds.MySqlClient import MySqlClient

def main():

    mysql_client = MySqlClient()
    if not mysql_client.is_can_access_mysql_local():
        print("I could not access the local mysql client. May it is not installed in the system.")
        exit()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--name",
        "-n",
        type=str,
        required=False,
        help="The RDS instance name"
    )

    parser.add_argument(
        "--database",
        "-d",
        type=str,
        required=False,
        help="The database name"
    )

    args = parser.parse_args()

    rds = RDS().set_database_name(args.database).set_rds_name(args.name)

    ask_database_values(rds)


if __name__ == '__main__':
    main()

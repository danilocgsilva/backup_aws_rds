import argparse
from backup_rds.functions import ensure_database_values_asking
from backup_rds.RDS import RDS
from backup_rds.MySqlClient import MySqlClient


def main():

    check_client_locally_installed()

    args = get_arguments_parsed()

    rds = RDS().set_database_name(args.database).set_rds_name(args.name)

    rds = ensure_database_values_asking(rds)


def check_client_locally_installed():
    mysql_client = MySqlClient()
    if not mysql_client.is_can_access_mysql_local():
        print("I could not access the local mysql client. May it is not installed in the system.")
        exit()


def get_arguments_parsed():
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

    return parser.parse_args()


if __name__ == '__main__':
    main()

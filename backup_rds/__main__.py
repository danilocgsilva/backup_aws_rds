import argparse
from backup_rds.functions import ask_database_values
from backup_rds.RDS import RDS

def main():

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

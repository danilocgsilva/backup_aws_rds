import argparse
from backup_rds.functions import ensure_database_values_asking
from backup_rds.RDS import RDS
from backup_rds.RDS_Client import RDS_Client
from backup_rds.MySqlClient import MySqlClient
from awssg.SG_Client import SG_Client
from awssg.Client import Client
from whatismyip.Wimi import Wimi


def main():
    mysql_client = MySqlClient()
    check_client_locally_installed(mysql_client)
    args = get_arguments_parsed()
    rds = RDS().set_database_name(args.database).set_rds_name(args.name)
    rds = ensure_database_values_asking(rds)
    group_ip = create_security_group_with_external_ip()
    RDS_Client().set_instance_name(rds.get_rds_name()).set_sgid(group_ip).communicate_assign_sg()


def check_client_locally_installed(mysql_client: MySqlClient):
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


def create_security_group_with_external_ip():
    ec2 = Client()
    sg_client = SG_Client()
    temporary_security_group = "temporary-security-group"
    result = sg_client.set_client(ec2).set_group_name(temporary_security_group).create_sg()
    just_created_group_id = result["GroupId"]
    sg_client.set_rule(
        just_created_group_id,
        'tcp', 
        Wimi().get_ip('ipv4'),
        '3306'
    )
    return just_created_group_id


if __name__ == '__main__':
    main()

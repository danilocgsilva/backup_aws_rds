import json


class ClientRDSMock:

    def describe_db_instances(self, Filters=None) -> dict:
        string_data = '''
        {
    "DBInstances": [
        {
            "DBInstanceIdentifier": "main-database",
            "DBInstanceClass": "db.t2.supermini",
            "Engine": "mysql",
            "DBInstanceStatus": "available",
            "MasterUsername": "root",
            "DBName": "themaindatabase",
            "Endpoint": {
                "Address": "main-database.abcdefgwyz.mo-east-4.rds.amazonaws.com",
                "Port": 3306,
                "HostedZoneId": "ABCDEXYZ1234890"
            },
            "AllocatedStorage": 20,
            "PreferredBackupWindow": "12:00-13:00",
            "BackupRetentionPeriod": 72,
            "DBSecurityGroups": [],
            "VpcSecurityGroups": [
                {
                    "VpcSecurityGroupId": "sg-abc123409ef",
                    "Status": "active"
                }
            ],
            "DBParameterGroups": [
                {
                    "DBParameterGroupName": "default.mysql4.0",
                    "ParameterApplyStatus": "in-sync"
                }
            ],
            "AvailabilityZone": "mo-east-4e",
            "DBSubnetGroup": {
                "DBSubnetGroupName": "default",
                "DBSubnetGroupDescription": "default",
                "VpcId": "vpc-890ab56cd",
                "SubnetGroupStatus": "Complete",
                "Subnets": [
                    {
                        "SubnetIdentifier": "subnet-abab1212",
                        "SubnetAvailabilityZone": {
                            "Name": "mo-east-4a"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-cdcd5656",
                        "SubnetAvailabilityZone": {
                            "Name": "mo-east-4b"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-123fd12ab",
                        "SubnetAvailabilityZone": {
                            "Name": "mo-east-4d"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-ab123456f",
                        "SubnetAvailabilityZone": {
                            "Name": "mo-east-4f"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-a01b34c56",
                        "SubnetAvailabilityZone": {
                            "Name": "mo-east-4e"
                        },
                        "SubnetStatus": "Active"
                    },
                    {
                        "SubnetIdentifier": "subnet-d78e90f12",
                        "SubnetAvailabilityZone": {
                            "Name": "mo-east-4c"
                        },
                        "SubnetStatus": "Active"
                    }
                ]
            },
            "PreferredMaintenanceWindow": "fri:04:33-fri:05:03",
            "PendingModifiedValues": {},
            "MultiAZ": false,
            "EngineVersion": "4.0.'01",
            "AutoMinorVersionUpgrade": false,
            "ReadReplicaDBInstanceIdentifiers": [],
            "LicenseModel": "mit",
            "OptionGroupMemberships": [
                {
                    "OptionGroupName": "default:mysql-4-0",
                    "Status": "in-sync"
                }
            ],
            "PubliclyAccessible": true,
            "StorageType": "gp2",
            "DbInstancePort": 0,
            "StorageEncrypted": false,
            "DbiResourceId": "db-AD89ASDFA7SDF6AS7D6",
            "CACertificateIdentifier": "rds-ca-2008",
            "DomainMemberships": [],
            "CopyTagsToSnapshot": false,
            "MonitoringInterval": 0,
            "DBInstanceArn": "arn:aws:rds:mo-east-4:13418273987:db:main-database",
            "IAMDatabaseAuthenticationEnabled": false,
            "PerformanceInsightsEnabled": false,
            "DeletionProtection": false,
            "AssociatedRoles": []
        }
    ],
    "ResponseMetadata": {
        "RequestId": "abc12-def0990-12ab-cd56-fab123456ab",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "abc12-def0990-12ab-cd56-fab123456ab",
            "content-type": "text/xml",
            "content-length": "4123124523",
            "vary": "accept-encoding",
            "date": "Tue, 32 Aug 2012 14:61:22 GMT"
        },
        "RetryAttempts": 0
    }
}'''
        return json.loads(string_data)

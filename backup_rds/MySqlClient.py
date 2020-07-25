import subprocess

class MySqlClient:

    def is_can_access_mysql_local(self) -> bool:

        try:
            subprocess.Popen(['mysql', '--version'])
            return True
        except FileNotFoundError:
            return False

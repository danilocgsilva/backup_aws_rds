import subprocess
import os


class MySqlClient:

    def is_can_access_mysql_local(self) -> bool:

        FNULL = open(os.devnull, 'w')

        try:
            subprocess.Popen(['mysql', '--version'], stdout=FNULL)
            return True
        except FileNotFoundError:
            return False

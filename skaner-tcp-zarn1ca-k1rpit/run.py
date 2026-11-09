from scan_conn.regular_scanning import *

from conn_banner.regular_banner_scraping import *
from conn_banner.web_scraping_banner import *

from sys import platform


def main() -> None:
    IP: str = input('input IP>')
    TIME: int = int(input('input delay scan port>'))
    TIMEOUT: float = float(input('input timeout>'))
    NAME_DICT: str =input('name file .json>') 
    banner_grabbing(ip=IP,time_max=TIME,timeout=TIMEOUT,name=NAME_DICT)



if __name__ == "__main__":
    if platform == 'linux':
        pass
    else:
        print('Warning:\tYour OS is not supported.\nThis program was not designed or tested on other operating systems.\nExecution halted.')
    main()

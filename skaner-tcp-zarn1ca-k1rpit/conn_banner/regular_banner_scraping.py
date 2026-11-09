from scan_conn.regular_scanning import *
import socket


def banner_grabbing(*,ip: str,time_max: int,timeout:float,name: str) -> None:
    dict_ports_json: dict[int,str]=unpack_json(name=name)
    open_port,open_port_dict = execute_ports_scanning(ip=ip,ports=dict_ports_json,time_max=time_max,timeout=timeout)
    
    for port in open_port:
        
                s: socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.settimeout(3.0)
                result_data: int = s.connect_ex((ip,int(port)))
                
                if result_data == 0:
                    try:
                        s.sendall(b"\r\nHELP\r\nEHLO\r\n")
                        data_baner = s.recv(1024)
                        print(f'baner port\t{port}:\f{str(data_baner.rstrip()).rstrip()}')
                    except ConnectionResetError as error:
                        print(f'PORT:{port}:\t{error}')
                    except socket.timeout as error:
                        print(f'PORT:{port}:\t{error}')
                    except Exception as error:
                        print(f'PORT:{port}:\t{error}')
                    finally:
                        s.close()
                        
    print(f'{open_port=}\n{open_port_dict=}')

    
"""python3 -m conn_banner.regular_banner_scraping """
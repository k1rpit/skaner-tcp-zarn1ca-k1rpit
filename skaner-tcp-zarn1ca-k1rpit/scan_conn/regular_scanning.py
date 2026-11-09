import socket
import json
import random
import time



def unpack_json(*,name: str) -> dict[int,str]:
    with open(f'json-data-ports/{name}','r') as file:
        raw_data_json: str = file.read()
    data_json: dict[int,str] =  json.loads(raw_data_json)
    return data_json



def execute_ports_scanning(*,ip: str,ports: dict[int,str],time_max: int,timeout:float) -> tuple[list[int],dict[int,str]]:
    open_port: list = []
    open_port_dict: dict[int,str] = {}
    for port,servis in ports.items():
        s: socket.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(timeout)
        time.sleep(random.randint(0,time_max))
        
        
        connect_attempt=s.connect_ex((ip,int(port)))
        s.close()
        
        if connect_attempt == 0:

                    
                    open_port.append(port)
                    open_port_dict[port] = servis
    return open_port,open_port_dict


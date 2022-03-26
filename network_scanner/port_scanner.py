import socket, time
from itertools import repeat
from multiprocessing import Pool

def check_ports_range(ip, start_port, end_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    result_types = []
    sucess_flg = False
    for port in range(start_port, end_port):
        result = s.connect_ex((ip, port))
        if result==0:
            print(f'connected {ip}:{port}')
            sucess_flg = True
            s.shutdown(socket.SHUT_RDWR)
            s.close()
        elif result==111:
            #print(f'connecting {ip}:{port} - {result}.\n')
            sucess_flg = False
        else:
            print(f'connecting {ip}:{port} - {result}')
            sucess_flg = False
        
        if sucess_flg:
            time.sleep(2)
            
        if result not in result_types:
            result_types.append(result)
    
    return result_types  


def check_port(pair):
    ip, port = pair
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((ip, port))
    if result==0:
        print(f'connected {ip}:{port}')
        sucess_flg = True
        s.shutdown(socket.SHUT_RDWR)
        s.close()
    elif result==111:
        pass
    else:
        print(f'connecting {ip}:{port} - {result}')    
    return None


if __name__=='__main__':
    from sys import argv
    ip = argv[1]
    ports_range = [port for port in range(1, 65535)]
    check_pair = zip(repeat(ip), ports_range)
    pool = Pool(processes=3)
    with Pool(processes=3) as p:
        p.map(check_port, check_pair)
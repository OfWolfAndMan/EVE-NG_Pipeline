from .eve_server_endpoints import EveServer
from .device import Router

LAB_NAME = 'test_1'

def app_1():
    my_eve = EveServer('192.168.170.129')
    my_eve.login('admin', 'eve')
    print ("*** CONNECTED TO UNL ***")
    lab = my_eve.create_lab(LAB_NAME)
    print("*** CREATED LAB ***")
    node_1 = lab.create_node(Router('R1'))
    print("*** CREATED NODE ***")

if __name__ == '__main__':
    app_1()
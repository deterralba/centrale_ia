import socket
from const import HUM, WOLV, VAMP
from time import sleep


class ComServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_with_server(self):
        self.connexion.connect((self.host, self.port))
        print('Opened connection with {} on {}'.format(self.host, self.port))

    def close_connexion(self):
        self.connexion.close()
        print('Closed connection with server')

    def send_name(self, name):
        self.connexion.send('NME'.encode('ascii'))
        self.connexion.send(bytes([len(name)]))
        self.connexion.send(name.encode('ascii'))

    def listen(self):
        msg = self.connexion.recv(3).decode('ascii')
        if msg == 'BYE':
            self.close_connexion()
        return msg

    def get_set(self):
        msg = self.connexion.recv(3).decode('ascii')
        if msg == 'SET':
            height = self.connexion.recv(1)
            width = self.connexion.recv(1)
            return int.from_bytes(height, byteorder='big'), int.from_bytes(width, byteorder='big')
        else:
            return 'Expected SET but received : ' + msg

    def get_hum(self):
        msg = self.connexion.recv(3).decode('ascii')
        if msg == 'HUM':
            size = self.connexion.recv(1)
            size = int.from_bytes(size, byteorder='big')
            humans = []
            for i in range(size):
                x = self.connexion.recv(1)
                y = self.connexion.recv(1)
                humans.append((int.from_bytes(x, byteorder='big'), int.from_bytes(y, byteorder='big')))
            return humans
        else:
            return 'Expected HUM but received : ' + msg

    def get_hme(self):
        msg = self.connexion.recv(3).decode('ascii')
        if msg == 'HME':
            x = self.connexion.recv(1)
            y = self.connexion.recv(1)
            return int.from_bytes(x, byteorder='big'), int.from_bytes(y, byteorder='big')
        else:
            return 'Expected HME but received : ' + msg

    def get_map(self):
        msg = self.connexion.recv(3).decode('ascii')
        if msg == 'MAP':
            size = self.connexion.recv(1)
            size = int.from_bytes(size, byteorder='big')
            map = []
            for i in range(size):
                x = int.from_bytes(self.connexion.recv(1), 'big')
                y = int.from_bytes(self.connexion.recv(1), 'big')
                hum = int.from_bytes(self.connexion.recv(1), 'big')
                vamp = int.from_bytes(self.connexion.recv(1), 'big')
                wolv = int.from_bytes(self.connexion.recv(1), 'big')
                map.append({'x': x, 'y': y, HUM: hum, VAMP: vamp, WOLV: wolv})
            return map
        else:
            return  'Expected MAP but received : ' + msg

    def get_upd(self):
        size = self.connexion.recv(1)
        size = int.from_bytes(size, byteorder='big')
        map = []
        for i in range(size):
            x = int.from_bytes(self.connexion.recv(1), 'big')
            y = int.from_bytes(self.connexion.recv(1), 'big')
            hum = int.from_bytes(self.connexion.recv(1), 'big')
            vamp = int.from_bytes(self.connexion.recv(1), 'big')
            wolv = int.from_bytes(self.connexion.recv(1), 'big')
            map.append({'x': x, 'y': y, HUM: hum, VAMP: vamp, WOLV: wolv})
        return map

    def send_mov(self, trame):
        self.connexion.send('MOV'.encode('ascii'))
        self.connexion.send(bytes([len(trame)]))
        for mvt in trame:
            for i in range(5):
                self.connexion.send(bytes([mvt[i]]))

if __name__ == '__main__':
    host = "localhost"
    port = 5555

    com = ComServer(host, port)
    com.connect_with_server()

    com.send_name('FLO')

    print('SET : ', com.get_set())
    print('HUM : ', com.get_hum())
    print('HME : ', com.get_hme())
    print('MAP : ', com.get_map())

    while True:
        msg = com.listen()
        if msg == 'BYE':
            print('BYE')
            break
        else:
            upd = com.get_upd()
            print(upd)
            mvt = [[4, 3, 1, 4, 2]]
            com.send_mov(mvt)
            sleep(2)

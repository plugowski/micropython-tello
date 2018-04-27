import socket


class Tello:

    TELLO_IP = '192.168.10.1'
    TELLO_PORT = 8889

    FLIP_LEFT = 'l'
    FLIP_RIGHT = 'r'
    FLIP_FRONT = 'f'
    FLIP_BACK = 'b'
    FLIP_LEFT_BACK = 'lb'
    FLIP_RIGHT_BACK = 'rb'
    FLIP_LEFT_FRONT = 'lf'
    FLIP_RIGHT_FRONT = 'rf'

    DIRECTION_DOWN = 'down'
    DIRECTION_UP = 'up'
    DIRECTION_FORWARD = 'forward'
    DIRECTION_BACKWARD = 'back'
    DIRECTION_LEFT = 'left'
    DIRECTION_RIGHT = 'right'

    def __init__(self, local_ip, local_port):

        self.abort_flag = False
        self.response = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tello_address = (self.TELLO_IP, self.TELLO_PORT)

        self.socket.bind((local_ip, local_port))

        # put tello into command mode
        self.command('command')

    def __del__(self):
        self.socket.close()

    def command(self, command):
        self.socket.sendto(command.encode('utf-8'), self.tello_address)

    def takeoff(self):
        self.command('takeoff')

    def flip(self, direction: str):
        self.command('flip %s' % direction)

    def land(self):
        self.command('land')

    def move(self, direction, distance):
        distance = int(round(float(distance) * 100))
        self.command('%s %s' % (direction, distance))

    def move_backward(self, distance):
        self.move(self.DIRECTION_BACKWARD, distance)

    def move_down(self, distance):
        self.move(self.DIRECTION_DOWN, distance)

    def move_forward(self, distance):
        self.move(self.DIRECTION_FORWARD, distance)

    def move_left(self, distance):
        self.move(self.DIRECTION_LEFT, distance)

    def move_right(self, distance):
        self.move(self.DIRECTION_RIGHT, distance)

    def move_up(self, distance):
        self.move(self.DIRECTION_UP, distance)

    def set_speed(self, speed):
        speed = int(round(float(speed) * 27.7778))
        self.command('speed %s' % speed)

    def rotate_cw(self, degrees):
        self.command('cw %s' % degrees)

    def rotate_ccw(self, degrees):
        self.command('ccw %s' % degrees)

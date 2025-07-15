import socket
from Environment import Environment

class NetworkingUtils(object):

    def check_internet_connection(host = "8.8.8.8", port = 53, timeout = 3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error as ex:
            Environment().get_logger().error(NetworkingUtils.__name__ + " - " + repr(ex))
            return False

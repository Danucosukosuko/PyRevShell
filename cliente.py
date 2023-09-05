# -*- coding: latin-1 -*-
import socket
import subprocess
import os

def start_client():
    host = 'x.x.x.x'  # Cambia la dirección IP a la del servidor
    port = 4444

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))

    while True:
        command = input(f"Shell remota ({host}:{port})> ")
        client.send(command.encode())

        if command.lower() == 'exit':
            break

        response = client.recv(4096).decode()
        print(response)

    client.close()

if __name__ == "__main__":
    start_client()

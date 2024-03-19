import websocket

class WebSocketClient:
    def __init__(self, server_url):
        self.server_url = server_url
        self.ws = websocket.WebSocketApp(server_url,
                                          on_open=self.on_open,
                                          on_message=self.on_message,
                                          on_error=self.on_error,
                                          on_close=self.on_close)

    def on_open(self, ws):
        print("Connected to server")

    def on_message(self, ws, message):
        print("Received message:", message)

    def on_error(self, ws, error):
        print("Error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("Disconnected from server")

    def run_forever(self):
        self.ws.run_forever()

    def send_message(self, message):
        self.ws.send(message)
        print("Sent message:", message)

# Contoh penggunaan
if __name__ == "__main__":
    client = WebSocketClient("ws://localhost:5555")
    client.run_forever()  # Jalankan klien secara terus-menerus

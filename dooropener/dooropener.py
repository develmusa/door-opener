from relaycontroller import RelayController
from webserver import WebServer

# Constants
VENDOR_ID=0x1a86
PRODUCT_ID=0x7523
HOST='::'
PORT=6666
ACTIVATION_TIME=5

def main():
    relay_controller = RelayController(vendor_id=VENDOR_ID, product_id=PRODUCT_ID, activation_time=ACTIVATION_TIME)
    web_server = WebServer(host=HOST, port=PORT, relay_controller=relay_controller)
    web_server.start()

if __name__ == "__main__":
    main()
import websocket
import thread
import time
import json
import logging

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)


class TxWatcher(object):
    def __init__(self, addresses=[]):
        self.addresses = addresses

    def on_message(self, ws, message):
        data = json.loads(message)
        log.debug("Receiving: {0}".format(data))
        d = [d for d in data['x']['out'] if d['addr'] in self.addresses]
        print(sum([a['value'] / 100000000.0 for a in d]))

    def on_error(self, ws, error):
        log.exception(error)

    def on_close(self, ws):
        log.critical('Closing WebSocket connection')

    def on_open(self, ws):
        def run(*args):
            for addr in self.addresses:
                time.sleep(0.1)
                log.debug('Sending: {"op": "addr_sub", "addr": "' + addr + '"}')
                ws.send('{"op": "addr_sub", "addr": "' + addr + '"}')

            # Ping every 30 secs so we won't get disconnected
            while 1:
                log.debug('Sending ping')
                ws.send('')
                time.sleep(30)
        thread.start_new_thread(run, ())

    def run_forever(self):
        log.info('Starting Blockchain WebSocket server...')
        ws = websocket.WebSocketApp("ws://ws.blockchain.info:8335/inv",
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
        ws.run_forever()

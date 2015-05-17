import thread
import time
import json
import logging

from events import Events
import websocket

logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger(__name__)


class TxWatcher(Events):
    __events__ = ['on_tx']

    def __init__(self, addresses=[]):
        self.addresses = set(addresses)
        self.events = Events()

    def on_message(self, ws, message):
        data = json.loads(message)
        log.debug("Receiving: {0}".format(data))
        self.on_tx(data)

    def on_error(self, ws, error):
        log.exception(error)

    def on_close(self, ws):
        log.critical('Closing WebSocket connection')

    def add_addresses(self, *addresses, **kwargs):
        for addr in addresses:
            time.sleep(0.1)
            log.debug('Sending: {"op": "addr_sub", "addr": "' + addr + '"}')
            kwargs.get('ws', self.ws).send('{"op": "addr_sub", "addr": "' + addr + '"}')

    def on_open(self, ws):
        def run(*args):
            self.add_addresses(*self.addresses, ws=ws)
            # Ping every 30 secs so we won't get disconnected
            while 1:
                log.debug('Sending ping')
                ws.send('')
                time.sleep(30)
        thread.start_new_thread(run, ())

    def _run_forever(self):
        log.info('Starting Blockchain WebSocket server...')
        self.ws = websocket.WebSocketApp("wss://ws.blockchain.info/inv",
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close)
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def run_forever(self):
        delay = 1
        while 1:
            # Trying to run_forever using an exponential backoff
            try:
                self._run_forever()
            except websocket.WebSocketException, exc:
                log.exception(exc)
                log.warning('Trying to restart connection in {0} seconds...'.format(delay))
                time.sleep(delay)
                delay *= 2
            except Exception, exc:
                raise exc

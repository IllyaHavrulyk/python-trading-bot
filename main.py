import logging

from connectors.binance import BinanceClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root



class Main:
    def __init__(self) -> None:
        if __name__ == '__main__':  # Execute the following code only when executing main.py (not when importing it)

            

            # Create and configure the logger object

            self.logger = logging.getLogger()
            self.logger.setLevel(logging.DEBUG)  # Overall minimum logging level

            self.stream_handler = logging.StreamHandler()  # Configure the logging messages displayed in the Terminal
            self.formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
            self.stream_handler.setFormatter(self.formatter)
            self.stream_handler.setLevel(logging.INFO)  # Minimum logging level for the StreamHandler

            self.file_handler = logging.FileHandler('info.log')  # Configure the logging messages written to a file
            self.file_handler.setFormatter(self.formatter)
            self.file_handler.setLevel(logging.DEBUG)  # Minimum logging level for the FileHandler

            self.logger.addHandler(self.stream_handler)
            self.logger.addHandler(self.file_handler)

            self.binance = BinanceClient("<your binance public key>",
                                    "<your binance secret key>",
                                    testnet=True, futures=True)
            self.bitmex = BitmexClient("<your bitmex public key>", "<your bitmex secret key>", testnet=True)

            self.root = Root(self.binance, self.bitmex)
            self.root.mainloop()

Main()
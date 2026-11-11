from datetime import datetime
from PriceTracker import PriceTracker

class MarketTracker:
    """
    A character class that tracks the node's attributes
    """
    def __init__(self):
        """
        Creates the dictionary of the tracker
        """
        self._trackers={}

    def add_price(self,name:str,time:datetime,price:float):
        """
        A method that adds a new node with name, the time added and its price
        Args:
            name: name of the node
            time: the time the node was added
            price: the price of the node
        """
        if name not in self._trackers:
            self._trackers[name]=PriceTracker()
        self._trackers[name].add_price(time,price)

    def get_price_data(self,name:str,start:datetime,end:datetime):
        """
        A method that brings the time window with the given parameters
        Args:
            name: the name of the node
            start: the start of the window
            end: the end of the window
        Returns: the time window of the good
        """
        if name not in self._trackers:
            raise KeyError
        return self._trackers[name].get_price_data(start,end)

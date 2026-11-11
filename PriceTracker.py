from AVLTree import AVLTree
from Heap import MinHeap
from datetime import datetime,timedelta
from BST import range_query

class PriceTracker:
    """
    A character class that tracks the prices of nodes on a tree
    """
    def __init__(self):
        """
        Sets the attributes of the price tree
        """
        self._price_tree=AVLTree()
        self._recent_prices=MinHeap()
        self._price_map={}
        self._latest_time=None

    def add_price(self, time: datetime, price: float):
        """
        A method adds a price and updates the most recent ten-day window
        Args:
            time: the time of adding
            price: the price of the good
        """
        if len(self._price_tree)==0:
            node = self._recent_prices.insert(key=price)
            self._price_map[time]=node
            self._price_tree.insert(key=time,value=price)
            self._latest_time=time
            return

        old_time_window=self._latest_time-timedelta(days=10)
        new_time_window=time-timedelta(days=10)
        outdated_times=[t for t,_ in range_query(self._price_tree,old_time_window,new_time_window)]
        for t in outdated_times:
            if t in self._price_map:
                node=self._price_map[t]
                self._recent_prices.delete_node(node)
                del self._price_map[t]
        node=self._recent_prices.insert(price)
        self._price_map[time]=node
        self._price_tree.insert(key=time, value=price)
        if self._latest_time is None or time>self._latest_time:
            self._latest_time=time


    def get_price_data(self,start:datetime,end:datetime):
        """
        A method that gives the most recent ten-day window
        Args:
            start: start of the window
            end: end of the window
        """
        data=range_query(self._price_tree,start-timedelta(days=10),end)
        data=sorted(data,key=lambda x:x[0])
        result=[]
        for (time,price) in data:
            if start<=time<=end:
                window_start=time-timedelta(days=10)
                window_data=range_query(self._price_tree, window_start, time)
                min_p=min(p for _,p in window_data)
                max_p=max(p for _,p in window_data)
                avg_p=sum(p for _,p in window_data)/len(window_data)
                result.append((time, (price,min_p,max_p,avg_p)))
        return result
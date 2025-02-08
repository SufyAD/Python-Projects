from typing import TypedDict, operator
from queue  import PriorityQueue

counter = 0

class Warehouse():
    def __init__(self, racks, capacity):
        self.racks: any = {rack: PriorityQueue() for rack in racks}
        self.capacity: int
    
    def add_item(self, rack_name:str, item: dict):
        global counter 
        counter += 1
        self.racks[rack_name].put((item["priority"], counter, item))

    def retrieve_item(self, rack_name: str):
        if self.racks[rack_name].empty():
            return f"Rack with {rack_name} does not exist!"
        _, _, item = self.racks[rack_name].get()
        return item
    
    def is_rack_empty(self):
        if (~self.capacity):
            return True
        return False
    
    def is_rack_full(self):
        if(self.capacity):
            return False
        return True
 
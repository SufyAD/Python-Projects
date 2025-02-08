from typing import TypedDict, operator
from queue  import PriorityQueue

# counter = 0 # we will not be using global counter, instead we'll use rack_counter

class Warehouse():
    def __init__(self, racks, capacity):
        self.racks = {rack: PriorityQueue() for rack in racks}
        self.capacity = capacity
        self.rack_count = {rack: 0 for rack in racks}
    
    def is_rack_empty(self, rack_name: str):
        return self.rack_count[rack_name] < self.capacity
      
    def add_item(self, rack_name:str, item: dict):
        if(self.is_rack_empty(rack_name)):
            self.rack_count[rack_name] += 1
            self.racks[rack_name].put((item["priority"], item))
            return "Item successfully added"
        return "No space left on rack!"

    
    def retrieve_item(self, rack_name: str):
        try:
            if self.racks[rack_name].empty():
                return f"Rack with {rack_name} does not exist!"
            item = self.racks[rack_name].get()
            return item
        except KeyError as e:
            print(f"Error: Key {e} not found in the Rack list")
            
    
 
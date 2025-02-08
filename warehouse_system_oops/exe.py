from abstract import Warehouse

w = Warehouse(["Rack1", "Rack2"], 100)  # Initialize with rack names

w.add_item("Rack1", {"name": "abc", "id": "123", "priority": 2})
w.add_item("Rack2", {"name": "xyz", "id": "456", "priority": 3})

# ✅ Retrieve the Highest Priority Item from "Rack1"
retrieved_item = w.retrieve_item("Rack2")
print(retrieved_item)  # Should return the item with priority 2
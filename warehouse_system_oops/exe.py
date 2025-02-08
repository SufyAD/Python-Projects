from abstract import Warehouse

w = Warehouse(["Rack1", "Rack4"], 1)  # Initialize with rack names

print(w.add_item("Rack1", {"name": "abc", "id": "123", "priority": 2}))
print(w.add_item("Rack4", {"name": "xyz", "id": "456", "priority": 3}))

# # ✅ Retrieve the Highest Priority Item from "Rack1"
retrieved_item = w.retrieve_item("Rack4")
print(retrieved_item)  # Should return the item with priority 2
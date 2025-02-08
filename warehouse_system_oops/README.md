# 📦 Warehouse Management System

## 🚀 Overview
The **Warehouse Management System** is an optimized Python-based solution that efficiently manages inventory using **Priority Queues**. It ensures structured storage, retrieval, and tracking of items within warehouse racks while prioritizing high-importance items.

## 🏗️ Features
✅ **Priority-Based Storage** - Items are retrieved based on priority (lower values = higher priority).  
✅ **FIFO Order** - When two items have the same priority, retrieval follows First-In-First-Out (FIFO).  
✅ **Rack Capacity Management** - Prevents overfilling by enforcing rack-specific limits.  
✅ **Dynamic Storage & Retrieval** - Supports adding and retrieving items dynamically while maintaining queue integrity.  
✅ **Scalable Architecture** - Designed to support multiple racks with independent item tracking.  

## ⚙️ Tech Stack
- **Python 3.x** 🐍
- **PriorityQueue (from queue module)** ⏳
- **OOP Principles** (Encapsulation, Abstraction) 🔥
- **Data Structures** (Priority Queue, Dictionary, Tuple) 📊

## 🛠️ Installation & Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/SufyAD/Python-Projects.git
   cd Python-Projects
   ```
2. Ensure you have Python installed:
   ```bash
   python --version
   ```
3. Run the script:
   ```bash
   python warehouse.py
   ```

## 📜 Usage Guide
### **1️⃣ Initialize Warehouse**
```python
from warehouse import Warehouse
w = Warehouse(["Rack1", "Rack2"], capacity=100)
```

### **2️⃣ Add Items to Racks**
```python
item1 = {"name": "Laptop", "id": "123", "priority": 1}
w.add_item("Rack1", item1)
```

### **3️⃣ Retrieve High-Priority Items**
```python
retrieved_item = w.retrieve_item("Rack1")
print(retrieved_item)  # Returns the highest priority item
```

## ⏳ Time Complexity Analysis
| Operation         | Time Complexity |
|------------------|----------------|
| Add Item         | O(log N)        |
| Retrieve Item    | O(log N)        |
| Check Rack Space | O(1)            |

## 🔥 Future Enhancements
🔹 **Database Integration (PostgreSQL, MongoDB)** for persistent storage.  
🔹 **REST API** to expose warehouse operations via endpoints.  
🔹 **Web Dashboard** for real-time warehouse tracking.  

## 🤝 Contributing
Pull requests are welcome! Please open an issue first to discuss any feature updates.

## 📜 License
This project is licensed under the **MIT License**.

---
💡 *Optimized for efficiency, scalability, and reliability.* 🚀


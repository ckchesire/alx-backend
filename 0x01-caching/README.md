---
### **What a caching system is:**

A **caching system** is a mechanism that stores **frequently accessed data** in a **fast, temporary storage** (cache), so future requests for that data can be served more quickly. Instead of reprocessing or re-fetching data every time, a cache provides quick access, improving performance and reducing load on the main system.

---

### **What FIFO means (First-In, First-Out):**

FIFO is a **cache eviction policy** where the **oldest** item added to the cache is the **first** to be removed when the cache is full.

* Example: If you add items A → B → C, and the cache is full, then adding D will remove A (the first added).

---

### **What LIFO means (Last-In, First-Out):**

LIFO removes the **most recently added** item **first**. It’s like a stack.

* Example: If you add A → B → C, and the cache is full, then adding D will remove C (the last added).

---

### **What LRU means (Least Recently Used):**

LRU evicts the **least recently used** item in the cache.

* Example: If A, B, and C are in the cache and A hasn’t been used for a while, adding D will remove A.

---

### **What MRU means (Most Recently Used):**

MRU removes the **most recently used** item, the opposite of LRU.

* Example: If you just accessed item C, and the cache is full, C will be the one evicted to make space for a new item.

---

### **What LFU means (Least Frequently Used):**

LFU removes the item that has been **used the least number of times**.

* Example: If item A was accessed 2 times and B was accessed 5 times, A will be removed first when space is needed.

---

### **What the purpose of a caching system is:**

The main purposes are:

* **Speed**: Reduce latency by serving data quickly.
* **Efficiency**: Reduce repeated computation or database hits.
* **Scalability**: Help systems handle more users/requests without slowing down.

---

### **What limits a caching system has:**

1. **Memory/Storage Constraints**: Caches have limited space.
2. **Staleness**: Cached data might become outdated.
3. **Eviction Overhead**: Choosing what to evict can add complexity.
4. **Complexity**: Managing cache logic (like LRU or LFU) can be tricky.
5. **Cache Misses**: If data isn’t in the cache, performance can suffer.
6. **Consistency Issues**: In distributed systems, ensuring the cache matches the original data source can be hard.

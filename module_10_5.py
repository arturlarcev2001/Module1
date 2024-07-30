import multiprocessing as mp
from time import sleep

class WarehouseManager(mp.Process):

    data = {}

    def __init__(self):
        super().__init__()
        
    def process_request(self, requests):
        product_name = requests[0]
        product_act = requests[1]
        product_count = requests[2]
        if product_name not in WarehouseManager.data:
            WarehouseManager.data[product_name] = product_count
            
        
    def run(self, requests):
        for r in requests:
            p = mp.Process(target=self.process_request, args=(r, ))
            p.start()
            p.join()


if __name__ == "__main__":
    manager = WarehouseManager()

    requests = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

    manager.run(requests)
    print(manager.data)
        

class Bin:
    def __init__(self, bin_id, capacity):
        self.bin_id = bin_id
        self.capacity = capacity
        self.remaining = capacity
        self.objects = []

    def add_object(self, obj_id, size):
        self.remaining -= size
        self.objects.append(obj_id)

    def remove_object(self, obj_id, size):
        self.remaining += size
        self.objects.remove(obj_id)

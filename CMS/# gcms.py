# gcms.py
from Bin import Bin
from Avl import AVLTree
from object import Object, Color
from Exceptions import NoBinFoundException

class GCMS:
    def __init__(self):
        self.bins = AVLTree()  # Store bins by bin_id
        self.objects = AVLTree()  # Store objects by object_id

    def add_bin(self, bin_id, capacity):
        bin_obj = Bin(bin_id, capacity)
        self.bins.insert(bin_id, bin_obj)

    def add_object(self, object_id, size, color):
        obj = Object(object_id, size, color)
        eligible_bins = []

        def collect_bins(node):
            if node is None:
                return
            bin = node.value
            if bin.remaining_capacity >= size:
                eligible_bins.append(bin)
            collect_bins(node.left)
            collect_bins(node.right)

        collect_bins(self.bins.root)

        if not eligible_bins:
            raise NoBinFoundException()

        # Select bin according to color rules
        if color in [Color.BLUE, Color.YELLOW]:  # Compact Fit
            eligible_bins.sort(key=lambda b: (b.remaining_capacity, b.bin_id if color == Color.BLUE else -b.bin_id))
        else:  # Largest Fit
            eligible_bins.sort(key=lambda b: (-b.remaining_capacity, b.bin_id if color == Color.RED else -b.bin_id))

        selected_bin = eligible_bins[0]
        selected_bin.add_object(obj)
        obj.bin = selected_bin
        self.objects.insert(object_id, obj)

    def delete_object(self, object_id):
        node = self.objects.search(object_id)
        if node:
            obj = node.value
            obj.bin.remove_object(object_id)
            self.objects.delete(object_id)

    def object_info(self, object_id):
        node = self.objects.search(object_id)
        if node:
            return node.value.bin.bin_id
        return None

    def bin_info(self, bin_id):
        node = self.bins.search(bin_id)
        if node:
            bin = node.value
            return (bin.remaining_capacity, [obj.object_id for obj in bin.objects])
        return None

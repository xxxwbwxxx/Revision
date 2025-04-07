class Array:
    def __init__(self, size):
        self._size = size
        self._data = [None] * size

    def _setitem_(self, index, value):
        if 0 <= index < self._size:
            self._data[index] = value
        else:
            raise IndexError("Index out of range!")

    def _getitem_(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        else:
            raise IndexError("Index out of range!")
        
    def _len_(self):
        return self._size
    

arr = Array(10)
arr._setitem_(9, 10)
arr._getitem_(9)
print(arr._len_())
print(arr._data)
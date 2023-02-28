class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Capacity must be non-negative')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('You cannot deposit more than the capacity')
        if self.size + n > self.capacity:
            raise ValueError('Jar is full')
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError('You cannot withdraw more cookies than you have')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

jar = Jar()
jar.deposit(7)
print(jar)
jar.withdraw(2)
print(jar)

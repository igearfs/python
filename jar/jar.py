import emoji

class Jar:
    def __init__(self, capacity=12):
        if(capacity < 0):
            raise ValueError("Wrong capacity")
        self._capacity = capacity
        self._jar = []

    def __str__(self):
        cookies = ""
        for j in self._jar:
            cookies += emoji.emojize(j, language='alias')
        return cookies

    def deposit(self, n):
        after_adding_calculation = len(self._jar) + n
        if after_adding_calculation <= self._capacity:
            count = 0
            while count < n:
                self._jar.append(":cookie:")
                count += 1
        else:
            raise ValueError("Too many Cookies")

    def withdraw(self, n):
        if len(self._jar) >= n:
            count = 0
            while count < n:
                self._jar.pop(0)
                count += 1
        else:
            raise ValueError("Not Enough Cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return len(self._jar)
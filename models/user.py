from abc import ABC,abstractmethod
class User(ABC):
    __next_id=1
    def __init__(self,name):
        self._id=User.__next_id
        self.name=name
        User.__next_id+=1

    @property
    def id(self):
        return self._id
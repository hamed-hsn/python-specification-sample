from abc import ABC, abstractmethod
from specifications import CanSatisfied
from products import Product
from typing import List


class BaseFilter(ABC):

    def __init__(self, prodocts, specifaction:CanSatisfied):
        self._products = prodocts
        self._specification = specifaction

    @abstractmethod
    def filter(self):
        raise NotImplementedError("not implemented yet")


class CommonFilter(BaseFilter):
    def __init__(self, prodocts, specifaction:CanSatisfied):
        super().__init__(prodocts, specifaction)
    
    def filter(self):
        res:List[Product] = []
        for p in self._products:
            if self._specification.isSatisfied(p):
                res.append(p)
        return res
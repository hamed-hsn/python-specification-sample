from abc import ABC, ABCMeta, abstractmethod
from products import Product


class CanSatisfied(metaclass=ABCMeta):
    
    __methods__ = ('isSatisfied', )

    @classmethod
    def __subclasshook__(cls, subclass):
        for method in cls.__methods__:
            if not (hasattr(subclass, method) and callable(getattr(subclass, method))):
                return False
        return True

    @abstractmethod
    def isSatisfied(self, product:Product):
        raise NotImplementedError('[-] this method not implemented yet!')


class BaseSpecification(ABC, CanSatisfied):
    def __init__(self, subject):
        self._subject = subject
    
    @property
    def subject(self):
        return self._subject

    @abstractmethod
    def isSatisfied(self, procuct:Product):
        raise NotImplementedError("not implemented yet")


class BaseAggrigageSpec(ABC, CanSatisfied):

    def __init__(self, first:CanSatisfied, second:CanSatisfied):
        self._first = first
        self._second = second
    
    @abstractmethod
    def isSatisfied(self, product:Product):
        raise NotImplementedError("not implemented yet")
        

class ColorSpec(BaseSpecification):
    def __init__(self, subject):
        super().__init__(subject)
    
    def isSatisfied(self, procuct: Product):
        return self._subject == procuct.color


class PriceGreateThanSpec(BaseSpecification):
    def __init__(self, subject):
        super().__init__(subject)
    
    def isSatisfied(self, procuct: Product):
        return procuct.price > self._subject


class PriceGreateThanEqSpec(BaseSpecification):
    def __init__(self, subject):
        super().__init__(subject)

    def isSatisfied(self, procuct: Product):
        return procuct.price >= self._subject


class PriceLessThanSpec(BaseSpecification):
    def __init__(self, subject):
        super().__init__(subject)

    def isSatisfied(self, procuct: Product):
        return procuct.price < self._subject


class PriceLessThanEqSpec(BaseSpecification):
    def __init__(self, subject):
        super().__init__(subject)

    def isSatisfied(self, procuct: Product):
        return procuct.price <= self._subject



class AndSpec(BaseAggrigageSpec):
    def __init__(self, first:BaseSpecification, second:BaseSpecification):
        super().__init__(first, second)
        self._second = second
    
    def isSatisfied(self, procuct: Product):
        return self._first.isSatisfied(procuct) and self._second.isSatisfied(procuct)


class OrSpec(BaseAggrigageSpec):
    def __init__(self, first: CanSatisfied, second: CanSatisfied):
        super().__init__(first, second)
    
    def isSatisfied(self, product: Product):
        return self._first.isSatisfied(product) or self._second.isSatisfied(product)


class NotSpec(CanSatisfied):
    def __init__(self, spec:CanSatisfied):
        self._spec = spec
    
    def isSatisfied(self, product: Product):
        return not self._spec.isSatisfied(product)
from abc import ABC, abstractmethod
from typing import List, NewType, Optional

PhoneNumber = NewType('PhoneNumber', str)


def normalize(number: PhoneNumber) -> List[PhoneNumber]:
    candidates = []

    for normalizer in Normalizer.__subclasses__():
        if normalizer.is_eligible(number):
            candidates.append(normalizer.normalize(number))

    return candidates

class Normalizer(ABC):
    @staticmethod
    @abstractmethod
    def is_eligible(n: PhoneNumber) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def normalize(n: PhoneNumber) -> PhoneNumber:
        pass

class AlreadyNormalized(Normalizer):
    def is_eligible(n):
        return n.startswith(('+', '00'))

    def normalize(n):
        if n.startswith('+'):
            n = n[1:]

        if n.startswith('00'):
            n = n[2:]

        return n

class US(Normalizer):
    AREA_CODES = [
        '925',
    ]

    @staticmethod
    def is_eligible(n):
        return any((n.startswith(code) for code in US.AREA_CODES))

    @staticmethod
    def normalize(n):
        return '1' + n

def test(n, expected):
    actual = normalize(n)
    assert actual == expected, 'normalize({}) = {}; got: {}'.format(n, expected, actual)


test('+123', ['123'])
test('00123', ['123'])
test('+00123', ['123'])
test('9258766785', ['19258766785'])


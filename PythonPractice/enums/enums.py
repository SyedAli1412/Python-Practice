from enum import Enum


# Enums Demonstration using Class
class LanguageEnum(Enum):
    JS = 'Javascript'
    JAVA = 'Java'
    GO = 'Go'
    PHP = 'Php'


class OperationsEnum(Enum):
    AND = 'AND'
    OR = 'OR'
    XOR = 'XOR'
    COMPLEMENT = 'COMPLEMENT'
    LEFTSHIFT = 'LEFTSHIFT'
    RIGHTSHIFT = 'RIGHTSHIFT'

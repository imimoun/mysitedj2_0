from enum import Enum


class Token(Enum):   # A subclass of Enum
    joker = 0
    token_A = 1
    token_B = 3
    token_C = 3
    token_D = 2
    token_E = 1
    token_F = 4
    token_G = 2
    token_H = 4
    token_I = 1
    token_J = 8
    token_K = 10
    token_L = 1
    token_M = 2
    token_N = 1
    token_O = 1
    token_P = 3
    token_Q = 8
    token_R = 1
    token_S = 1
    token_T = 1
    token_U = 1
    token_V = 4
    token_W = 10
    token_X = 10
    token_Y = 10
    token_Z = 10

    @classmethod
    def choices(cls):
        return tuple((token[1].value, token[0]) for token in cls.__members__.items())

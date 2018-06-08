from enum import Enum


class Token(Enum):
    joker = ("joker", 0)
    token_A = ("A", 1)
    token_B = ("B", 3)
    token_C = ("C", 3)
    token_D = ("D", 2)
    token_E = ("E", 1)
    token_F = ("F", 4)
    token_G = ("G", 2)
    token_H = ("H", 4)
    token_I = ("I", 1)
    token_J = ("J", 8)
    token_K = ("K", 10)
    token_L = ("L", 1)
    token_M = ("M", 2)
    token_N = ("N", 1)
    token_O = ("O", 1)
    token_P = ("P", 3)
    token_Q = ("Q", 8)
    token_R = ("R", 1)
    token_S = ("S", 1)
    token_T = ("T", 1)
    token_U = ("U", 1)
    token_V = ("V", 4)
    token_W = ("W", 10)
    token_X = ("X", 10)
    token_Y = ("Y", 10)
    token_Z = ("Z", 10)

    @classmethod
    def choices(cls):
        return [(each.value[0], each.value[0]) for each in cls.__members__.values()]

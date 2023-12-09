from random import *
import CryptoDef

voting_options = {"No": 0, "Yes": 1, "Abstain": 2}


class Server:
    def __init__(self):

        self.used_users = set()

        while True:
            self.P = getrandbits(512)
            if CryptoDef.ferma(self.P):
                break
        # print("P = ", P)
        while True:
            self.Q = getrandbits(512)
            if CryptoDef.ferma(self.Q):
                break

        self.N = self.P * self.Q
        print("N:", self.N)
        phi = (self.P - 1) * (self.Q - 1)
        self.D = CryptoDef.generate_friend_simple_numper(phi)
        print("D:", self.D)
        self.__C = CryptoDef.gcd(self.D, phi)[1]
        while self.__C < 0:
            self.__C += phi
        self.voted = set()
        self.blanks = list()
        print(f'Сервер запущен')

    @staticmethod
    def connect_vote(self, _h, name):

        self.used_users.add(name)

        _s = pow(_h, self.__C, self.N)
        return _s

    @staticmethod
    def check_vote(server, n, s):
        if CryptoDef.sha(n) == pow(s, server.D, server.N):
            server.blanks.append((n, s))
            return True
        else:
            # print(CryptoDef.sha(n))
            # print(pow(s, server.D, server.N))
            return False

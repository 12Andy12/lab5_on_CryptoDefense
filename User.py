from random import getrandbits
import Server

import CryptoDef


class user:
    def __init__(self, name):
        self.name = name

    def vote(self, choice, server: Server.Server):
        rnd = getrandbits(256)
        v = Server.voting_options[choice]
        n = rnd << 257 | v
        r = CryptoDef.generate_friend_simple_numper(server.N)
        h = CryptoDef.sha(n)
        _h = h * pow(r, server.D, server.N) % server.N
        if self.name in server.used_users:
            print(f"{self.name} пытается проголосовать дважды")
            return
        print(f"{self.name} голосует . . . ")
        _s = Server.Server.connect_vote(server, _h, self.name)
        s = _s * CryptoDef.inverse(r, server.N) % server.N
        if Server.Server.check_vote(server, n, s):
            print(f"{self.name} успешно проголосовал")
        else:
            print(f"{self.name} не смог проголосовать")

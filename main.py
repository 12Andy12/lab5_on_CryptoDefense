import collections

import Server
import User


print((99*6**5)%119)
print((11*5**5)%119)

print(pow(13,77,119))
print(pow(103,77,119))

print(pow(6,-1,119))
print(pow(5,-1,119))

print((20*13) % 119)
print((24*52) % 119)

print(pow(99,77,119))
print(pow(11,77,119))



server = Server.Server()

user1 = User.user("Alica")
user1.vote("Yes", server)

user2 = User.user("Ivan")
user2.vote("No", server)

user3 = User.user("Andreyka")
user3.vote("Abstain", server)

user4 = User.user("Biba")
user4.vote("Yes", server)

user5 = User.user("Boba")
user5.vote("Yes", server)

user4.vote("Yes", server)
user5.vote("Yes", server)

print("\nПроголосовавшие:")
for vote in server.used_users:
    print(vote)
counter = collections.Counter()
for blank in server.blanks:
    # print(blank[0] & 3)
    counter[blank[0] & 3] += 1
print("\nРезультат голосования:")
print("За: \t\t ", counter[1])
print("Против:\t\t ", counter[0])
print("Воздержались:", counter[2])




class User(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


# インスタンスを作成
user1 = User(1, "Yohei")
user2 = User(2, "Satoshi")
user3 = User(3, "Kento")
user4 = User(1, "Shunji")  # idが一緒

# Setを作る
s = set([user1, user2, user3, user4])

# 中身を確認する
print(len(s))  # 3
for user in s:
    print(user.id, user.name)
    # 1 Yohei
    # 2 Satoshi
    # 3 Kento
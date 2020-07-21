import csv
import peewee

# データベースを指定
db = peewee.SqliteDatabase("user_tbl.db")

# ユーザーモデルを定義
class User(peewee.Model):
    user_id = peewee.TextField()
    name = peewee.TextField()
    age = peewee.IntegerField()
    address = peewee.TextField()

    class Meta:
        database = db

# ユーザーテーブル作成
User.create_table()

# tsvファイルを一行ずつ読み込んでタブで分割し，それぞれをデータベースに登録
with open("user_list.csv") as f:
    reader = csv.reader(f)
    for line in reader:
        (userId, userName, userAge, userAddress) = line
        if userAge.isdigit(): # 一行目のコメント対応．
            User.create(
                user_id = userId,
                name = userName,
                age = int(userAge),
                address = userAddress)

# 全部取得して画面に表示確認
print ("user list -----------------")
for user in User.select():
    print(vars(user))
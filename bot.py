from telegram import Bot


def read_token():
    with open("token.txt", "r") as f:
        return f.readline()


bot = None

if __name__ == "main":
    bot = Bot(token=read_token())

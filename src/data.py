import pickle
import time


class UserData:
    def __init__(self):
        self.health_days = 0
        self.sleep_time = []
        self.reset_time = []
        self.last_checkin = 0

    def checkin(self):
        self.health_days += 1
        self.sleep_time.append(time.time())
        self.last_checkin = time.time()

    def reset(self):
        self.health_days = 0
        self.sleep_time = []
        self.reset_time.append(time.time())
        self.last_checkin = time.time()

    def calc_rank(self, users):
        return sorted(users, key=lambda x: x.health_days, reverse=True).index(self) + 1


class Data:
    INSTANCE = None

    def __init__(self) -> None:
        self.users = {}
        self.group2users = {}

    def add_user_to_group(self, user_id: int, group_id: int):
        if group_id not in self.group2users:
            self.group2users[group_id] = []
        self.group2users[group_id].append(user_id)

    def get_users_checkedin_today(self, group_id=None) -> list:
        for (uid, userData) in self.users:
            if group_id is not None and self.group2users[group_id] is not None and not uid in self.group2users[group_id]:
                continue
            if userData.last_checkin >= time.time() - 86400


def load():
    try:
        with open("data.pickle", "rb") as f:
            Data.INSTANCE = pickle.load(f)
    except FileNotFoundError:
        save()


def save():
    if Data.INSTANCE is None:
        Data.INSTANCE = Data()
    with open("data.pickle", "wb") as f:
        pickle.dump(Data.INSTANCE, f)

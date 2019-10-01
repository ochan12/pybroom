
class Configuration:
    def __init__(self, name, tw_users, ig_users, fb_users, yt_users, keywords, banned_users,banned_content):
        self.tw_users = tw_users
        self.ig_users = ig_users
        self.fb_users = fb_users
        self.yt_users = yt_users
        self.keywords = keywords
        self.banned_content = banned_content
        self.banned_users = banned_users
        self.name = name

    def __init__(self, remote_config):
        for field in remote_config:
            self[field] = remote_config[field]
    
    def __getitem__(self, key):
        return getattr(self, key)

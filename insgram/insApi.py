# from instagram_web_api import Client
# web_api = Client(auto_patch=True, drop_incompat_keys=False)
# user_info = web_api.user_info2('kuohsingchun_official')
# print(user_info)

from MyClient import MyClient
web_api = MyClient(auto_patch=True, drop_incompat_keys=False)
user_info = web_api.user_info2('kuohsingchun_official')
print(user_info)
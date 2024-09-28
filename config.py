from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "183721dca18fce6ed2877fdcd1066a3a")
      API_ID = int(getenv("API_ID", "28607871"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7735764701:AAHzakUcn1EaZsUU0tdhZfmobmiqyRbmrtM")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001610472708:-1004510674591").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from AbingMusic import LOGGER, app, userbot
from AbingMusic.core.call import Yukki
from AbingMusic.plugins import ALL_MODULES
from AbingMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("AbingMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("AbingMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("AbingMusic.plugins" + all_module)
    LOGGER("AbingMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await Abing.start()
    try:
        await Abing.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("AbingMusic").error(
            "[ERROR] - \n\nHarap aktifkan Obrolan Suara di Grup Logger Anda. Pastikan Anda tidak pernah menutup/mengakhiri panggilan Obrolan suara di grup log Anda"
        )
        sys.exit()
    except:
        pass
    await Abing.decorators()
    LOGGER("AbingMusic").info("Abing Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("AbingMusic").info("Stopping Abing Music Bot! GoodBye")

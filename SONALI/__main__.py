import asyncio
import importlib

from pyrogram import idle

import config
from SONALI import LOGGER, app, userbot
from SONALI.core.call import RAUSHAN
from SONALI.misc import sudo
from SONALI.plugins import ALL_MODULES
from SONALI.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(name).error(
            "𝐒𝐭𝐫𝐢𝐧𝐠 𝐒𝐞𝐬𝐬𝐢𝐨𝐧 𝐍𝐨𝐭 𝐅𝐢𝐥𝐥𝐞𝐝, 𝐏𝐥𝐞𝐚𝐬𝐞 𝐅𝐢𝐥𝐥 𝐀 𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦 V2 𝐒𝐞𝐬𝐬𝐢𝐨𝐧🤬"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER(name).warning(f"Error loading banned users: {e}")

    await app.start()

    # Corrected module import
    for all_module in ALL_MODULES:
        try:
            importlib.import_module(f"SONALI.plugins.{all_module}")
        except Exception as e:
            LOGGER("SONALI.plugins").error(f"Failed to load module {all_module}: {e}")

    LOGGER("SONALI.plugins").info("𝐀𝐥𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞𝐬 𝐋𝐨𝐚𝐝𝐞𝐝 𝐁𝐚𝐛𝐲🥳...")
    
    await userbot.start()
    await RAUSHAN.start()
    await RAUSHAN.decorators()
    LOGGER("SONALI").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️ 𝗧𝗛𝗘 𝗨𝗡𝗢𝗙𝗙𝗖𝗜𝗔𝗟 𝗡𝗘𝗧𝗪𝗢𝗥𝗞  ♨️\n╚═════ஜ۩۞۩ஜ════╝")
    
    await idle()
    await app.stop()
    await userbot.stop()
    
    LOGGER("SONALI").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️ 𝗧𝗛𝗘 𝗨𝗡𝗢𝗙𝗙𝗖𝗜𝗔𝗟 𝗡𝗘𝗧𝗪𝗢𝗥𝗞 ꪜ ♨️\n╚═════ஜ۩۞۩ஜ════╝")


if name == "main":
    asyncio.get_event_loop().run_until_complete(init())

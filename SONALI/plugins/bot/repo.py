from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ Tᴀᴍᴀɴɴᴀ 𝐌ᴜsɪᴄ 

❥ ʙᴏᴛ ᴡɪᴛʜ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs
│❍ • ʏᴏᴜ ᴄᴀɴ ᴘʟᴀʏ ᴍᴜꜱɪᴄ + ᴠɪᴅᴇᴏ •
│❍ • ʙᴇsᴛ ǫᴜɪʟɪᴛʏ ᴍᴜsɪᴄ sᴏᴜɴᴅ •
│❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs •
│❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ •
├──────────────

"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url=f"https://t.me/TAMANNA_MUSIC_BOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗣𝗶𝗰𝗸 𝘂𝗽 𝗹𝗶𝗻𝗲𝘀", url="https://t.me/ll_P_U_L_lI"),
          InlineKeyboardButton("𝗨𝗡𝗢𝗙𝗙𝗖𝗜𝗔𝗟 𝗡𝗘𝗧𝗪𝗢𝗥𝗞", url="https://t.me/UFC_NETWORK"),
          ],
               [
                InlineKeyboardButton("𝗨𝗙𝗖 𝗟𝗜𝗡𝗞 𝗭𝗢𝗡𝗘", url=f"https://t.me/UFC_LINK_ZONE"),
],
[
InlineKeyboardButton("ᴄʜᴇᴄᴋ", url=f"https://t.me/UFC_LINK_ZONE"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://files.catbox.moe/odegyd.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )

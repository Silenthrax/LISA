from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from SONALI import app
from config import BOT_USERNAME
from SONALI.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
❥ ωєℓ¢σмє тσ Sɪʟᴇɴᴛʜʀᴀx 𝐌ᴜsɪᴄ 

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
          InlineKeyboardButton("💠 𝖠ᴅᴅ ᴍᴇ 𝖡ᴀʙʏ 💠", url=f"https://t.me/LISA_UFC_BOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗟𝗶𝘀𝗮 𝗠𝘂𝘀𝗶𝗰 ♪", url="https://t.me/BESTIE_UNITE_CLUB"),
          InlineKeyboardButton("ᴇʟɪᴢᴀ ᴍᴜꜱɪᴄ", url="https://t.me/ELIZA_UFC_BOT?startgroup=true"),
          ],
               [
                InlineKeyboardButton("𝟵𝟮.𝟳 𝗕𝐈𝗚 𝗙𝗠🎧 ", url=f"https://t.me/RJ_92_MUSIC_BOT?startgroup=true"),
],
[
InlineKeyboardButton("𝐒ɪʏʌ 𝐌ᴜꜱɪᴄ", url=f"https://t.me/SIYA_UFC_ROBOT?startgroup=true"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_video(
        video="https://files.catbox.moe/xiffuv.mp4",
        caption=start_txt,
        reply_markup=reply_markup
    )

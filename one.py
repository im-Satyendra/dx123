from http import client
from numpy import block
from pyrogram import Client, filters
import time
from pyrogram import idle
import os
import time
import math

async def progress_for_pyrogram(
    current,
    total,
    ud_type,
    message,
    start
):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "{0}{1}".format(
            ''.join(["▣" for i in range(math.floor(percentage / 5))]),
            ''.join(["▢" for i in range(20 - math.floor(percentage / 5))]))

        PROGRESS_DIS = """
PROG: {}
CURRENT: {}
TOTAL: {}
SPEED: {}
TIME: {}"""
        tmp = progress + PROGRESS_DIS.format(
                  round(percentage, 2),
                  humanbytes(current),
                  humanbytes(total),
                  humanbytes(speed),
                  estimated_total_time if estimated_total_time != '' else "0 s")


        try:
            await message.edit(
                text="{}\n{}".format(ud_type, tmp))

        except:
            pass

def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: '<i>K</i>', 2: '<i>M</i>', 3: '<i>G</i>', 4: '<i>T</i>'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + '<i>B</i>'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]

Bot1 = Client(
    "Simpleachu1",
    bot_token="1814624231:AAFr1cp1MGKCaC2spPrbJFN6FoNt1MMso5w",
    api_id=2171111,
    api_hash="fd7acd07303760c52dcc0ed8b2f73086"
)
Bot2 = Client(
    "Simpleachu2",
    bot_token="5154860805:AAEZs1rWayks2zJF4y1LeYoQb_r7ApDSMBU",
    api_id=2171111,
    api_hash="fd7acd07303760c52dcc0ed8b2f73086"
)
Bot4 = Client(
    "Simpleachu4",
    bot_token="5217702275:AAH0KwikoXAzjEc7qO8V9XiH1-gnTAVnFF4",
    api_id=2171111,
    api_hash="fd7acd07303760c52dcc0ed8b2f73086"
)
Bot5 = Client(
    "Simpleachu5",
    bot_token="5263754363:AAFdmNpmqjZj3d0psXivJR11ni54mXmUWPU",
    api_id=2171111,
    api_hash="fd7acd07303760c52dcc0ed8b2f73086"
)
@Bot1.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )
@Bot1.on_message(filters.command(["d","r","rename"]))
async def rn(c,m):
  try:
    if (" " in m.text) and (m.reply_to_message is not None):
        fn = file_name = m.text.split(" ", 1)[1]
        c_time = time.time()
        cm = await c.send_message(m.chat.id,"Downloading...")
        dl = await c.download_media(
        message=m.reply_to_message,
        file_name=fn,
        block=True,
        progress=progress_for_pyrogram,
        progress_args=("downloading..", cm, c_time))
        await c.send_document(
        chat_id=m.chat.id,
        document=dl,
        reply_to_message_id=m.reply_to_message.message_id,
        progress=progress_for_pyrogram,
        progress_args=("uploading..", cm, c_time))
    else:
        await m.reply_text("error: reply to media or gibe file name with ext")
  except Exception as e:
      await c.send_message(m.chat.id,e)
@Bot2.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )
@Bot2.on_message(filters.command(["d","r","rename"]))
async def rn(c,m):
  try:
    if (" " in m.text) and (m.reply_to_message is not None):
        fn = file_name = m.text.split(" ", 1)[1]
        c_time = time.time()
        cm = await c.send_message(m.chat.id,"Downloading...")
        dl = await c.download_media(
        message=m.reply_to_message,
        file_name=fn,
        block=True,
        progress=progress_for_pyrogram,
        progress_args=("downloading..", cm, c_time))
        await c.send_document(
        chat_id=m.chat.id,
        document=dl,
        reply_to_message_id=m.reply_to_message.message_id,
        progress=progress_for_pyrogram,
        progress_args=("uploading..", cm, c_time))
    else:
        await m.reply_text("error: reply to media or gibe file name with ext")
  except Exception as e:
      await c.send_message(m.chat.id,e)
@Bot4.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )
@Bot4.on_message(filters.command(["d","r","rename"]))
async def rn(c,m):
  try:
    if (" " in m.text) and (m.reply_to_message is not None):
        fn = file_name = m.text.split(" ", 1)[1]
        c_time = time.time()
        cm = await c.send_message(m.chat.id,"Downloading...")
        dl = await c.download_media(
        message=m.reply_to_message,
        file_name=fn,
        block=True,
        progress=progress_for_pyrogram,
        progress_args=("downloading..", cm, c_time))
        await c.send_document(
        chat_id=m.chat.id,
        document=dl,
        reply_to_message_id=m.reply_to_message.message_id,
        progress=progress_for_pyrogram,
        progress_args=("uploading..", cm, c_time))
    else:
        await m.reply_text("error: reply to media or gibe file name with ext")
  except Exception as e:
      await c.send_message(m.chat.id,e)
@Bot5.on_message(filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=f"Hi {update.from_user.mention}"
    )
@Bot5.on_message(filters.command(["d","r","rename"]))
async def rn(c,m):
  try:
    if (" " in m.text) and (m.reply_to_message is not None):
        fn = file_name = m.text.split(" ", 1)[1]
        c_time = time.time()
        cm = await c.send_message(m.chat.id,"Downloading...")
        dl = await c.download_media(
        message=m.reply_to_message,
        file_name=fn,
        block=True,
        progress=progress_for_pyrogram,
        progress_args=("downloading..", cm, c_time))
        await c.send_document(
        chat_id=m.chat.id,
        document=dl,
        reply_to_message_id=m.reply_to_message.message_id,
        progress=progress_for_pyrogram,
        progress_args=("uploading..", cm, c_time))
    else:
        await m.reply_text("error: reply to media or gibe file name with ext")
  except Exception as e:
      await c.send_message(m.chat.id,e)
Bot = [Bot1,Bot2,Bot4,Bot5]
for i in Bot:
    i.start()
    idle()

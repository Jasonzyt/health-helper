import asyncio

from .data import Data, UserData
from telegram import Update
from telegram.ext import ContextTypes


def _process_cmd(cmd: str, params: list, update: Update) -> None:
    if cmd == "打卡":
        if Data.INSTANCE.users[update.effective_user.id] is None:
            Data.INSTANCE.users[update.effective_user.id] = UserData()
        health_days = Data.INSTANCE.users[update.effective_user.id].checkin()
        text = f"打卡成功！\n你已经保持健康了 {health_days} 天！"
        if update.effective_chat.type == "group":
            Data.INSTANCE.group2users[update.effective_chat.id]
        update.message.reply_text()


async def message_callback(update: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    usr = update.effective_user
    chat = update.effective_chat
    msg = update.message
    if usr is None or chat is None or msg is None:
        return
    if msg.text is None:
        return
    text = msg.text.strip()
    parts = text.split()
    if len(parts) <= 1:
        return
    cmd = parts[0]
    params = parts[1:]
    if cmd.startswith("#"):
        cmd = cmd[1:]
        _process_cmd(cmd, params, update)

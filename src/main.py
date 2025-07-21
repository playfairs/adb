import discord_ios
import logging
import jishaku
import os
from pathlib import Path
from discord.ext import commands
from discord import Intents, AllowedMentions
from dotenv import load_dotenv
from config import DISCORD

load_dotenv()

jishaku.Flags.HIDE = True
jishaku.Flags.RETAIN = True
jishaku.Flags.NO_DM_TRACEBACK = True
jishaku.Flags.NO_UNDERSCORE = True
jishaku.Flags.FORCE_PAGINATOR = True

log = logging.getLogger(__name__)


class adb(commands.AutoShardedBot):

    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            command_prefix=DISCORD.PREFIX,
            shard_count=None,
            case_insensitive=True,
            intents=Intents(
                guilds=True,
                members=True,
                messages=True,
                reactions=True,
                # presences=True,
                moderation=True,
                message_content=True,
                emojis_and_stickers=True,
                voice_states=True,
            ),
            allowed_mentions=AllowedMentions(
                everyone=False, users=True, roles=False, replied_user=True
            ),
        )
        self.owner_id = DISCORD.OWNER_ID

    def run(self) -> None:
        log.info("Starting adb.")
        super().run(os.getenv("TOKEN"), reconnect=True)

    async def load_extensions(self) -> None:
        await self.load_extension("jishaku")
        
        try:
            await self.load_extension("cogs.commands")
            print("Successfully loaded cogs.commands")
        except Exception as e:
            print(f"Failed to load cogs.commands: {e}")
            raise

    async def setup_hook(self):
        await self.load_extensions()
        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")
        print("Bot is ready!")
        print("Use /adb or /info to test the commands")

    async def get_prefix(self, message):
        return commands.when_mentioned_or(DISCORD.PREFIX)(self, message)

    async def process_commands(self, message):
        ctx = await self.get_context(message)
        if ctx.command is not None:
            ctx.invoked_with = ctx.invoked_with.lower()
            if ctx.command == "help" and "help" in ctx.command.aliases:
                if len(ctx.args) > 2:
                    ctx.args = list(ctx.args)
                    ctx.args[2] = ctx.args[2].lower()
        await self.invoke(ctx)

if __name__ == "__main__":
    bot = adb()
    bot.run()

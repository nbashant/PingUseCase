from webex_bot.webex_bot import WebexBot
from Chippy import chippy
from Chippy import HelpCommand

bot = WebexBot("Zjc0YjVhOTAtYTAxYi00NGUwLWExZGQtY2EzYzZhMmU3NTlmYWI5NTcxNDgtMmNl_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f")

bot.add_command(chippy())

bot.help_command = HelpCommand()

bot.run()


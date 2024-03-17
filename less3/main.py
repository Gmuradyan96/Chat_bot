import asyncio
import config
from aiogram import Bot, Dispatcher
import logging
from less3.handlers import career_choice, common


async def main():
    #Logging in
    logging.basicConfig(level=logging.INFO)

    #Create bot`s structure
    bot = Bot(token=config.token)

    #Dispatcher
    dp = Dispatcher()
    dp.include_router(common.router)
    dp.include_router(career_choice.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

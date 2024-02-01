from TikTokApi import TikTokApi
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
SPIDEY_MAIN = "shearingshedvlogs" 
SPIDEY_BACKUP = "turan.spidey"
SPIDEY_ALTS = [
    "spideywilliam",
    "spideyturan",
    "shearingshed",
] 

ms_token = os.environ.get(
    "MS_TOKEN_A", None
)

if not ms_token:
    raise Exception("No MS token")


async def user_example():
    async with TikTokApi() as api:
        await api.create_sessions(ms_tokens=[ms_token], num_sessions=1, sleep_after=3)
        user = api.user(SPIDEY_MAIN)
        user_data = await user.info()
        print(user_data)

        async for video in user.videos(count=30):
            print(video)
            print(video.as_dict)


if __name__ == "__main__":
    asyncio.run(user_example())

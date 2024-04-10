import os
from poe_api_wrapper import AsyncPoeApi
import asyncio

# Reading environment variables
b_token = os.getenv('B_TOKEN')
lat_token = os.getenv('LAT_TOKEN')

tokens = {
    'b': b_token, 
    'lat': lat_token
}

async def main():
    client = await AsyncPoeApi(cookie=tokens).create()
    message = "Italicize every third word in this text by using Markdown syntax: \"This is just a test. Just a test.\""
    async for chunk in client.send_message(bot="gpt3_5", message=message):
        print(chunk["response"], end='', flush=True)
        
asyncio.run(main())


import asyncio
import aiohttp
import aiofiles

import time

async def download_and_save_picture(session, url, filename):
    async with session.get(url) as response:
        async with aiofiles.open(filename, 'wb') as file:
            content = await response.content.read()
            await file.write(content)

async def main():
    n = int(input())
    start_time = time.time()
    url = "https://thispersondoesnotexist.com/"
    file_directory_path = '../random_photos'
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[download_and_save_picture(session, url, filename=f"{file_directory_path}/{i}.jpeg") for i in range(n)])
    end_time = time.time()
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")

if __name__ == "__main__":
    asyncio.run(main())
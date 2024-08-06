import asyncio
import aiofiles
import aiohttp
import ssl


async def req(url, index, semph):
    semaphore = asyncio.Semaphore(semph)
    async with semaphore:
        conn = aiohttp.TCPConnector(ssl=False)  # Отключаем проверку SSL
        async with aiohttp.ClientSession(connector=conn) as session:
            try:
                async with session.get(url) as resp:
                    status_code = f"Код ответа для запроса {index}, {resp.status}"
                    async with aiofiles.open(f"status_info_{index}", "w") as file:
                        await file.write(status_code)
            except Exception as e:
                print(f"Error: {e}")


async def main():
    tasks = [req("https://example.com/", i, 10) for i in range(50)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

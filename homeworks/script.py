import asyncio
import aiofiles

# Напишите скрипт который создаст параллельно 10 файлов с именем
# `file_ {index}.txt' и записывает их номер внутрь файла.


semaphore = asyncio.Semaphore(2)


async def script(ind):
    file_name = f"It {ind} file"
    async with semaphore:
        async with aiofiles.open(file_name, "w") as file:
            await file.write(f"This {ind} file")


async def main():
    tasks = [script(i) for i in range(5)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())

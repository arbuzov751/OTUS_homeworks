"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def task_master():
    task_users = asyncio.create_task(fetch_json(USERS_DATA_URL))
    task_posts = asyncio.create_task(fetch_json(POSTS_DATA_URL))
    data = await asyncio.gather(task_users, task_posts)
    return data


def main():
    asyncio.run(task_master())

#
# if __name__ == "__main__":
#     main()

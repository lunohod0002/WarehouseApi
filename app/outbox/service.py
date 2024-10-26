# from app.outbox.producer import send_messages
import schedule
from app.outbox.dao import OutBoxDao
from app.outbox.producer import send_messages
import asyncio

'''class OutBoxService():
    @classmethod
    async def create(cls,data):
        return await OutBoxDao.add(**data)'''


async def background_task():
    while True:
        print("Обработка эвентов...")
        data=await OutBoxDao.get_all_pending()
        send_messages(data=data["payload"])
        for id in data["id"]:
            await OutBoxDao.update_status(id=id)
        print(f"Обработано эвентов {len(data)}")
        await asyncio.sleep(5)

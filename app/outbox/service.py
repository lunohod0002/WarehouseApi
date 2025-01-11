# from app.outbox.producer import send_messages
import logging
from ast import literal_eval

import schedule
from app.outbox.dao import OutBoxDao
from app.outbox.producer import send_messages
import asyncio
from app.outbox.consumer import get_messages



async def background_task():
    await asyncio.sleep(15)

    while True:
        try:
            await asyncio.sleep(8)
            logging.error("Обработка эвентов...")
            data=await OutBoxDao.get_all_pending()
            logging.error(data)
            payload_data=[]
            rows_id=[]

            for data_row in data :
                payload_data.append(literal_eval(data_row["payload"]))
                rows_id.append(data_row["id"])

            if len(data)!=0:
                send_messages(data=payload_data)
                for id in rows_id:

                    await OutBoxDao.update_status(id=int(id))
            logging.error(f"Обработано эвентов {len(data)}")
            get_messages()
        except Exception as e:
            logging.exception(str(e))


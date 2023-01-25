import asyncio
from datetime import datetime
from time import perf_counter

from service.users import get_users
from db.db import session


def create_html(counter, during):
    html = f"""
        <html>
            <head>
                <title>Report</title>
            </head>
            <body>
                <h4>Number of sent messages: {counter}</h4>
                <h4>Completed in: {during} seconds</h4>
            </body>
        </html>
    """
    time = datetime.now().strftime("%Y%m%d-%H%M%S")
    with open(f'report_{time}.html', 'w') as f:
        f.write(html)


async def send_message(app):
    start = perf_counter()
    users = await get_users(session)
    if not users:
        return
    counter = 0
    for user in users:
        await app.send_message(user.tg_id, "privet")
        await asyncio.sleep(0.1)
        counter += 1
        if counter == 1000:
            break
    end = perf_counter()
    during = round(end - start, 2)
    create_html(counter, during) # Отчет в html формате
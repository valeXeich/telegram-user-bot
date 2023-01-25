from db.db import Base, engine


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
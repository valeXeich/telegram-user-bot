from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from db.models import User


async def get_users(session: AsyncSession):
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()
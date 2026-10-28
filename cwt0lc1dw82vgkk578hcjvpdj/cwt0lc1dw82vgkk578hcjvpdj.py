from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import async_sessionmaker as SessionMaker, AsyncSession as Session
from sqlmodel.ext.asyncio.session import AsyncSession

import nz92c2w8z2f8udlci6ravpn7t as the_engine


async def cwt0lc1dw82vgkk578hcjvpdj() -> AsyncGenerator[Session, None]:
    _session_maker_: SessionMaker[Session] = SessionMaker(
        the_engine._, class_=AsyncSession, expire_on_commit=False
    )
    async with _session_maker_() as _session_:
        yield _session_

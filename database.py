import aiosqlite
import asyncio
async def createDB():
    async with aiosqlite.connect('user.db') as db:
        await db.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT)')
        await db.commit()
        await db.close()

async def save(usermame, passw):
    async with aiosqlite.connect('user.db') as db:
        await db.execute('INSERT INTO users(username, password) VALUES(?,?)', (usermame, passw))
        await db.commit()
        await db.close()

async def getUser():
    async with aiosqlite.connect('user.db') as db:
        cur = await db.execute('SELECT username')
        return await cur.fetchall()


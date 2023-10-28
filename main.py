from pyrogram import Client
app = Client("MyBot", api_id = 8, api_hash = "7245de8e747a0d6fbe11f7cc14fcc0bb",
             bot_token= "6780239837:AAH0CHShG6N8zYdp6j-rio97sKboOsAPQMw")

@app.on_message()
async def viewCount(client, message):
  await message.reply("Views on this post: %s"%message.views if message.views
                      else "This is not a message forwarded from a channel")

app.run()

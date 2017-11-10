import telepot
import time

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print 'Got command: %s' % command

    if(command == "ping"):
        bot.sendMessage(chat_id,"pong")
        print"pong"
    if(command == "hi"):
        bot.sendMessage(chat_id,"hello dude")

bot = telepot.Bot('459118198:AAHzngRi3JT8DeShfRjr-9FLzpYl-T9g2xo')
bot.message_loop(handle)


while 1:
     time.sleep(10)

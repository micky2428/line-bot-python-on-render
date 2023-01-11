from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('b+YZPLfqivSa3tY+uUr0nPP6tI4i3U6wChIrcjhIs6UlsdSF56k1S8E7EdDpvjRj8edR2U7bF9yDOjzcLqK7nG2ANizVg1XWHl+QxI8OLajHKteoE4Jprd3ZWRfDLgyIOll2KVNj6a0BbdckA0xtEwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fb9bfa5297b2c04a610fde0caf3f74a5')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext =='＠使用說明':
        message = TextSendMessage(text='''歡迎使用小廢柴2.0🙌 
        在這裡您將可以拯救你的眼睛～
        請輸入查核表的編號🤖
        您將收到對應的圖片''')
        line_bot_api.reply_message(
            event.reply_token,
            message)   
    
    elif re.match('1', message):
            image_message = ImageSendMessage(
            original_content_url='https://drive.google.com/drive/my-drive?hl=zh-tw',
            preview_image_url='https://drive.google.com/drive/my-drive?hl=zh-tw'
            )
            line_bot_api.reply_message(event.reply_token, image_message)
    
    elif re.match('2', message):
        image_message = ImageSendMessage(
        original_content_url='https://i.imgur.com/9d0O0Jh.jpg',
        preview_image_url='https://i.imgur.com/9d0O0Jh.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)

            
            

if __name__ == "__main__":
    app.run()

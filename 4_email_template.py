# %%

import win32com.client as client

outlook = client.Dispatch('Outlook.Application')
message = outlook.CreateItem(0)
message.Display()

message.To = 'test@gmail.com'
message.Subject = 'Test Subject'

html_body = """
    <div>
        <h1 style="font-family: 'Lucida Handwriting'; font-size: 56; font-weight: bold; color: #9eac9c;">
            Happy Birthday!! 
        </h1>
        <span style="font-family: 'Lucida Sans'; font-size: 28; color: #8d395c;">
            {}, wishing you all the best on your birthday!!
        </span>
    </div><br>
    <div>
        <img src="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/cute-birthday-instagram-captions-1584723902.jpg" width=50%>
    </div>
    """

message.HTMLBody = html_body
message.HTMLBody = html_body.format('Richard')
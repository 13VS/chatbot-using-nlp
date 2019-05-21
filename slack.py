from slacker import Slacker
import pandas as pd
import time

df=pd.read_excel('data.xlsx',sheet_name='config')
d=dict(zip(df.name,df.value))
slack_token=d['slack_token']
channel_name=d['channel_name']
bot_name=d['bot_name']
bot_pic=d['bot_pic']
        

def connect():
        conn=Slacker(slack_token)
        # Check for success
        if conn.api.test().successful:
            print(f"Connection between Bot and Slack has established Successfully in {conn.team.info().body['team']['name']}.")
            return conn
        else:
            print("Connection hasn't established. Try Again!")
            return None
    
# To send message to User
def post_message(conn,message):
	conn.chat.post_message(channel=channel_name,text=message,username=bot_name,icon_url=bot_pic)
	time.sleep(3)
	
# To retrieve message from User
def get_message(conn):
    while True:
        #To get Latest Conversation of user
        r=conn.channels.history(conn.channels.get_channel_id(channel_name))
        conversation_history = r.body
        latest_conversation=conversation_history['messages'][0]
        if 'client_msg_id' in latest_conversation.keys():
            #To get user name of the latest conversation
            users_list=conn.users.list()
            details=users_list.body
            user_name=[i['real_name'] for i in details['members'] if i['id']==latest_conversation['user']]
            break
        time.sleep(3)
    return latest_conversation['text'],user_name[0]


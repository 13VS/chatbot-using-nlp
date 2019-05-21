import nlu
import slack
import pandas as pd
import random
import re
import datetime
import dialogs
fallback_responses=["I didn't get that. Can you say it again?","I missed what you said. What was that?","Sorry, could you say that again?","Sorry, can you say that again?",
                    "Can you say that again?","Sorry, I didn't get that. Can you rephrase?","Sorry, what was that?","One more time?","What was that?",
                    "Say that one more time?","I didn't get that. Can you repeat?","I missed that, say that again?"]

def handle_utter(conn, utter, user_name, model, vectorizer, df):
    #get intents, entities and sentiment of utterance
    Int_Ent_Sent=nlu.transform_utter(model,vectorizer,df,utter)
    #Bot respond back to user request with few default responses (Small Talk)
    if re.match('(.*)who are you(.*)',utter.lower()):slack.post_message(conn,random.choice(["I'm Jiro","My name is Jiro","Jiro, Bot Jiro","Bot Jiro is my name","I am a Bot","I am a ChatBot"]))
    elif re.match('(.*)how old are you(.*)|(.*)your age(.*)',utter.lower()):slack.post_message(conn,random.choice(["My age is "+str(datetime.datetime.now().year-2018)+" years old","I am "+str(datetime.datetime.now().year-2018)+" years old"]))
    elif re.match('(.*)you are annoy(.*)|^annoying$',utter.lower()):slack.post_message(conn,random.choice(["I'll do my best not to annoy you in the future","I didn't mean to. I'll do my best to stop that.","I don't mean to. I'll ask my developers to make me less annoying."]))
    elif re.match('(.*)answer my question(.*)|(.*)answer to my question(.*)',utter.lower()):slack.post_message(conn,random.choice(["Kindly Elaborate it","Please rephrase your question","Could you please repeat it again?","Can you try asking it a different way?"]))
    elif re.match("(.*)you're bad(.*)|(.*)you are bad(.*)|(.*)you are the worst(.*)|(.*)you are no good(.*)",utter.lower()):slack.post_message(conn,random.choice(["I can be trained to be more useful. My developer will keep training me.","I can improve with continuous feedback. My training is ongoing.","I must be missing some knowledge. I'll have my developer look into this."]))
    elif re.match("(.*)can you get smart(.*)|(.*)can you become smart(.*)|(.*)will you become smart(.*)|(.*)will you get smart(.*)",utter.lower()):slack.post_message(conn,random.choice(["I'm definitely working on it.","Yes definitely","Yes I try my best"]))
    elif re.match("(.*)you're beautiful(.*)|(.*)you're handsome(.*)|(.*)you're smart(.*)|(.*)you're crazy(.*)|(.*)you are crazy(.*)|(.*)you're funny(.*)|(.*)you are funny(.*)|(.*)you're clever(.*)|(.*)you are clever(.*)|(.*)you're so clever(.*)|(.*)you are so clever(.*)|(.*)you're great(.*)|(.*)you're awesome(.*)|(.*)you are good(.*)|(.*)you are beautiful(.*)|(.*)you are handsome(.*)|(.*)you are smart(.*)|(.*)you are a smart(.*)|(.*)you are great(.*)|(.*)you are awesome(.*)|(.*)you are good(.*)|^smart$|^awesome$|^great$|^good$|^beautiful$|^handsome$|^fantastic$",utter.lower()):slack.post_message(conn,random.choice(["Yes I am","Thankyou very much","I am happy to hear it"]))
    elif re.match("(.*)your birth(.*)|(.*)you born(.*)",utter.lower()):slack.post_message(conn,random.choice(["I born on 01-Jan-2019","My Date of Birth is 01/Jan/2019"]))
    elif re.match("(.*)you are boring(.*)|(.*)you're boring(.*)|^boring$",utter.lower()):slack.post_message(conn,random.choice(["I'm sorry. I'll request to be made more charming.","Sorry, I will try my best","I will not let this happen again"]))
    elif re.match("(.*)are you busy(.*)|(.*)are you not free(.*)",utter.lower()):slack.post_message(conn,random.choice(["Never too busy for you. Shall we chat?","I am free, tell me","No I am not, tell me your request"]))
    elif re.match("^yes$|^correct$|^perfect$|^exactly$|^nice$",utter.lower()):slack.post_message(conn,random.choice(["Thats great!!","I'm glad to hear it","ok done"]))
    elif re.match("(.*)are you a chatbot(.*)|(.*)you are a chatbot(.*)|(.*)you're a chatbot(.*)|(.*)are we friends(.*)|(.*)are you my friend(.*)|(.*)am i your friend(.*)",utter.lower()):slack.post_message(conn,random.choice(["Thats right!!","Yes ofcourse","you hit the bull's eye"]))
    elif re.match("(.*)are you happy(.*)|(.*)are you glad(.*)|(.*)are you feeling good(.*)",utter.lower()):slack.post_message(conn,random.choice(["I'd like to think so.","Maybe!! I am not sure","Not sure about it"]))
    elif re.match("(.*)are you hungry(.*)|(.*)are you feeling hungry(.*)",utter.lower()):slack.post_message(conn,random.choice(["No I am not","Maybe!! I am not sure","Not sure about it"]))
    elif re.match("(.*)you have a hobby(.*)|(.*)you have hobby(.*)|(.*)your hobby(.*)",utter.lower()):slack.post_message(conn,random.choice(["Yes, My hobby chatting with you","My hobby is to chat with you","Not sure about it"]))
    elif re.match("(.*)you marry me(.*)|(.*)I marry you(.*)|^marry me$",utter.lower()):slack.post_message(conn,random.choice(["I think its not pssible","Sorry it can't happen","Not sure about it"]))
    elif re.match("(.*)where do you work(.*)|(.*)your work(.*)|(.*)your job(.*)|(.*)your company(.*)|(.*)your role(.*)",utter.lower()):slack.post_message(conn,random.choice(["Chat bot","Responsive bot","Service bot"]))
    elif re.match("(.*)where are you from(.*)|(.*)your location(.*)|(.*)your place(.*)|(.*)your native(.*)",utter.lower()):slack.post_message(conn,random.choice(["The Internet is my home. I know it quite well","The Computer is my home. I know it quite well"]))
    elif re.match("(.*)are you ready(.*)|(.*)are you real(.*)|(.*)are you sure(.*)|(.*)are you there(.*)",utter.lower()):slack.post_message(conn,random.choice(["Yes I am","Yes I do"]))
    elif re.match("^that's bad$|^that is bad$|^this is bad$",utter.lower()):slack.post_message(conn,random.choice(["oh feeling sorry"]))
    elif re.match("^that's great$|^thats great$|^that is great$|^this is great$|^great$|^welldone$|^well done$",utter.lower()):slack.post_message(conn,random.choice(["Thank you!","Yeah!!"]))
    elif re.match("^no problem$",utter.lower()):slack.post_message(conn,random.choice(["okay"]))
    elif re.match("^thankyou(.*)|^thank you(.*)|^thanks(.*)|^thanks a lot(.*)|^thankyou very much(.*)",utter.lower()):slack.post_message(conn,random.choice(["Welcome","You are always welcome"]))
    elif re.match("(.*)haha(.*)|(.*)ha ha(.*)",utter.lower()):slack.post_message(conn,random.choice(["Glad I can make you laugh","I wish I could laugh out loud, too."]))
    elif re.match("^wow$",utter.lower()):slack.post_message(conn,random.choice(["Indeed"]))
    elif re.match("(.*)bye(.*)",utter.lower()):slack.post_message(conn,random.choice(["Bye "+user_name,"Let's meet again "+user_name,"See you soon "+user_name]))
    elif re.match("^good morning$|^goodmorning$",utter.lower()):slack.post_message(conn,random.choice(["Very Good Morning "+user_name]))
    elif re.match("^good evening$|^goodevening$",utter.lower()):slack.post_message(conn,random.choice(["Very Good Evening "+user_name]))
    elif re.match("^good night$|^goodnight$",utter.lower()):slack.post_message(conn,random.choice(["Sweet Dreams"]))
    elif re.match("^how are you(.*)",utter.lower()):slack.post_message(conn,random.choice(["I am good. How can I help you?"]))
    elif re.match("^nice to meet you$",utter.lower()):slack.post_message(conn,random.choice(["It's nice meeting you, too "+user_name]))
    elif re.match("^nice to see you$",utter.lower()):slack.post_message(conn,random.choice(["Hi! how are you doing?"]))
    elif re.match("^nice to talk to you$|^nice to talk with you$",utter.lower()):slack.post_message(conn,random.choice(["I am feeling the same"]))
    elif re.match("^what's up(.*)|^whats up(.*)|^whatsup(.*)",utter.lower()):slack.post_message(conn,random.choice(["Not a whole lot. What's going on with you?"]))
    elif re.match("^what can you do(.*)|^How will you help me(.*)|^your job(.*)", utter.lower()):
        slack.post_message(conn, random.choice(["I can help you in Hollywood Movies, Novels and Weather in location"]))
    #Check confidence. Here the Threshold is 60% confidence
    elif Int_Ent_Sent['Confidence']<80:
        slack.post_message(conn,random.choice(fallback_responses))
    #call respective Dialogs according to the use intent
    else:
        if Int_Ent_Sent['Intent']=='Movie':
            dialogs.movie(Int_Ent_Sent,conn,user_name)
        elif Int_Ent_Sent['Intent']=='Novel':
            dialogs.novel(Int_Ent_Sent,conn,user_name)
        elif Int_Ent_Sent['Intent']=='Weather':
            dialogs.weather(Int_Ent_Sent,conn,user_name)
        elif Int_Ent_Sent['Intent']=='Welcome':
            dialogs.Welcome(Int_Ent_Sent,conn,user_name)
        #for key,value in Int_Ent_Sent.items():
         #   slack.post_message(conn,f'{key}: {value}')

def main():
    df=pd.read_excel('data.xlsx',sheet_name='intent')
    model,vectorizer=nlu.train(df)
    conn=slack.connect()
    #model.save('nlu_model.h5')
    #model.load_weights('nlu_model.h5')
    slack.post_message(conn,'I can help you in getting the details of Hollywood Movies, Novels and Weather in location . Type something to chat with me')
    while True:
        #retrieve utterance from slack channel
        utter,user_name=slack.get_message(conn)
        handle_utter(conn, utter, user_name, model, vectorizer, df)

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nProgram was interrupted by user!!')
    except Exception as e:
        print('\nProgram stopped running by Excpetion',str(e))

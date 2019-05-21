import slack
import pandas as pd
import random
import requests
from pylibgen import Library

df=pd.read_excel('data.xlsx',sheet_name='entity')

#novel Dialog
def novel(Int_Ent_Sent,conn,user_name):
    title = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['novel_name'])]
    author = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['writer'])]
    publisher = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['publisher'])]
    year = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['year'])]
    descr = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['descr'])]
    while (1):
        if title:
            #proceed
            l = Library()
            ids = l.search(title[0])
            if ids:
                for id in ids:
                    b1 = l.lookup(id, fields=["*"])
                for b in b1:
                    slack.post_message(conn, random.choice(["details of novel "+b.__dict__['title']+" are"]))
                    if author:
                        slack.post_message(conn, random.choice(["author : " + str(b.__dict__['author']) ]))
                    if publisher:
                        slack.post_message(conn, random.choice(["publisher : " + str(b.__dict__['publisher'])]))
                    if year:
                        slack.post_message(conn, random.choice(["year : " + str(b.__dict__['year'])]))
                    if descr:
                        slack.post_message(conn, random.choice(["descr : " + str(b.__dict__['descr']) ]))
            break
        else:
            slack.post_message(conn,'Please enter the novel name correctly')
            title= [slack.get_message(conn)][0]

#movie Dialog
def movie(Int_Ent_Sent,conn,user_name):
    title = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['movie_name'])]
    actors= [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['actors'])]
    awards = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['awards'])]
    country= [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['country'])]
    genre = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['genre'])]
    director = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['director'])]
    language = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['language'])]
    poster = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['poster'])]
    plot = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['plot'])]
    rate = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['rate'])]
    ratings= [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['ratings'])]
    release = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['release'])]
    runtime = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['runtime'])]
    writer = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['writer'])]
    website = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['website'])]
    while (1):

        omdb_api_key = '3b3c8518'
        details = requests.get('http://www.omdbapi.com/?t={0}&apikey={1}'.format(title[0] if title else '', omdb_api_key)).json()
        if details['Response']=='True':
            slack.post_message(conn, random.choice(["details of movie " + details['Title'] + " are"]))
            if actors:
                slack.post_message(conn, random.choice(["actors : " + str(details['Actors'])]))
            if awards:
                slack.post_message(conn, random.choice(["awards : " + str(details['Awards'])]))
            if country:
                slack.post_message(conn, random.choice(["country : " + str(details['Country'])]))
            if genre:
                slack.post_message(conn, random.choice(["genre of movie is " + str(details['Genre'])]))
            if director :
                slack.post_message(conn, random.choice(["directed by " + str(details['Director'])]))
            if language:
                slack.post_message(conn, random.choice(["language : " + str(details['Language'])]))
            if poster:
                slack.post_message(conn, random.choice(["link to poster : " + str(details['Poster'])]))
            if plot:
                slack.post_message(conn, random.choice(["plot of movie : " + str(details['Plot'])]))
            if rate:
                slack.post_message(conn, random.choice(["rate : " + str(details['Rated'])]))
            if ratings:
                for b in details['Ratings']:
                    slack.post_message(conn,random.choice(["rating at " + str(b['Source']) + " is "+str(b['Value'])]))
            if release:
                slack.post_message(conn, random.choice(["release date is " + str(details['Released'])]))
            if runtime :
                slack.post_message(conn, random.choice(["runtime of show: " + str(details['Runtime'])]))
            if writer:
                slack.post_message(conn, random.choice(["written by " + str(details['Writer'])]))
            if website:
                slack.post_message(conn, random.choice(["website link : " + str(details['Website'])]))
            break
        else :
            slack.post_message(conn, 'Please enter the movie name correctly')
            title = [slack.get_message(conn)][0]

#climate Dialog
def weather(Int_Ent_Sent,conn,user_name):
    #update acc to excel
    temp = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['temp'])]
    pressure = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['pressure'])]
    temp_min = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['temp_min'])]
    temp_max = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['temp_max'])]
    speed = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['speed'])]
    deg = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['direction'])]
    country = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['country'])]
    humidity = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['humidity'])]
    loc = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['location_names'])]
    coord = [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['coordinates'])]
    wea= [i.lower() for i in list(dict.fromkeys(Int_Ent_Sent['Entity'])) if i.lower() in list(df['weather'])]
    while (1):
        if loc:
            weather_reposonse = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+str(loc[0])+'&APPID=0583a32030db119217dc0595d49acc33')
            climate = weather_reposonse.json()
            slack.post_message(conn, random.choice(["climate at "+str(loc[0])+" is as follows "]))
            if coord:
                slack.post_message(conn, random.choice(["coordinates are " + str(climate['coord']['lon']) + " longitude and " + str(climate['coord']['lat']) + " latitude "]))
            if wea:
                slack.post_message(conn,random.choice(["weather at "+str(loc[0])+" is " + str(climate['weather'][0]['description'])]))
            if temp:
                slack.post_message(conn, random.choice(["temperature is  " + str(climate['main']['temp'])+"Fahrenheit"]))
            if pressure:
                slack.post_message(conn, random.choice(["pressure is " + str(climate['main']['pressure'])+"hectopascals"]))
            if humidity:
                slack.post_message(conn, random.choice(["humidity is " + str(climate['main']['humidity'])+"%"]))
            if temp_min:
                slack.post_message(conn, random.choice(["minimum temperature is " + str(climate['main']['temp_min'])+"Fahrenheit"]))
            if temp_max:
                slack.post_message(conn, random.choice(["maximum temperature is " + str(climate['main']['temp_max'])+"Fahrenheit"]))
            if speed:
                slack.post_message(conn, random.choice(["speed of wind is " + str(climate['wind']['speed'])+"miles/hour"]))
            if deg:
                slack.post_message(conn, random.choice(["direction of wind is " + str(climate['wind']['deg']+" degrees")]))
            if country:
                slack.post_message(conn, random.choice(["written by " + str(climate['country'])]))
            break
        else:
            slack.post_message(conn,'Please enter the location name correctly')
            loc= [slack.get_message(conn)][0]

#Welcome Dialog
def Welcome(Int_Ent_Sent,conn,user_name):
    welcome_responses=["Hi "+user_name+"! How are you doing?","Hello "+user_name+"! How can I help you?","Good day "+user_name+"! What can I do for you today?","Greetings "+user_name+"! How can I assist?"]
    slack.post_message(conn,random.choice(welcome_responses))

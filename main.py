#importing dependencies 

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pywhatkit
import wikipedia  
import pyjokes 
from bs4 import BeautifulSoup
import requests
import time 
import os 
import sys 
import random 
from translate import Translator
from response_generator import ResponseGenerator
import subprocess


#initializing voice of AI ASSISTANT 
def speak(text):
    engine = pyttsx3.init()                       # initializing pyttsx3
    voices = engine.getProperty('voices')         # extracting voices
    engine.setProperty('voice', voices[1].id)    # Set the voice to a specific one (adjust this)
    engine.setProperty('rate', 130)               # Speech rate (words per minute)
    engine.setProperty('volume', 2.0)             # Volume level (from 0.0 to 1.0)
    engine.say(text)                              # making alexa speak
    engine.runAndWait()
    

def recognize_command():
    '''to take initial voice command'''
    r = sr.Recognizer()                 #recognize speech from audio
    with sr.Microphone() as source:     #opens the computer's microphone as a source for audio input

        print("Listening to your voice...")
        
        r.pause_threshold = 1

        # Adjust for ambient noise
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source,0,15)           #records audio using the listen method of the Recognizer object and stores the recorded audio in the audio variable.

    try:
        command = r.recognize_google(audio, language = "en")
        command = command.lower()

        print("You said:", command)
        return command 
    
    except sr.UnknownValueError:
        speak("Sorry , I can't understand your voice")
        print("Sorry, I could not understand your voice.")
        return None

    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None



def perform_web_search(query):

    '''function for web search using Google based on the given query 
    and retrieves a list of URLs that correspond to the search results'''

    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    response = requests.get(search_url)    # sending HTTP Request       

    if response.status_code == 200:    #Response Handling
        #indicating a successful response
        soup = BeautifulSoup(response.content, 'html.parser')   #Parse HTML Content
        search_results = []
        for link in soup.find_all('a'):             #searches for all <a> (anchor) elements in the HTML content
            href = link.get('href')                 
            if href and href.startswith('/url?q='):   #filters out URLs related to search results.    
                url = href[7:].split('&')[0]          #extracts the URLs
                search_results.append(url) 
        return search_results      #returns a list of URLs representing the search results
    else:
        print("Error: Unable to retrieve search results.")
        return []



# Function to fetch the current weather
def get_current_weather(city, country_code):
    api_key = os.getenv('OPENWEATHERMAP_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Make sure you set the OPENWEATHERMAP_API_KEY environment variable.")

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city},{country_code}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    data = response.json() 

    if data["cod"] != "404":         #indicating response is successful
        main_data = data["main"]
        temperature = main_data["temp"]
        humidity = main_data["humidity"]
        description = data["weather"][0]["description"]

        return f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}"
    else:
        return "City not found."


# Function to download an image from a given URL
def download_image(url, save_path):
    response = requests.get(url)                     # send an HTTP request to the provided URL (url)
    if response.status_code == 200:                  # request was successful
        #Handling Errors
        with open(save_path, 'wb') as file:          # function opens a file in binary write mode at the specified save_path.
            file.write(response.content)             # writes the content of the response (the image data) to the file
        print("Image downloaded successfully.")
    else:
        print("Failed to download image.")



# Function to fetch top headlines for a specific country
def get_top_headlines(country):
    # Fetch API key from environment variable
    api_key = os.getenv('NEWS_API_KEY')

    if not api_key:
        raise ValueError("News API key not found. Set the NEWS_API_KEY environment variable.")

    base_url = "https://newsapi.org/v2/top-headlines"
    
    if country.lower() == "all" :
        params = {
            "apiKey": api_key
        }
    else:
        params = {
            "apiKey": api_key,
            "country": country
        }

    complete_url = f"{base_url}?q={country}&apiKey={api_key}"
    print("Complete URL:", complete_url)  
    response = requests.get(complete_url,params=params)
    print("Response Status Code:", response.status_code)
    data = response.json() 

    if response.status_code == 200:       #request is successful 
        articles = data.get('articles', [])
        for article in articles: 
            print("Current News")
            speak("Current News") 
            print(f"Title: {article['title']}")
            speak(f"Title: {article['title']}")
            print(f"Description: {article['description']}")
            speak(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            speak(f"URL: {article['url']}")
            print("------")
    else:
        print("Failed to retrieve news.")
        speak("Failed to retrieve news.")


def recommend_books(genre=None, author=None):
    '''function to recommend books based on genre and author '''

    base_url = "http://openlibrary.org/subjects/"
    params = {}
    if genre:
        params['subject'] = genre
    if author:
        params['author'] = author
    if author and genre :
        params['subject'] = genre 
        params['author']  = author

    response = requests.get(base_url + "recommend.json", params=params)
    print(response)
    if response.status_code == 200:
        books = response.json().get('works', [])
        print(response.status_code) 

        if books:
            print("Recommended Books:")
            for book in books:
                title = book.get('title', 'Unknown Title')
                author = book.get('authors', [{'name': 'Unknown Author'}])[0].get('name')
                print(f"Title: {title}")
                print(f"Author: {author}")
                print("-----")
                speak(f"Title: {title}. Author: {author}")
        else:
            print("No books found for the specified criteria.")
            speak("No books found for the specified criteria.")
    else:
        print("Failed to retrieve book recommendations.")
        speak("Failed to retrieve book recommendations.")


def play_movie(movie_name):
    try:
        # Perform a web search for the movie
        search_query = f"{movie_name} movie"
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)

        # You may add a delay to give time for the browser to open before proceeding
        time.sleep(5)  
        print(f"Searching for movie: {movie_name}")

    except Exception as e: 
        print(f"Error: {str(e)}")
        print(f"Could not play the movie: {movie_name}")
        speak(f"Could not play the movie: {movie_name}")


def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation


def open_application(application_name):
    try:
        
        if "notepad" in application_name.lower():
            subprocess.run(["notepad.exe"])
        elif "word" in application_name.lower():
            subprocess.run(["winword.exe"])
        elif "calculator" in application_name.lower():
            subprocess.run(["calc"])
        elif "file explorer" in application_name.lower():
            subprocess.run(["explorer"])
        elif "powerpoint" in application_name.lower():
            subprocess.run(["powerpnt"])
        elif "photoshop" in application_name.lower():
            subprocess.run(["photoshop"])
        elif "vs code" in application_name.lower():
            subprocess.run(["code"])
        elif "spotify" in application_name.lower():
            subprocess.run(["spotify"])
        elif "telegram" in application_name.lower():
            subprocess.run(["telegram"])
        elif "vlc" in application_name.lower():
            subprocess.run(["vlc"])
        elif "sublime text" in application_name.lower():
            subprocess.run(["sublime_text"])
        elif "zoom" in application_name.lower():
            subprocess.run(["zoom"])
        elif "slack" in application_name.lower():
            subprocess.run(["slack"])
        elif "firefox" in application_name.lower():
            subprocess.run(["firefox"])
        elif "microsoft edge" in application_name.lower():
            subprocess.run(["msedge"])
        elif "visual studio" in application_name.lower():
            subprocess.run(["devenv"])
        elif "outlook" in application_name.lower():
            subprocess.run(["outlook"])
        elif "discord" in application_name.lower():
            subprocess.run(["Discord"])
        elif "whatsapp" in application_name.lower():
            subprocess.run(["WhatsApp"])
        elif "microsoft teams" in application_name.lower():
            subprocess.run(["Teams"])
        elif "jupyter notebook" in application_name.lower():
            subprocess.run(["jupyter-notebook"])
        elif "android studio" in application_name.lower():
            subprocess.run(["studio64"])
        elif "chrome incognito" in application_name.lower():
            subprocess.run(["chrome", "--incognito"])
        elif "skype" in application_name.lower():
            subprocess.run(["Skype"])
        elif "pycharm" in application_name.lower():
            subprocess.run(["pycharm64"])
        elif "paint" in application_name.lower():
            subprocess.run(["mspaint"])
        elif "calendar" in application_name.lower():
            subprocess.run(["outlookcal"], shell=True)
        elif "instagram" in application_name.lower():
            webbrowser.open( "www.instagram.com")
        elif 'youtube' in application_name.lower():
            webbrowser.open("www.youtube.com")
        elif "one note" in application_name.lower():
            subprocess.run(["onenote"])
        elif "team viewer" in application_name.lower():
            subprocess.run(["TeamViewer"])
        elif "google meets" in application_name.lower():
            webbrowser.open("https://meet.google.com/") 
        elif "linkedin" in application_name.lower():
            webbrowser.open( "https://www.linkedin.com/")
        elif "facebook" in application_name.lower():
            webbrowser.open( "https://www.facebook.com/")
        elif "yahoo" in application_name.lower():
            webbrowser.open("https://www.yahoo.com/")
        else:
            print(f"Sorry, I don't know how to open {application_name}.")
    except Exception as e:
        print(f"An error occurred: {e}")


def play_music(query):
    # You can customize this function based on how you want to play music.
    # For example, you can open a music streaming website with the search query.

    search_url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(search_url)



#performing actions  based on commands
def perform_action(command, response_generator):

    print("Performing action for command :", command)

    response_generator = ResponseGenerator()
    # Access responses  from the ResponseGenerator class
    responses = response_generator.responses
    
    if command:
        if command in responses:
            response = random.choice(responses[command])
            print("Alexa:", response)  # Print the generated response
            speak(response)
        
        #Playing a specified YouTube video or a search term on YouTube.
        elif 'play video ' in command : 
            search = command.replace('play video','')         #extracting search name 
            speak('playing' + search)                   #making alexa speaking search name 
            print('playing')
            pywhatkit.playonyt(search)                  #youtube automation

        elif "youtube" in command:                        #opening youtube by saying "youtube" 
            speak("Opening youtube")
            print("opening youtube... ")         
            webbrowser.open("https://www.youtube.com/")

        elif "open application" in command : 
            print("Which application do you want to get open?")
            speak("Which application do you want to get open?")
            
            # Use speech recognition to get the number of suggestions
            recognizer = sr.Recognizer()

            try:
                # Recognize the speech input for the number of suggestions
                with sr.Microphone() as source:
                    print("Listening to your voice...")
                    recognizer.pause_threshold = 1
                    # Adjust for ambient noise
                    recognizer.adjust_for_ambient_noise(source)
        
                    audio = recognizer.listen(source,0,10)

                application_name = recognizer.recognize_google(audio, language = "en")
                print("Opening ", application_name)
                speak("Opening "+ application_name)
                open_application(application_name)

            except sr.UnknownValueError:
                print("Could not understand the audio")
                return None
            except sr.RequestError as e:
                print(f"Error with the speech recognition service: {e}")
                return None

        elif "open wikipedia" in command:              #instructing to open wikipedia by saying : "open wikipedia" 
            speak("Opening wikipedia")
            print("opening wikipedia.. ")
            webbrowser.open("https://www.wikipedia.org/")

        elif "open national portal of india " in command:   #instructing to open national portal of india by saying "national portal of india "
            speak("Information about government ")
            print("giving information about government ")
            webbrowser.open("https://www.india.gov.in/")


        elif "news of wool" in command:                 #instructing to give news of wool by saying : "news of wool"
            speak("Information regarding wool")
            print("information related wool")
            webbrowser.open("https://www.bing.com/ck/a?!&&p=5c538f30f39e8684JmltdHM9MTY5NDU2MzIwMCZpZ3VpZD0xNjBkOWMzNS02NmIwLTYyNzEtMzBhMS04ZDAyNjdiNjYzOGUmaW5zaWQ9NTIwNw&ptn=3&hsh=3&fclid=160d9c35-66b0-6271-30a1-8d0267b6638e&psq=which+is+best+website+to+give+news+and+trends+of+wool+of+indian+market&u=a1aHR0cHM6Ly93d3cuaWJlZi5vcmcvZXhwb3J0cy93b29sLWFuZC13b29sbGVu&ntb=1")

        
        elif "Wool TEXTILES of INDIA" in command:          #instructing to open ministry of textiles by saying : "wool textiles of india"
            speak("“WOOL AND WOOLLEN TEXTILES SECTOR")
            print("ministry of textiles information")
            webbrowser.open("https://www.bing.com/ck/a?!&&p=5aa3c336aa998960JmltdHM9MTY5NDU2MzIwMCZpZ3VpZD0xNjBkOWMzNS02NmIwLTYyNzEtMzBhMS04ZDAyNjdiNjYzOGUmaW5zaWQ9NTIwOA&ptn=3&hsh=3&fclid=160d9c35-66b0-6271-30a1-8d0267b6638e&psq=how+farming+of+wool+is+done+in+india+in+hindi&u=a1aHR0cDovL21pbmlzdHJ5b2Z0ZXh0aWxlcy5nb3YuaW4vc2l0ZXMvZGVmYXVsdC9maWxlcy9UZXh0aWxlc19TZWN0b3JfV29vbGFuZFdvb2xsZW5fMS5wZGY&ntb=1")

        elif "video of wool farming" in command:           #instructing to open vieo on wool farming by saying : "video of wool farming"
            speak("The process of wool farming is ")
            print("how wool farming is done ... ")
            webbrowser.open("https://youtu.be/XrRCTuLznOU?si=mokQIPny6TdoZjSR")

        elif "open google" in command:                  #instructing to open google by saying : "open google" 
            speak("Opening the google")
            print('Opening google')
            webbrowser.open("https://www.google.com/")

        elif "summary" in command :                    #instructing to give summary by saying "summary" along with specific topic name
            query = command.replace('summary',"")
            summary = wikipedia.summary(query,sentences=10, chars=0, auto_suggest=True, redirect=True)
            print("Displaying Summary....")
            print(summary)
            speak(summary) 

        
        elif "suggest article names" in command :         #for brainstorming article names by saying: "suggest article names"
            print("How many suggestions do you want ?")
            speak("How many suggestions do you want ?")
            
            # Use speech recognition to get the number of suggestions
            recognizer = sr.Recognizer()

            try:
                # Recognize the speech input for the number of suggestions
                with sr.Microphone() as source:
                    print("Listening to your voice...")
                    recognizer.pause_threshold = 1
                    audio = recognizer.listen(source,0,10)

                number = recognizer.recognize_google(audio, language = "en")
                number = int(number)
                suggestions = wikipedia.random(number)
                if suggestions:
                    print(f"Displaying {number} Suggestions....")
                
                    for i, suggestion in enumerate(suggestions):
                        print(f"{i+1}. {suggestion}")     
                        speak(f"Suggestion {i+1}: {suggestion}")
                else:
                    speak("I couldn't find any suggestions.")
                    print("No suggestions found.")

            except sr.UnknownValueError:
                speak("Could not understand the audio")
                print("Could not understand the audio ")
            except ValueError:
                speak("Sorry, I didn't get the number of suggestions.")
                print("Could not understand the audio ")


        elif "who is " in command :            #to know about a person by saying : "who is "
            person = command.replace("who is ","").strip()
            info = wikipedia.summary(person,sentences = 3, chars=0, auto_suggest=True, redirect=True)
            print(info)
            speak(person + info)


        elif "tell me a joke" in command :              #instructing to ask a joke by mentioning "joke" in a sentence
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        elif "search" in command :
            print("What do you want to search? ")
            speak("What do you want to search? ")
            
            recognizer = sr.Recognizer() 
            try:
                # Recognize the speech input for the number of suggestions
                with sr.Microphone() as source:
                    print("Listening to your voice...")
                    recognizer.pause_threshold = 1
                    audio = recognizer.listen(source,0,10) 

                query = recognizer.recognize_google(audio, language = "en")
                print('Performing web search on :',query)
                speak('Performing web search on :'+ query)
                perform_web_search(query)
            except sr.UnknownValueError:
                speak("Sorry, I could not understand the audio")
                print("Could not understand the audio ")
            except sr.RequestError:
                speak("There was an error with the speech recognition service")
                print("Could not request results from Google Speech Recognition service")


        elif "send whatsapp message" in command :    #instructing to send whatsapp message by saying : "send whatsapp message"

            '''whatsapp automation is performed in this condition'''

            print("Message will only be sent if you will give both recipient's phone number and message ")
            speak("Message will only be sent if you will give both recipient's phone number and message ")
            print("Please say the recipient's phone number (including country code):")
            speak("Please say the recipient's phone number (including country code):")

            # Use speech recognition to get the number of suggestions

            recognizer = sr.Recognizer() 
            try:
                # Recognize the speech input for the number of suggestions
                with sr.Microphone() as source:
                    print("Listening to your voice...")
                    recognizer.pause_threshold = 1
                    audio = recognizer.listen(source,0,22) 

                phone_number = recognizer.recognize_google(audio, language = "en")
                print(f"Phone number: {phone_number}")
                if phone_number:
                    
                    print("Do you want to send a text message or an image message?")
                    speak("Do you want to send a text message or an image message?")
                    print("For 'image' say 'image' and for 'text' say 'text' ")
                    speak("For 'image' say 'image' and for 'text' say 'text' ")
                    
                    with sr.Microphone() as source:
                        print("Listening to your voice ...")
                        recognizer.pause_threshold = 1
                        audio = recognizer.listen(source, 0, 15)

                    choice = recognizer.recognize_google(audio)
                    
                    if "text" in choice.lower():
                        print("Please say the text message you want to send:")
                        speak("Please say the text message you want to send:")
                        with sr.Microphone() as source:
                            print("Listening to your voice ...")
                            recognizer.pause_threshold = 1
                            audio = recognizer.listen(source, 0, 20)

                        message = recognizer.recognize_google(audio, language="en")
                        print(f"Message: {message}")
                        # Get the current time
                        now = datetime.datetime.now()
                        hours = now.hour
                        minutes = now.minute + 1  # Send the message 1 minute from now

                        if message:
                            # Send the text message
                        
                            pywhatkit.sendwhatmsg(phone_number, message, hours, minutes)
                            print(f"Text message will be sent to {phone_number} in 1 minute.")
                        else:
                            print("You haven't provide me text message yet.")
                    
                    elif "image" in choice.lower():
                        print("what type of image do you want to send ")
                        speak("what type of image do you want to send ")
                        with sr.Microphone() as source:
                            print("Listening to your voice ...")
                            recognizer.pause_threshold = 1
                            audio = recognizer.listen(source, 0, 15)
                        search_query = recognizer.recognize_google(audio, language="en")
                        print("Search Query:", search_query) 
                        # Get the current time
                        now = datetime.datetime.now()
                        hours = now.hour
                        minutes = now.minute + 1  # Send the message 1 minute from now
                        search_results = perform_web_search(search_query)
                        print("Search Results:", search_results)  # Print the search results to verify

                        if search_results:
                            first_result = search_results[0]
                            image_path = os.path.join(r"C:\Users\ishika gupta\myenv\Scripts\images", f"{search_query.replace(' ', '_')}.png")
                            try:

                                download_image(first_result, image_path)
                                print("Image downloaded successfully.")  
                                speak(f"Sending an image related to {search_query}") 

                                try:
                                    pywhatkit.sendwhatmsg(phone_number, image_path, hours, minutes)
                                    print(f"Message will be sent to {phone_number} in 1 minute.")  
                                except Exception as e:
                                    print("Error:", str(e))

                            except Exception as e:
                                print("Error:", str(e))
    
                        else:
                            speak(f"Sorry, I couldn't find any images related to {search_query}")
                    else:
                        speak("Invalid choice. Message not sent.")
                else:
                    speak("You haven't provide me your phone number correctly. ")
            except sr.UnknownValueError:
                print("Could not understand the audio")
                speak("Could not understand the audio")



        elif "current weather" in command :
            print("Fetching current weather...")
            speak("Fetching current weather...")
            
            recognizer = sr.Recognizer()
            try:
                print("Please specify the city for weather information:")
                speak("Please specify the city for weather information:")
                with sr.Microphone() as source:
                    print("Listening to your voice ...")
                    recognizer.pause_threshold = 1
                    audio = recognizer.listen(source, 0, 15)

                city = recognizer.recognize_google(audio)
                print(f"City: {city}")

                # Assuming the country code is always the same 
                country_code = "US"

                weather_info = get_current_weather(city, country_code)
                print("Current Weather:")
                print(weather_info)
                speak("Here is the current weather:")
                speak(weather_info)

            except sr.UnknownValueError:
                print("Could not understand the audio")
                speak("Could not understand the audio")
        

        
        elif "current news" in command:
            print("Which country's news would you like to know? Say 'all' for all countries and give country code for specific country. ")
            speak("Which country's news would you like to know? Say 'all' for all countries give country code for specific country. ")
            recognizer = sr.Recognizer()
            
            try:

                with sr.Microphone() as source:
                    print("Listening to your voice...")
                    recognizer.pause_threshold = 1
                    audio = recognizer.listen(source, 0,15)
                country = recognizer.recognize_google(audio).lower()
                
                if "world" in country or "global" in country:
                    country = "all"

                print(f"Country: {country}")
                print("Fetching news...")  # Add this line for additional debug output

                try:
                    get_top_headlines(country)
                except ValueError as e:
                    print(str(e))
            
            except sr.UnknownValueError: 
                print("Could not understand the audio")
                speak("Could not understand the audio")

        

        elif "recommend books" in command:
            speak("Sure! I can recommend books based on genre or author. Please specify the genre or author.")
            print("Please specify the genre or author for book recommendations:")
            genre = None
            author = None
            recognizer = sr.Recognizer()
            try:
                    with sr.Microphone() as source:
                        print("Listening to your voice...")
                        recognizer.pause_threshold = 1
                        audio = recognizer.listen(source, 0,15)
                    user_input = recognizer.recognize_google(audio).lower()

                    if "genre" in user_input:
                        speak("Please specify the genre.")
                        print("Please specify the genre:")
                        with sr.Microphone() as source:
                            print("Listening to your voice...")
                            recognizer.pause_threshold = 1
                            audio = recognizer.listen(source, 0,15)
                        genre = recognizer.recognize_google(audio).lower()
                        recommend_books(genre,author) 
                    elif "author" in user_input:
                        speak("Please specify the author.")
                        print("Please specify the author:")
                        with sr.Microphone() as source:
                            print("Listening to your voice...")
                            recognizer.pause_threshold = 1
                            audio = recognizer.listen(source, 0,15)
                        genre = recognizer.recognize_google(audio).lower()
                        recommend_books(genre,author) 
                    elif 'author' in user_input and 'genre' in user_input:
                        speak("Please specify both author and genre only in sequence. ")
                        print("Please specify both author and genre in sequence. ")
                        with sr.Microphone() as source:
                            print("Listening to your voice...")
                            recognizer.pause_threshold = 1
                            audio = recognizer.listen(source, 0,15)
                        genre = recognizer.recognize_google(audio).lower()
                        recommend_books(genre,author)
                    
            except sr.UnknownValueError: 
                print("Could not understand the audio")
                speak("Could not understand the audio")


        elif "play movie" in command: #instructing to play a movie 
            movie_name = command.replace('play movie ',"").strip()
            print(f"Playing movie: {movie_name}")
            speak(f"Now playing the movie: {movie_name}")
            play_movie(movie_name)  # Call the function to search and potentially play the movie


        elif  "translate language" in command:
            print("Sure! I'll translate the language. ")  
            speak("Sure! I'll translate the language. ")
            print("Please specify the text you want to translate:")
            speak("Please specify the text you want to translate:")
        
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening to your voice...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source, 0,15)
                text_to_translate  = recognizer.recognize_google(audio).lower()

            print("Please specify the target language (e.g., 'fr' for French):")
            speak("Please specify the target language (e.g., 'fr' for French):")
            
            with sr.Microphone() as source:
                print("Listening to your voice...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source, 0,15)
                target_language = recognizer.recognize_google(audio).lower()

            translation = translate_text(text_to_translate, target_language)
            print(f"Translation: {translation}")
            speak(f"The translation of {text_to_translate} in {target_language} is: {translation}")


        elif "copy me" in command:    #instructing alexa to copy user
            speak("Sure! I'll repeat what you say.")
            print("Sure! I'll repeat what you say.")
    
            recognizer = sr.Recognizer()
            with sr.Microphone as source :
                print("Listening to your voice...")
                recognizer.pause_threshold = 1
                audio = recognizer.listen(source, 0,15)
                user_command = recognizer.recognize_google(audio).lower()
                speak(command)
                if user_command:
                    print("You said:", user_command)
                    speak("You said: " + user_command)
                else:
                    print("Couldn't understand what you said.")
                    speak("Sorry, I couldn't understand what you said.")
        

        elif "play song" in command:     #query for playing song
        
            print("What genre or artist would you like to listen to?")
            speak("What genre or artist would you like to listen to?")
            
            # Use speech recognition to get the music query
            music_query = recognize_command()
            
            if music_query:
                print(f"Playing music: {music_query}")
                speak(f"Playing music: {music_query}")
                play_music(music_query)
            else:
                print("Sorry, I couldn't understand your music preference.")
                speak("Sorry, I couldn't understand your music preference.")


        elif "close program" in command:               #instructing to end program by saying "close program"
            speak("Thanks for conversation")
            speak("Program is closing")
            print("Closing the program")
            sys.exit()
    
        
        else:
            response = random.choice(responses["default"])
            print(response)
            speak(response)
    
    else:
        print("No valid command recognized.")




if __name__ == "__main__" :

    response_generator = ResponseGenerator()
    
    print("Hi I am Alexa , how my I help you? ")
    speak("Hi I am Alexa , how my I help you? ")
    
    while True:
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        speak(f"Current date and time : {formatted_datetime}")
        print(f"Current date and time : {formatted_datetime}")
        speak("You may start speaking now") 
        command = recognize_command()

        if command : 
            perform_action(command, response_generator)
        
                          
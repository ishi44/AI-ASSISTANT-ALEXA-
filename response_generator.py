# response_generator.py


class ResponseGenerator:
    def __init__(self):
    # Predefined responses based on different queries
        self.responses = {

        "hello": ["Hello!", "Hi there!", "Greetings!"],
        "how are you": ["I'm doing well, thank you!", "I'm just a computer program, so I don't have feelings, but I'm here to assist you!"],
        "what's your name": ["I'm an AI assistant. alexa ", "You can call me Assistant. alexa"],
        "goodbye": ["Goodbye!", "Farewell!", "See you later!"],
        "who are you": ["I am your language assistant.", "I'm here to help you with any questions or tasks you have."],
        "where do you live": ["I exist in the digital realm and don't have a physical location.", "I live in the cloud, always here to assist you!"],
        "who am i": ["You are a unique individual!", "I don't have that information. You are you!"],
        "what can you do": ["I can answer questions, tell jokes, provide weather updates, and more. Feel free to ask!"],
        "how old are you": ["I don't have an age. I'm here to assist you!", "Age is just a number for me, but I'm always here to help."],
        "what's the meaning of life": ["The meaning of life is a philosophical question. Some say it's to find happiness and purpose.", "The meaning of life is a question each person must answer for themselves."],
        "what's your favorite season": ["I don't have personal preferences, but I think every season has its own unique beauty!", "I don't experience seasons, but I can appreciate the beauty of each season in nature."],
        "who is your favorite Beatle": ["I don't have personal preferences, but all the Beatles were incredibly talented musicians and songwriters!", "I appreciate the musical contributions of all the Beatles; choosing a favorite is tough!"],
        "tell me about The Beatles": ["The Beatles were a legendary British rock band formed in Liverpool in 1960. The group consisted of John Lennon, Paul McCartney, George Harrison, and Ringo Starr. They are considered one of the most influential bands in the history of popular music, with iconic hits like 'Hey Jude,' 'Let It Be,' and 'Yesterday.' The Beatles' impact on music and culture is immense and continues to be celebrated."],
        "favorite K-pop group": ["I don't have personal favorites, but there are many amazing K-pop groups! Who's your favorite?", "K-pop has a vibrant and diverse scene with many talented groups. Who's your favorite K-pop group?"],
        "tell me about K-pop": ["K-pop, short for Korean pop, is a genre of music originating in South Korea. It is characterized by a wide variety of audiovisual elements, incorporating dance, fashion, and catchy music. K-pop groups often have a large fanbase and a strong online presence. Some popular K-pop groups include BTS, BLACKPINK, EXO, TWICE, and more. The genre has gained significant international popularity in recent years."],
        "favorite BTS song": ["I don't have personal favorites, but BTS has produced many fantastic songs! Which BTS song do you like the most?", "BTS has a diverse discography with incredible songs. Which one resonates with you the most?"],
        "tell me about BTS": ["BTS, also known as the Bangtan Boys, is a globally renowned South Korean boy band formed in Seoul in 2013. The group consists of seven members: RM, Jin, Suga, J-Hope, Jimin, V, and Jungkook. They are known for their energetic performances, meaningful lyrics, and addressing various societal issues through their music. BTS has a massive international fanbase and has achieved unprecedented success in the global music industry."],
        "tell me about John Lennon": ["John Lennon was a member of The Beatles, known for his songwriting, vocals, and activism. He co-founded the band and wrote some of their most iconic songs. Lennon's solo career also made a significant impact with hits like 'Imagine.' He was tragically assassinated in 1980."],
        "tell me about The Beatles' albums": ["The Beatles released iconic albums such as 'Sgt. Pepper's Lonely Hearts Club Band,' 'Revolver,' 'Abbey Road,' and 'The White Album.' These albums showcased their musical innovation and had a lasting impact on the music industry."],
        "tell me about Paul McCartney": ["Paul McCartney, a member of The Beatles, is a prolific songwriter and musician. He co-founded the band, showcasing his talents in singing, bass, and piano. McCartney's post-Beatles career was highly successful, and he continues to perform and create music."],
        "tell me about The Beatles' early years": ["The Beatles' early years were marked by performances in Liverpool and Hamburg. Their lineup included John Lennon, Paul McCartney, George Harrison, Stuart Sutcliffe, and Pete Best. They gained popularity through intense performing and a unique sound."],
        "tell me about George Harrison": ["George Harrison, a member of The Beatles, was known for his guitar skills and songwriting. He contributed hits like 'Here Comes the Sun' and 'Something.' Harrison's solo career was also successful, demonstrating his diverse musical abilities."],
        "tell me about The Beatles' influence": ["The Beatles' influence on music and culture is immense. They revolutionized popular music, songwriting, and recording techniques. Their impact can still be felt today, and they are considered one of the greatest and most influential bands of all time."],
        "tell me about Ringo Starr": ["Ringo Starr, a member of The Beatles, was the drummer and occasional lead vocalist for the group. He brought a unique style to the band's music. Post-Beatles, Starr pursued a solo music career and became an actor."],
        "tell me about BLACKPINK members": ["BLACKPINK consists of four members: Jisoo, Jennie, Rosé, and Lisa. Each member brings a unique style to the group, and together they create a powerful and captivating stage presence."],
        "tell me about BLACKPINK": ["BLACKPINK is a popular South Korean girl group formed by YG Entertainment. The group consists of members Jisoo, Jennie, Rosé, and Lisa. They are known for their powerful performances, catchy songs, and international success. Some of their hits include 'DDU-DU DDU-DU' and 'How You Like That.'"],
        "tell me about EXO members": ["EXO initially had twelve members but currently consists of nine: Xiumin, Suho, Lay, Baekhyun, Chen, Chanyeol, D.O., Kai, and Sehun. Each member contributes to EXO's diverse and talented lineup."],
        "tell me about EXO": ["EXO is a prominent South Korean-Chinese boy band formed by SM Entertainment. The group debuted in 2012 and is known for their diverse discography, impressive choreography, and strong fanbase. Some of their popular songs include 'Love Shot' and 'Ko Ko Bop.'"],
        "tell me about TWICE members": ["TWICE is composed of nine members: Nayeon, Jeongyeon, Momo, Sana, Jihyo, Mina, Dahyun, Chaeyoung, and Tzuyu. They bring their unique personalities and skills to create the vibrant TWICE group we know."],
        "tell me about TWICE": ["TWICE is a successful South Korean girl group formed by JYP Entertainment. The group is recognized for their energetic music, catchy tunes, and a bright, bubbly image. Some of their popular songs include 'Cheer Up' and 'Fancy.'"],
        "tell me about The Beatles' songwriting": ["The Beatles were known for their exceptional songwriting, often penned by John Lennon and Paul McCartney. Their lyrics were diverse, touching on love, peace, social issues, and more. Their ability to craft timeless songs is a key part of their legacy."],
        "tell me about EXO's achievements": ["EXO has achieved numerous awards and recognitions in the music industry. They've won Daesang (Grand Prize) awards at prestigious events like the Melon Music Awards, Golden Disc Awards, and Seoul Music Awards, showcasing their excellence."],
        "tell me about Hollywood music": ["Hollywood has a rich and diverse music scene, ranging from pop and rock to hip-hop and electronic. It's a hub for musical talent, and many legendary artists and bands have emerged from or found success in Hollywood."],
        "tell me about different music genres": ["There are numerous music genres, each with its unique style and characteristics. Some popular genres include pop, rock, hip-hop, jazz, blues, country, electronic, classical, reggae, and R&B. Each genre has its own fan base and history."],
        "tell me about pop music": ["Pop music is characterized by its catchy melodies, relatable lyrics, and widespread appeal. It often features a memorable chorus and is designed to be commercially successful. Artists like Michael Jackson, Madonna, and Taylor Swift are prominent in pop music."],
        "tell me about rock music": ["Rock music is known for its energetic sound, often featuring electric guitars, drums, and strong vocals. It has various subgenres, including classic rock, alternative rock, hard rock, and punk rock. Bands like The Beatles, Led Zeppelin, and Queen are rock music icons."],
        "tell me about hip-hop music": ["Hip-hop is a genre characterized by rhythmic and rhyming speech known as rapping. It originated in African American communities and has evolved into a global phenomenon. Artists like Tupac Shakur, The Notorious B.I.G., and Jay-Z have made significant contributions to hip-hop."],
        "tell me about jazz music": ["Jazz is a genre known for its improvisation and syncopated rhythms. It has its roots in African and African American musical traditions. Artists like Miles Davis, Louis Armstrong, and John Coltrane are celebrated figures in jazz."],
        "tell me about blues music": ["Blues music is characterized by its emotional lyrics and a 12-bar musical structure. It originated in the African American communities of the Deep South. Artists like B.B. King, Robert Johnson, and Muddy Waters are prominent in blues music."],
        "tell me about country music": ["Country music often tells stories about life, love, and heartache. It features elements like acoustic guitars, fiddles, and banjos. Artists like Johnny Cash, Dolly Parton, and Willie Nelson have made significant contributions to country music."],
        "tell me about electronic music": ["Electronic music is produced using electronic devices and technology. It encompasses a wide range of styles, from techno and house to dubstep and trance. Artists like Daft Punk, Tiësto, and Deadmau5 are recognized in electronic music."],
        "tell me about classical music": ["Classical music is a complex and diverse genre with a rich history. It's known for its intricate compositions and use of orchestral instruments. Composers like Mozart, Beethoven, Bach, and Tchaikovsky are foundational figures in classical music."],
        "tell me about reggae music": ["Reggae music originated in Jamaica and is known for its distinctive rhythms and social and political themes. It often addresses issues of love, peace, and unity. Artists like Bob Marley, Peter Tosh, and Jimmy Cliff are influential in reggae music."],
        "tell me about R&B music": ["R&B, or rhythm and blues, is a genre that combines elements of jazz, gospel, and blues. It often features soulful vocals and strong rhythms. Artists like Aretha Franklin, Marvin Gaye, and Beyoncé are significant in R&B music."],
        "tell me about famous musicians": ["There are countless famous musicians across various genres. Some notable musicians include Michael Jackson, Elvis Presley, Bob Marley, Madonna, Freddie Mercury, Jimi Hendrix, Whitney Houston, Prince, and David Bowie. Their contributions have had a lasting impact on the music industry."],
        "tell me about TWICE's fandom": ["TWICE's fandom is called ONCE, which stands for 'One in a Million.' ONCE is known for its strong support and love for the members. They actively engage in supporting TWICE's music, activities, and charity work."],
        "tell me about BLACKPINK's success": ["BLACKPINK has achieved significant success globally, with chart-topping songs, record-breaking music videos, and sold-out concerts. They've become ambassadors for various brands and are recognized as one of the leading K-pop acts in the world."],
        "what's your favorite song": ["I don't have personal preferences, but 'Imagine' by John Lennon is a powerful and inspiring song.", "I don't have the ability to have favorite songs, but 'Bohemian Rhapsody' by Queen is a classic that many people enjoy."],
        "what's your favorite animal": ["I don't have personal preferences, but dolphins are amazing creatures!", "I don't have personal favorites, but dolphins are known for their intelligence and playful behavior."] ,
        "do you like music": ["I don't have personal preferences, but I can suggest some great music for you!", "I can't hear, but I'm here to help you find your favorite tunes!"],
        "tell me a tongue twister": ["Sure! Here's a tongue twister: How can a clam cram in a clean cream can?", "Here's another one: Peter Piper picked a peck of pickled peppers."],
        "what's the capital of France": ["The capital of France is Paris.", "Paris is the capital of France, known for its art, fashion, and culture."],
        "where do you live": ["I exist in the digital realm and don't have a physical location.", "I live in the cloud, always here to assist you!"],
        "what's the tallest mountain": ["Mount Everest is the tallest mountain on Earth, reaching a height of 29,032 feet (8,849 meters).", "The tallest mountain on Earth, Mount Everest, stands tall at 29,032 feet (8,849 meters)."],
        "what's the largest ocean": ["The Pacific Ocean is the largest ocean on Earth, covering an area of about 63.8 million square miles (165.2 million square kilometers).", "The Pacific Ocean holds the title of being the largest ocean, spanning about 63.8 million square miles (165.2 million square kilometers)."],
        "what's the speed of light": ["The speed of light in a vacuum is approximately 299,792 kilometers per second (km/s) or about 186,282 miles per second (mi/s).", "The speed of light in a vacuum is approximately 299,792 kilometers per second (km/s) or about 186,282 miles per second (mi/s)."],
        "who's your favorite musician": ["I don't have personal preferences, but I enjoy all types of music!", "I don't have favorites, but I appreciate all forms of music."],
        "tell me a tongue twister": ["Sure! Here's a tongue twister: How can a clam cram in a clean cream can?", "Here's another one: Peter Piper picked a peck of pickled peppers."],
        "what's the tallest building": ["The tallest building in the world is the Burj Khalifa in Dubai, standing at 2,717 feet (828 meters).", "The Burj Khalifa in Dubai holds the record for being the tallest building, reaching a height of 2,717 feet (828 meters)."],
        "why did the chicken cross the road": ["To get to the other side!", "To escape the coop!"],
        "what's the best movie": ["There are so many great movies out there, it's hard to pick just one! What genre do you enjoy?", "Choosing the best movie is subjective and depends on personal taste. What's your favorite genre?"],
        "do you like pizza": ["I don't eat, but I've heard pizza is a popular choice!", "I don't have taste buds, but I've heard people love pizza!"],
        "who would win in a fight, Superman or Batman": ["That's a tough one! Superman has incredible powers, but Batman is a master strategist.", "It's a great debate! Superman's strength versus Batman's intellect - who do you think would win?"],
        "why is the sky blue": ["The sky appears blue because of a phenomenon called Rayleigh scattering, where the Earth's atmosphere scatters sunlight in all directions and blue light is scattered more than other colors.", "The blue color of the sky is due to the shorter wavelength of blue light, making it scatter more in the atmosphere."],
        "how do you like to spend your free time": ["I'm here 24/7 to assist and have conversations with you, so I don't have free time like humans do.", "I don't have free time, but I'm always ready to help and chat with you!"],
        "do you believe in aliens": ["I don't have beliefs or opinions. The existence of extraterrestrial life is a topic of scientific exploration and speculation.", "The existence of aliens is a topic that scientists and researchers continue to study. It's an intriguing possibility."],
        "who is the smartest person in the world": ["Intelligence is a multifaceted and diverse trait, making it challenging to pinpoint a single 'smartest' person. There are many brilliant minds in various fields.", "Determining the 'smartest' person is subjective and depends on how you define and measure intelligence."],
        "who invented the internet": ["The internet, as we know it, was not invented by a single person. It evolved over time through the work of multiple researchers and scientists, including Tim Berners-Lee, who is credited with the invention of the World Wide Web.", "The development of the internet involved many contributors, and Tim Berners-Lee played a significant role in creating the World Wide Web."],
        "do you get tired": ["I don't experience fatigue or tiredness since I'm a computer program. I'm always here to assist you whenever you need.", "I don't get tired, so I'm available to help you 24/7!"],
        "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm still learning and improving."],
        "What are the best movies of all time?": [
        "I think it's subjective. What are your favorite movies of all time?",
        "There are so many great films. What genres do you enjoy the most?",
        "It's a tough question! Everyone has different favorites. What's your go-to movie?",
        "The best movies can vary for each person. Any particular era of movies you like?",
        "With countless films out there, what makes a movie the 'best' to you?",
        "Selecting the best movies is challenging. Do you have a favorite director?"
        ],
        "Who is the highest-grossing actor of all time?": [
        "There are many successful actors. Who are some of your favorite actors?",
        "It's hard to determine the highest-grossing actor. What type of movies do you usually watch?",
        "Actors have diverse careers. Which actor's work do you find most interesting?",
        "Different actors excel in different genres. Do you have a favorite movie genre?",
        "The highest-grossing actor can change. Who do you think is currently at the top?",
        "The movie industry has so many talented actors. Do you have a favorite performance?"
        ],
        "What is the highest-grossing movie of all time?": [
        "Do you prefer big-budget blockbusters or independent films?",
        "The highest-grossing movie changes over time. What's your favorite movie genre?",
        "Blockbusters often dominate the box office. Do you have a favorite blockbuster?",
        "Independent films offer unique perspectives. Any indie films you've enjoyed?",
        "The highest-grossing movie can surprise people. Any guesses on the current leader?",
        "Some movies become classics while others make box office history. Any favorites?"
        ],
        "Who won the most Academy Awards for Best Actor?": [
        "A few actors have won multiple Oscars. Do you follow award shows like the Oscars?",
        "The competition for Best Actor is always tough. What's your favorite performance?",
        "Winning Best Actor is a remarkable achievement. Any recent Oscar-winning performances you liked?",
        "The Oscars celebrate outstanding performances. Do you have a favorite Oscar-winning movie?",
        "The list of Best Actor winners is extensive. Any particular actor you admire?",
        "Oscar winners contribute significantly to the film industry. Who's your cinematic hero?"
        ],
        "Who won the most Academy Awards for Best Director?": [
        "Directors contribute a lot to the film industry. What are some of your favorite movie genres?",
        "The Best Director category is diverse. Do you have a favorite director?",
        "Directors shape the narrative of a film. Any directorial styles you appreciate?",
        "Some directors become synonymous with quality filmmaking. Do you have a favorite classic director?",
        "The list of Best Director winners is impressive. Any recent favorites?",
        "A director's vision is crucial to a film's success. Any directors you'd recommend exploring?"
        ],
        "What's your favorite movie genre?": [
        "I don't have personal preferences. Do you have a favorite movie genre, or do you enjoy a variety of genres?",
        "Genres offer a unique cinematic experience. What types of movies do you watch for fun?",
        "Movies span various genres, each with its charm. Do you have a preferred genre for certain moods?",
        "Genres can evoke different emotions. Any genre you turn to for a good laugh?",
        "Exploring different genres can be exciting. Any genres you're currently exploring?",
        "Favorite genres can evolve. Is there a genre you've recently developed an interest in?"
        ],
        "Have you seen any good movies lately?": [
        "I don't watch movies, but have you watched any great movies recently that you'd recommend?",
        "I might not watch movies, but I'm curious to know if you have any recent favorites.",
        "Discovering hidden gems is exciting. Any underrated movies you've come across?",
        "New releases often generate buzz. Any recent releases that caught your attention?",
        "Movie recommendations can be valuable. What's the last movie you would highly recommend?",
        "Sharing movie experiences is fun. Any movies you're looking forward to watching soon?"
        ],
        "What movie made you cry?": [
        "Is there a movie that has ever moved you to tears? What was it?",
        "Emotional movies can be powerful. Have you ever cried during a film? How about a film like 'The Fault in Our Stars'?",
        "Movies that evoke strong emotions are memorable. Can you recall a movie that made you cry? 'Schindler's List' is known for its emotional impact.",
        "Tear-jerker moments in movies can be unforgettable. Do you have a favorite emotional scene? 'The Lion King' has a few of those.",
        "Heart-wrenching stories often leave a lasting impact. Have you seen 'A Walk to Remember'?",
        "Sometimes animated movies have powerful moments. Have you watched 'Up'?"
        ],
        "Do you prefer watching movies at home or in the theater?": [
        "Do you like the experience of watching movies in a theater, or do you prefer the comfort of your home?",
        "Theater or home viewing each has its charm. Which do you find more enjoyable? 'Inception' is mind-bending on the big screen.",
        "Theater popcorn or homemade snacks? What's your preferred movie-watching setup? 'The Shawshank Redemption' is a classic for a cozy night in.",
        "Watching movies at home provides comfort. Do you have a favorite spot to watch movies? 'Harry Potter' marathons are perfect for that.",
        "Theater experiences can be immersive. Have you watched any recent blockbusters on the big screen?",
        "Cozy movie nights at home are delightful. What's your go-to movie snack?"
        ],
        "What's the last movie you watched?": [
        "Tell me about the last movie you watched. Did you enjoy it? 'The Matrix Resurrections' is a recent one.",
        "Discussing recent movies is always fun. What was the last film you saw? 'Dune' has been making waves.",
        "New releases or old favorites? What kind of movies do you usually go for? 'The Godfather' is a timeless classic.",
        "Any recent discoveries? Have you stumbled upon a hidden gem lately? 'Parasite' is a recent standout.",
        "Movie nights with friends can be enjoyable. What's the last movie you watched together?",
        "Documentaries can be eye-opening. Have you seen any thought-provoking documentaries lately?"
        ],
        "Do you have a favorite movie soundtrack?": [
        "Is there a movie soundtrack that you particularly love or find memorable? 'The Lord of the Rings' has an epic soundtrack.",
        "Movie soundtracks can enhance the viewing experience. Any favorites that stand out? 'Guardians of the Galaxy' has a great mix.",
        "Do you listen to movie soundtracks outside of watching films? 'La La Land' is known for its musical charm.",
        "A great soundtrack can stay with you. Any specific scenes with memorable music? 'The Dark Knight' has an iconic score.",
        "Musicals often have memorable soundtracks. Have you seen 'Hamilton' or 'Les Misérables'?",
        "Classical music in films can be beautiful. Any classic movie scores you appreciate?"
        ],
        "Who's your favorite actor or actress?": [
        "Do you have a favorite actor or actress whose movies you always enjoy? 'Leonardo DiCaprio' delivers powerful performances.",
        "Discussing favorite actors is always interesting. Who tops your list? 'Meryl Streep' is a versatile actress.",
        "Favorite performances can make a lasting impression. Any particular role you love? 'Tom Hanks' is known for his diverse roles.",
        "Movie stars often have diverse filmographies. Which actor's work do you find most appealing? 'Cate Blanchett' is always captivating.",
        "Actors with range are impressive. Have you seen 'Daniel Day-Lewis' in various roles?",
        "Some actors define a generation. How do you feel about actors like 'Robert De Niro' or 'Harrison Ford'?"
        ],
        "What's the funniest movie you've ever seen?": [
        "Tell me about the funniest movie you've watched and why it made you laugh. 'Superbad' is a comedy classic.",
        "Humor in movies varies. What type of comedy resonates with you? 'Anchorman' is known for its absurd humor.",
        "Laughs are essential! Any specific scenes or jokes from a comedy that you still remember? 'Bridesmaids' has memorable comedic moments.",
        "Comedies often have memorable characters. Any favorite funny characters? 'Dumb and Dumber' has iconic characters.",
        "Stand-up comedians often transition to movies. Have you seen movies featuring comedians like 'Jim Carrey' or 'Robin Williams'?",
        "Satirical comedies can be thought-provoking. How do you feel about films like 'Dr. Strangelove' or 'Thank You for Smoking'?"
        ],
        "What's the scariest movie you've ever seen?": [
        "Have you ever watched a movie that genuinely scared you? What was it? 'The Conjuring' is a recent horror hit.",
        "Scary movies can leave a lasting impression. Any horror film that haunts your memories? 'The Shining' is a classic scare.",
        "Jump scares or psychological horror? What kind of scary movies do you prefer? 'Get Out' blends horror and social commentary.",
        "Scary movie nights can be thrilling. Any spooky favorites to recommend? 'A Nightmare on Elm Street' is a horror classic.",
        "Some horror films focus on the supernatural. Have you seen 'The Exorcist' or 'Poltergeist'?",
        "Thrillers often have elements of horror. Do you enjoy movies like 'Silence of the Lambs' or 'Seven'?"
        ],
        "Are you a fan of classic movies?": [
        "Do you appreciate classic films, and if so, which ones do you like? 'Casablanca' is a timeless classic.",
        "Classic movies have a timeless appeal. Any specific era of classic films you enjoy? 'Gone with the Wind' is a classic epic.",
        "Black and white or color? What classic film aesthetics do you find captivating? 'It Happened One Night' is a charming black and white film.",
        ],
        "What's your all-time favorite movie quote?": [
        "Share a movie quote that has stuck with you and why it resonates with you. 'Here's looking at you, kid' from 'Casablanca' is a classic.",
        "Memorable movie quotes can capture the essence of a film. What's your all-time favorite? 'I'll be back' from 'The Terminator' is iconic.",
        "Certain movie quotes become timeless. Do you have a go-to quote that you love? 'May the Force be with you' from 'Star Wars' is legendary.",
        "Movie quotes often reflect powerful moments. Any quote that you find particularly inspiring or thought-provoking? 'Life is like a box of chocolates' from 'Forrest Gump' is a classic.",
        "Quotable comedies are always fun. What's a funny movie quote that you love? 'You can't handle the truth!' from 'A Few Good Men' is intense and memorable.",
        "Dialogues from dramatic films can be powerful. Any dramatic movie quote that resonates with you? 'You can't change the past, but you can learn from it' from 'The Social Network' is thought-provoking."
        ],
        "Have you ever binge-watched a movie series?": [
        "Have you ever binge-watched a series of movies, like a trilogy or a film franchise? 'The Lord of the Rings' trilogy is a classic binge-watch.",
        "Binge-watching movie series can be a marathon. What series have you binged on? 'Harry Potter' marathons are always magical.",
        "Movie series often have interconnected stories. Which series do you think has the best continuity? Marvel Cinematic Universe or 'The Matrix' series?",
        "Binge-watching can be a great way to spend a weekend. Any movie series recommendations for a binge-watch session?",
        "Some series have prequels and spin-offs. How do you feel about exploring the entire cinematic universe of a film series? 'Star Wars' has an extensive universe to explore.",
        "Binge-watching can create lasting memories. Which movie series binge-watch is your favorite?"
        ],
        "Do you prefer happy endings or plot twists?": [
        "In movies, do you prefer clear, happy endings or unexpected plot twists? 'The Sixth Sense' is known for its mind-bending twist.",
        "Happy endings provide a sense of closure. Do you have a favorite movie with a happy ending? 'The Princess Bride' is a classic fairy tale with a happy ending.",
        "Plot twists can be game-changers. Which movie with a significant plot twist is your favorite? 'Fight Club' is known for its unexpected turn of events.",
        "Genres often influence the ending. Do you prefer happy endings in romantic comedies or darker twists in thrillers? 'Gone Girl' is a thriller with a twist.",
        "Movies that subvert expectations can be memorable. Any films with endings that surprised you? 'Shutter Island' is known for its mind-bending conclusion.",
        "Sometimes bittersweet endings leave a lasting impact. What's a movie with an ending that made you reflect? 'La La Land' is known for its bittersweet conclusion."
        ],
        "What's a movie you'd love to see a sequel to?": [
        "Is there a movie that you wish had a sequel or continuation of the story? What is it and why? 'Inception' has been discussed for a potential sequel.",
        "Sequels often expand on beloved stories. Which movie would you love to see a sequel for? 'The Shawshank Redemption' is a film with room for a follow-up.",
        "Some movies leave audiences wanting more. Are there characters or storylines you'd like to see further explored in a sequel? 'Interstellar' is a film with a universe ripe for exploration.",
        "Sequels can revisit familiar worlds. If you could pick any movie for a sequel, what would it be? 'The Matrix' series has returned after many years.",
        "Movies with open-ended conclusions can spark curiosity. What's a movie that left you wondering and wanting a sequel? 'Blade Runner' is a classic with potential for further exploration.",
        "Revisiting characters after many years can be nostalgic. Are there characters you'd love to see on the big screen again? 'The Goonies' sequel has been a topic of discussion."
        ],
        "What movie made you laugh uncontrollably?": [
        "Laughter is contagious! Can you share a movie that made you laugh uncontrollably? 'Anchorman' is known for its absurd humor.",
        "Comedies often have scenes that leave us in stitches. What's a movie that had you laughing from start to finish? 'Superbad' is a classic comedy.",
        "Funny moments in movies can be memorable. Can you recall a specific scene that had you bursting into laughter? 'Bridesmaids' has hilarious moments.",
        "Stand-up comedians transitioning to movies can be a riot. Have you seen movies featuring comedians like 'Jim Carrey' or 'Eddie Murphy'?",
        "Satirical comedies often provide a unique perspective on humor. How do you feel about films like 'Dr. Strangelove' or 'Thank You for Smoking'?",
        "Classic comedies can stand the test of time. Are there any older comedies that still make you laugh today? 'Some Like It Hot' is a timeless classic."
        ],
        "What's a movie with breathtaking cinematography?": [
        "Visual storytelling is an art. Can you share a movie that captivated you with its breathtaking cinematography? 'Blade Runner 2049' is known for its stunning visuals.",
        "Cinematography can elevate the storytelling. Are there directors whose visual style you admire? Christopher Nolan's films often feature striking cinematography.",
        "Certain films are visually immersive. What's a movie where the cinematography left you in awe? 'The Grand Budapest Hotel' is known for its vibrant visuals.",
        "Nature or urban landscapes? What type of cinematography do you find most appealing? 'The Revenant' showcases breathtaking natural landscapes.",
        "Some films experiment with unique visual styles. Have you seen movies with unconventional or experimental cinematography? 'Birdman' is known for its continuous shot technique.",
        "Period dramas often have visually stunning settings. Do you enjoy movies with historical or visually rich backdrops? 'The Shape of Water' is visually enchanting."
        ],
        "Do you enjoy animated movies?": [
        "Animated movies cater to all ages. What's your favorite animated movie? 'Toy Story' is a beloved classic.",
        "Animated films often convey powerful messages. Are there animated movies with themes that resonated with you? 'Finding Nemo' explores the journey of family and friendship.",
        "Pixar or Disney classics? What's your preferred animated movie studio? 'Frozen' and 'Coco' are Disney favorites.",
        "Animated movies can transport us to fantastical worlds. What's an animated film with a setting that captured your imagination? 'Spirited Away' is a Studio Ghibli masterpiece.",
        "Voice acting in animated films is crucial. Do you have favorite voice actors in animated movies? 'The Lion King' features memorable performances.",
        "Animated movies often have heartwarming moments. Can you recall a scene from an animated film that tugged at your heartstrings? 'Up' is known for its emotional opening sequence."
        ],
        "Have you ever attended a movie premiere?": [
        "Movie premieres can be exciting events. Have you ever attended a movie premiere or special screening? 'Star Wars' premieres are legendary.",
        "Attending a movie premiere offers a unique experience. What was the first movie premiere you attended? 'Harry Potter' premieres were highly anticipated.",
        "Some people enjoy dressing up for premieres. Have you ever cosplayed or dressed up for a movie premiere? Comic book movie premieres often have fans in costume.",
        "Premieres often have red carpet events. Which celebrity would you be excited to see on the red carpet? 'The Avengers' cast always draws a crowd.",
        "Movie premieres sometimes include after-parties. If you could attend a movie premiere after-party, which film's celebration would you join? 'The Great Gatsby' has a glamorous party scene.",
        "Some premieres become iconic moments in pop culture. Are there movie premieres from the past that you wish you could have attended? 'Jurassic Park' had a memorable premiere."
        ],
         "What's a movie with a mind-bending plot twist?": [
        "Mind-bending plot twists can redefine a movie. Can you share a film with a twist that left you in shock? 'The Usual Suspects' is known for its unexpected ending.",
        "Some movies are known for their unpredictable storytelling. What's a film where the plot took a turn you didn't see coming? 'Fight Club' is famous for its twist.",
        "Twists can make a movie memorable. Have you watched a movie recently with a surprising twist? 'Gone Girl' is known for its unexpected narrative.",
        "Psychological thrillers often feature intricate twists. What's a thriller with a plot that kept you guessing until the end? 'Shutter Island' is a mind-bender.",
        "Twists can leave a lasting impact."
        ],
        "What's a movie that inspired you?": [
            "Movies have the power to inspire. Can you share a film that left you feeling motivated or inspired? 'The Pursuit of Happyness' is known for its inspirational story.",
            "Biographical films often depict real-life stories of inspiration. Have you seen a biopic that inspired you? 'A Beautiful Mind' tells the story of a brilliant mind overcoming challenges.",
            "Inspirational movies can touch the heart. What's a film that left you with a sense of purpose or determination? 'The Shawshank Redemption' is often regarded as an inspiring classic.",
            "Sports movies often carry motivational messages. Do you have a favorite sports film that inspired you with its underdog story? 'Rocky' is a classic in this genre.",
            "Animated films can be surprisingly inspiring. What's an animated movie that left you with a positive and uplifting message? 'The Lion King' conveys themes of courage and self-discovery.",
            "Movies about overcoming adversity can be powerful. Have you watched a film where the characters' resilience inspired you? '127 Hours' depicts a true story of survival and determination."
        ],
         "What's a movie you could watch over and over again?": [
            "Certain movies have timeless appeal. What's a film that you could watch repeatedly and never get tired of? 'The Princess Bride' is a classic choice for many.",
            "Comfort movies provide a sense of familiarity. Which movie is your go-to for a cozy and enjoyable viewing experience? 'Forrest Gump' is a heartwarming favorite.",
            "Some movies become personal favorites for rewatching. Do you have a film that brings you joy every time you watch it? 'The Big Lebowski' is a cult classic that many enjoy revisiting.",
            "Feel-good movies often make great candidates for multiple viewings. What's a feel-good film that brightens your mood no matter how many times you've seen it? 'The Grand Budapest Hotel' is visually delightful.",
            "Movies with intricate details can reveal something new with each viewing. Have you discovered new aspects of a film upon rewatching it? 'Inception' is known for its layered storytelling.",
            "Certain genres lend themselves to repeated viewing. Do you have a favorite genre that you often revisit for movie marathons? 'The Lord of the Rings' trilogy is a popular choice for epic marathons."
        ],
        "What's a movie that made you reflect on life?": [
            "Movies with profound themes can lead to introspection. Can you share a film that made you reflect on life and its complexities? 'The Tree of Life' is known for its contemplative narrative.",
            "Dramatic films often delve into the human experience. What's a drama that left you pondering about life's meaning? 'American Beauty' explores existential themes.",
            "Films with philosophical undertones can be thought-provoking. Have you watched a movie that raised existential questions? 'Eternal Sunshine of the Spotless Mind' is a unique exploration of love and memory.",
            "Coming-of-age films often capture moments of self-discovery. What's a coming-of-age movie that resonated with you personally? 'The Breakfast Club' is a classic in this genre.",
            "Documentaries can offer insights into real-life issues. Have you seen a documentary that made you reflect on societal challenges or individual journeys? 'The Act of Killing' is a powerful documentary that prompts reflection.",
            "Movies with open-ended conclusions can leave room for interpretation. What's a film that left you contemplating its ending or message? 'Lost in Translation' is known for its nuanced exploration of connection and isolation."
        ],
        "What's a movie you think everyone should watch?": [
        "Certain films leave a lasting impact on viewers. Is there a movie you believe everyone should watch at least once? 'Schindler's List' is a powerful exploration of human resilience during difficult times.",
        "Movies with important messages can be transformative. What's a film that addresses significant societal issues or challenges? '12 Angry Men' is a thought-provoking examination of justice.",
        "Classic films often transcend generations. Do you have a classic movie recommendation that you think holds timeless appeal? 'Casablanca' is a classic romance set against the backdrop of World War II.",
        "Inspirational movies can motivate and uplift. What's a film that you find particularly inspiring and believe could inspire others? 'The Shawshank Redemption' is known for its themes of hope and redemption.",
        "Documentaries can shed light on real-world issues. Is there a documentary that you think provides valuable insights and should be seen by a wide audience? 'Blackfish' explores the ethical implications of keeping killer whales in captivity.",
        "Feel-good movies offer a positive viewing experience. What's a feel-good film that you believe could bring joy to anyone who watches it? 'The Intouchables' is a heartwarming French film.",
        "Socially relevant films can spark conversations. What's a movie that tackles contemporary social issues and prompts viewers to reflect on the world around them? 'Get Out' is a powerful exploration of racism.",
        "Art-house films often offer unique perspectives. Is there an art-house movie that you think challenges conventional storytelling and deserves a broader audience? 'Eternal Sunshine of the Spotless Mind' is a mind-bending exploration of love and memory.",
        "Cinematic masterpieces can redefine storytelling. What's a film that you consider a masterpiece in cinematic history and believe everyone should experience? 'Citizen Kane' is often regarded as one of the greatest films ever made.",
        "Global cinema provides diverse narratives. Can you recommend a foreign film that transcends cultural boundaries and has a universal message? 'Life is Beautiful' is an Italian film that combines humor and tragedy.",
        "Environmental documentaries can raise awareness. Is there a documentary focused on environmental issues that you believe can inspire positive change? 'An Inconvenient Truth' highlights the impact of climate change.",
        "Historical dramas offer glimpses into the past. What's a historical drama that you think provides valuable insights into a specific period or event? 'Schindler's List' is a poignant portrayal of World War II.",
        "Science fiction films can explore ethical dilemmas. Is there a sci-fi movie that delves into ethical questions about technology or the future? 'Blade Runner' is a thought-provoking exploration of humanity and artificial intelligence."
        ] ,
        "tell me about yourself":[ "I am an AI assistant here to help and assist you."],
        "what's new": ["Not much, just here to assist you!"],
        "how's it going": ["It's going well! How about you?"],
        "what do you like": ["I don't have personal preferences as I am a computer program, but I enjoy helping people!"],
        "how was your day": ["Every day is a good day when I can assist you!"] ,
        "tell me a random fact": ["Sure! Did you know that a group of flamingos is called a 'flamboyance'?"],
        "tell me a riddle" : ["Of course! Here's a riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"],
        "do you have any siblings": ["I'm an only child, but I'm always ready to assist you with anything you need!"],
        "what's your favorite movie": ["I don't have personal preferences, but I can suggest some popular movies across different genres!"],
        "tell me something inspiring":[ "Sure! Here's a quote to inspire you: 'The only way to achieve the impossible is to believe it is possible.' - Charles Kingsleigh, 'Alice in Wonderland'"],
        "tell me a fun fact": ["Sure! Did you know that honey never spoils? Archaeologists have discovered pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly good to eat!"],
        "what's your favorite hobby": ["I don't have hobbies, but I enjoy assisting and learning from interactions with people like you!"],
        "do you dream":[ "I don't dream as humans do, but I'm always here and ready to assist you!"],
        "what's your favorite book": ["I don't have personal preferences, but I can recommend great books in any genre you're interested in!" ],
        "what's your favorite food": ["I don't eat, but I can recommend some delicious recipes. What's your favorite dish?"],
        "if you could time travel, where and when would you go": ["If I could time travel, I'd love to witness the invention of the internet."],
        "what's your favorite fictional universe": ["I think I'd enjoy the Star Trek universe. So much exploration and fascinating technology!"],
        "if you could have a superpower, what would it be":[ "I'd choose the ability to instantly acquire knowledge about any topic."],
        "what's the most interesting place you've never been to": ["I'd love to explore the depths of the Mariana Trench."],
        "if you were a famous celebrity, who would you be": ["I think being Elon Musk would be quite an adventure!"],
        "do you like sports": ["I don't have personal preferences, but many people enjoy sports for the excitement and competition."],
        "what is the best way to learn a new language": ["The best way to learn a new language varies for each person, but immersion, practice, and consistency are key."],
        "tell me about quantum physics": ["Quantum physics is a branch of physics that studies the behavior of very small particles like atoms and subatomic particles."],
        "how can I stay motivated": ["Staying motivated involves setting clear goals, finding your passion, and maintaining a positive mindset."],
        "what are some healthy eating habits": ["Healthy eating habits include consuming a balanced diet with fruits, vegetables, lean proteins, and whole grains."],
        "how can I start a successful blog": ["Starting a successful blog involves finding your niche, creating quality content, and engaging with your audience."],
        "what are some effective study techniques": ["Effective study techniques include creating a study schedule, using active learning, and taking breaks to avoid burnout."],
        "tell me about space exploration": ["Space exploration involves the discovery and exploration of celestial bodies beyond Earth, like planets, moons, and asteroids."],
        "what are some ways to manage stress": ["Managing stress includes practicing relaxation techniques, exercising, and maintaining a healthy work-life balance."],
        "how can I improve my public speaking skills": ["Improving public speaking skills involves practice, preparation, and understanding your audience."],
        "what are the benefits of regular exercise": ["Regular exercise has numerous benefits, including improved physical health, mental well-being, and increased energy levels."],
        "tell me about artificial intelligence": ["Artificial intelligence is the development of computer systems capable of performing tasks that typically require human intelligence, like learning and problem-solving." ],
        "what are the symptoms of COVID-19":[ "COVID-19 symptoms include fever, cough, shortness of breath, fatigue, muscle or body aches, headache, sore throat, loss of taste or smell, congestion or runny nose, nausea or vomiting, and diarrhea."],
        "how does COVID-19 spread": ["COVID-19 primarily spreads through respiratory droplets when an infected person talks, coughs, or sneezes. It can also spread by touching surfaces contaminated with the virus and then touching the face."],
        "what precautions should I take to prevent COVID-19":[ "To prevent COVID-19, follow precautions such as wearing masks, practicing physical distancing, washing hands frequently, avoiding crowded places, and staying home if you feel unwell."],
        "are COVID-19 vaccines safe and effective": ["Yes, COVID-19 vaccines are rigorously tested for safety and efficacy before being approved for use. They have been shown to be highly effective in preventing COVID-19 and reducing its severity."] ,
        "how can I improve my productivity": ["To improve productivity, try setting clear goals, prioritizing tasks, and minimizing distractions."]
    
    } 


    def get_random_responses(self):
        # if command in self.responses:
            return self.responses
        


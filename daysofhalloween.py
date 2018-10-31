from pyfiglet import Figlet

fonts = ['poison', 'bubble', 'tombstone', 'univers', 'tinker-toy', 'thin', 'thick', 'starwars', 'shadow', 'serifcap', 'sblood', 'roman', 'rev', 'pyramid', 'pebbles', 'ogre', 'nancyj-fancy', 'moscow', 'marquee', 'letters', 'isometric2', 'invita', 'gothic', 'fuzzy', 'doom', 'digital', 'cybermedium', 'cosmic', 'contessa', 'colossal', 'caligraphy', 'barbwire']
used = ['poison']

f = Figlet(font=fonts[3], width=100)
print(f.renderText('31 Days of Halloween'))


quotes = ["", "Oh look, another glorious morning...makes me sick", "Double, double toil and trouble; Fire burn and caldron bubble.", "It's October 3rd.", "Be afraid..be VERY afraid.", "I would like, if I may, to take you on a strange journey.", "Magic is really very simple, all you’ve got to do is want something and then let yourself have it.", "I’ve seen enough horror movies to know that any weirdo wearing a mask is never friendly.", "I'm a homicidal maniac, they look just like everyone else.", "Villainy wears many masks, none so dangerous as the mask of virtue.", "We came, we saw, we kicked its ass.", "Where there is no imagination, there is no horror.", "Nothing on earth is so beautiful as the final haul on Halloween night.", "I put a spell on you because you're mine.", "Being normal is vastly overrated.", "There is a child in every one of us who is still a trick-or-treater looking for a brightly-lit front porch.", "Clothes make a statement. Costumes tell a story.", "We're all mad here.", "Listen to them, the children of the night. What music they make!", "I see dead people.", "Hell is empty. All the devils are here.", "I'm every nightmare you've ever had. I am your worst dream come true. I am everything you ever were afraid of!", "I fear not the dark itself, but what may lurk within it.", "By the pricking of my thumbs, something wicked this way comes.", "Magic is really very simple, all you've got to do is want something and then let yourself have it.", "It's Halloween; everyone's entitled to one good scare.", "There are nights when the wolves are silent and only the moon howls.", "I'm so glad I live in a world where there are Octobers.", "Heeeeere's Johnny!", "They're Heeeeereeee.", "I ate his liver with some fava beans and a nice chianti.", "It's alive! It's alive!"]

movies = [
	{'title': 'It', 'run_time': 135, 'quote': "We all float down here.", 'year': 2017, 'genre': 'thriller'}, 
	{'title': 'Rose Red', 'run_time': 255, 'quote': "Houses... are alive. This is something we know. News from our nerve endings. If we're quiet, if we listen, we can hear houses breath. Sometimes, in the depth of the night, you can even hear them groan. It's as if they were having bad dreams. A good house cradles and comforts, a bad one fills us with instinctive unease. Bad houses hate our warmth and our human-ness. That blind hate of our humanity is what we mean when we use the word haunted.", 'year': 2002, 'genre': 'thriller'}, 
	{'title': 'Psycho', 'run_time': 109, 'quote': "A boy's best friend is his mother.", 'year': 1960, 'genre': 'psychological horror'}, 
	{'title': 'Hocus Pocus', 'run_time': 96, 'quote': "It's just a little hocus pocus!", 'year': 1993, 'genre': 'family'},
	{'title': 'Final Girls', 'run_time': 91, 'quote':"Ever since I was a little boy, I've dreamed of being the final girl.", 'year': 2015, 'genre': 'comedy'},
	{'title': 'A Quiet Place', 'run_time': 91, 'quote': "We have to protect them.", 'year': 2018, 'genre': 'thriller'},
	{'title': 'Get Out', 'run_time': 104, 'quote': "All I know is sometimes, when there's too many white people, I get nervous, you know?", 'year': 2017, 'genre': 'thriller'},
	{'title': 'Night of the Living Dead', 'run_time': 97, 'quote': "They're coming to get you Barbara.", 'year': 1968, 'genre': 'zombie'},
	{'title': 'Texas Chainsaw Massacre', 'run_time': 90, 'quote': "You like this face?", 'genre': 'slasher', 'year': 1974},
	{'title': 'Fright Night', 'run_time': 108, 'quote': "Welcome to Fright Night...For real.", 'genre': 'comedy', 'year': 1985},
	{'title': 'Halloweentown', 'run_time': 84, 'quote': "Magic is really very simple, all you\'ve got to do is want something and then let yourself have it.", 'genre': 'family', 'year': 1998},
	{'title': 'Halloween', 'run_time': 101, 'quote': "Was that the Boogeyman?", 'year': 1978, 'genre': 'slasher'},
	{'title': 'Halloween', 'run_time': 109, 'quote': "He’s waited for this night. He’s waited for me. I’ve waited for him.", 'year': 2018, 'genre': 'slasher'},
	{'title': 'Young Frankenstein', 'run_time': 106, 'quote': "Hallo. Vould you like to have a roll in ze hay?", 'year': 1974, 'genre': 'comedy'},
	{'title': 'Frankenstein', 'run_time': 120, 'quote': "IT\'S ALIVE!", 'year': 1931, 'genre': 'monster'},
	{'title': 'American Psycho', 'run_time': 104, 'quote': "Howard, it's Bateman, Patrick Bateman. You're my lawyer so I think you should know: I've killed a lot of people.", 'year': 2000, 'genre': 'black comedy'},
	{'title': 'All the Boys Love Mandy Lane', 'run_time': 90, 'quote': "There she is boys, Mandy Lane. Untouched, pure. Since the dawn of junior year men have tried to possess her, and to date all have failed. Some have even died in their reckless pursuit of this angel.", 'year': 2006, 'genre': 'teen horror'},
	{'title': 'Saw', 'run_time': 103, 'quote': "I want to play a game. ", 'year': 2004, 'genre': 'toture porn'},
	{'title': 'The Blair Witch Project', 'run_time': 105, 'quote': " I'm scared to close my eyes, I'm scared to open them! We're gonna die out here! ", 'year': 1999, 'genre': 'found footage'},
	{'title': 'Poltergeist', 'run_time': 120, 'quote': "", 'year': 1982, 'genre': 'supernatural'}]

def days_of_halloween(day):
	days_left = 31 - day
	print(quotes[day])
	print("Happy October {}! There are {} days left for spooky fun.".format(day, days_left))
	if days_left == 0:
		return "TIME'S UP!!! Until next year..."

	inp = input('Today\'s Movie: ')
	output = ''

	for movie in movies:
		if inp == movie['title']:
			hours = movie['run_time'] // 60
			minute = movie['run_time'] % 60
			output = movie['quote'] + "\n {} hour(s) {} minutes of spooky fun coming your way.".format(hours, minute) if movie['genre'] == 'family' or movie['genre'] == 'comedy' else movie['quote'] + "\n" + "{} hour(s) {} minutes of terror coming your way.".format(hours, minute)
			output += "\n Release date: " + str(movie['year'])
			output += "\n Horror subgenre: " + movie['genre']

	print(output)
	


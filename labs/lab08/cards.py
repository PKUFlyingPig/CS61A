# All cards available in a standard deck.
from classes import *

#TAs
aaron = TACard('Baron Aaron', 2100, 1300)
addison = TACard('Addison, from operator import add', 1000, 2000)
albert = TACard('Albert, Lethargy Incarnate', 1000, 2000)
alex_k = TACard('Alex, Skipper of Labs and Preparer for Exams', 2293.141593, 1111.11111)
alex_s = TACard('President Lieutenant Stennet for Senate', 1400, 2000)
aman = TACard('Aman', 1000, 2100)
amrita = TACard('Amrita, the Pun-stoppable', 1800, 1450)
annie = TACard('Annie, the Annihilator of Water', 1700, 1500)
audrey = TACard('Audrey, Excitable Engineer', 1777, 1777)
brandon = TACard('Brandon, Not Brendan ', 1234, 1234)
catherine = TACard('Catherine, Referencer of Self', 2500, 900)
cesar = TACard('Cesar, Surveyor of Steaz', 1337, 2222)
chae = TACard('Chae', 1500, 1900)
charles = TACard('Charles, Protector of UwU', 1000, 2000)
dalton = TACard('Dalton, Unit of Atomic Mass', 2144, 1998)
danelle = TACard('Danelle Nachos', 2200, 1100)
derek = TACard('Derek, The Wan and Only', 2000, 1000)
derrick = TACard('EZ4ENCE', 1100, 2000)
griffin = TACard('Griffin, He Who is Hydrated', 1000, 2000)
jack = TACard('Jack, The Master of Dice', 1650, 2100)
jade = TACard('Jade, Singher of Songs', 1700, 1500)
kavi = TACard('Kavi Gupta', 2100, 1000)
lillian = TACard('Lillian, Linda', 1100, 2100)
nancy = TACard('Nancy, The Sheep in the Jeep', 1100, 2100)
patricia = TACard('Patricia, Pokémon Master', 1800, 1600)
paul = TACard('Better Call Paul', 2100, 1200)
regina = TACard('Regina, Wrangler of Skipped Readings', 1200, 2250)
richard = TACard('Richard, Admirer of Baby Yoda ', 1800, 2000)
sean = TACard('Sean, the Over-Caffeinated', 1000, 2300)
shayna = TACard('Shayna, Procrastinator Supreme', 1916, 1459)
yannan = TACard('Yannan, the Yammeister', 1500, 1900)
yichen = TACard('Yichen, Drinker of Boba', 1800, 1500)

#Tutors
christine = TutorCard('Christine', 1500, 1700)
ethan = TutorCard('Ethan, Pillar of the Demon Slayer Corps', 1800 , 1100)
grant = TutorCard('Grant', 1100, 2100)
ivan = TutorCard('Ivan, the ender of dreaming the starter of scheming', 1900, 2300)
jason = TutorCard('Jason, Counter of Chang-e', 1500, 1900)
jemmy = TutorCard('Jemmy, the Joker', 1200, 1700)
jessica = TutorCard('Jessica, Lover of Shin Ramen', 1528, 2154)
lauren = TutorCard('Lauren, Queen of First Floor Moffitt', 1200, 1800)
matthew = TutorCard('Matty Lee', 2000, 1500)
nicholas = TutorCard('Nicholas, Keeper of Shared Secrets', 1009, 2297)
nikhita = TutorCard('Nikhita, Always Schemin', 1700, 1700)
uma = TutorCard('Uma, Hoarder of Hydroflasks', 1200, 1700)




# Professors
denero = ProfessorCard('John DeNero, Protector of Abstraction Barriers', 5000, 5000)

# A standard deck contains all standard cards.
standard_cards = [denero, aaron, addison ,albert ,alex_k ,alex_s ,aman ,amrita ,annie ,audrey ,brandon ,catherine ,cesar ,chae ,charles ,dalton ,danelle ,derek ,derrick ,griffin ,jack ,jade ,kavi ,lillian ,nancy ,patricia ,paul ,regina ,richard ,sean ,shayna ,yannan ,yichen ,ethan ,grant ,ivan ,jason ,jemmy ,jessica ,lauren ,matthew ,nicholas ,nikhita ,uma]
standard_deck = Deck(standard_cards)

# The player and opponent's decks are the standard deck by default.
player_deck = standard_deck.copy()
opponent_deck = standard_deck.copy()


#CS50 week 0 problem set INDOOR VOICE AND PLAYBACK SPEED

Message = input("what is the message? \n")

# Input in lower case == Indoor Voice
Indoor_voice = Message.lower()
print(f"\n 1. Indoor Voice = {Indoor_voice} \n")

# Have to put ... insted of whitespace == playback speed
Playback_speed = Indoor_voice.title().replace(" ","...")
print(F" 2. Plackback speed = {Playback_speed}\n")

# Have to replace :) with 🙂 & :( with 🙁 == Faces
FACES = Message.replace(":)", "🙂").replace(":(","🙁")
print(F" 3. FACES = {FACES}\n")
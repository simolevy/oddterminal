from flask import Flask, request, jsonify
import pyfiglet
from flask_cors import CORS
import random 

app = Flask(__name__)
CORS(app)  

conversation_history = []

COLORS = [
    "\033[31m",  # Red
    "\033[32m",  # Green
    "\033[33m",  # Yellow
    "\033[34m",  # Blue
    "\033[35m",  # Magenta
    "\033[36m",  # Cyan
    "\033[37m",  # White
    "\033[91m",  # Bright Red
    "\033[92m",  # Bright Green
    "\033[93m",  # Bright Yellow
    "\033[94m",  # Bright Blue
    "\033[95m",  # Bright Magenta
    "\033[96m",  # Bright Cyan
]

RESET = "\033[0m"  # Reset color

def generate_ascii(text):
    fonts = ["slant", "doom", "graffiti", "small", "shadow", "starwars", "starwars", "larry3d"]
    font_choice = random.choice(fonts)  # Randomly pick a font

    ascii_text = pyfiglet.figlet_format(text, font=font_choice)

    glitch_chars = ["█", "▒", "░", "▓", "#", "@", "?", "/", "\\", "꒰ᐢ. .ᐢ꒱₊˚⊹", "࿔‧ ֶָ֢˚˖𐦍˖˚ֶָ֢ ‧࿔", "𓆝 𓆟 𓆞", "♪ ˖ ⊹ ♬˚₊‧"]
    ascii_lines = ascii_text.split("\n")

    words = text.split()
    random.shuffle(words)

    for i in range(len(ascii_lines)):
        if random.random() > 0.6:  # 60% chance to glitch
            ascii_lines[i] = "".join(random.choice(glitch_chars) if random.random() > 0.5 else char for char in ascii_lines[i])

        if random.random() > 0.8:  # 20% chance to invert
            ascii_lines[i] = ascii_lines[i][::-1]

    # join modified lines again
    glitched_ascii = "\n".join(ascii_lines)

    return glitched_ascii

@app.route("/")  
def home():
    return "Flask server is running! Send POST requests to /ascii."

@app.route("/ascii", methods=["POST"])
def ascii_endpoint():
    data = request.json
    text = data.get("text", "Hello")
    
    conversation_history.append(text)
    if len(conversation_history) > 5:
        conversation_history.pop(0)

    print(f"Conversation history: {conversation_history}")  # Debugging

    if len(conversation_history) == 5:
        combined_text = " ".join(random.sample(conversation_history, k=min(3, len(conversation_history))))  
        ascii_art = generate_ascii(combined_text)
        conversation_history.clear()  
    else:
        ascii_art = f"(...) Stored your response. Need {5 - len(conversation_history)} more."

    return jsonify({"ascii_art": ascii_art})


    #ascii_art = generate_ascii(text)
    #return jsonify({"ascii_art": ascii_art})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
from model import analyze_mood

app = Flask(__name__)

@app.route('/analyze-mood', methods=['POST'])
def analyze_mood_route():
    mood_text = request.form.get("mood")
    mood_image = request.files.get("image")
    
    mood = analyze_mood(mood_text, mood_image)
    playlist = get_playlist(mood)
    
    return jsonify({"playlist": playlist})

def get_playlist(mood):
    playlists = {
        "happy": ["Happy - Pharrell Williams", "Walking on Sunshine - Katrina"],
        "sad": ["Someone Like You - Adele", "Let Her Go - Passenger"],
        "neutral": ["Here Comes the Sun - The Beatles", "Imagine - John Lennon"]
    }
    return playlists.get(mood, playlists["neutral"])

if __name__ == "__main__":
    app.run(debug=True)

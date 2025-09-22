from flask import Flask, render_template, Response, jsonify
import cv2
import hand_utils
import random
import threading

app = Flask(__name__)

# Try multiple camera indexes automatically
def get_camera():
    for i in range(3):  # try 0, 1, 2
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ Using camera index {i}")
            return cap
    print("❌ No webcam found!")
    return None

cap = get_camera()
game_state = {"player_score": 0, "computer_score": 0, "status": "playing", "winner": None}

# Background thread for continuous hand recognition + game logic
def game_loop():
    global cap, game_state
    while True:
        if cap is None:
            break
        ret, frame = cap.read()
        if not ret:
            continue

        # Detect player number
        player_num = hand_utils.detect_number(frame)
        if player_num is not None:
            computer_num = random.randint(1, 6)

            if player_num == computer_num:
                game_state["status"] = "out"
                game_state["winner"] = "Computer"
            else:
                game_state["player_score"] += player_num
                game_state["computer_score"] += computer_num

            # End game if score reaches 30
            if game_state["player_score"] >= 30:
                game_state["status"] = "ended"
                game_state["winner"] = "Player"
            elif game_state["computer_score"] >= 30:
                game_state["status"] = "ended"
                game_state["winner"] = "Computer"

        # Draw landmarks
        frame = hand_utils.draw_hands(frame)

        # Store frame for streaming
        _, jpeg = cv2.imencode('.jpg', frame)
        game_state["frame"] = jpeg.tobytes()

threading.Thread(target=game_loop, daemon=True).start()

def generate_frames():
    while True:
        if "frame" in game_state:
            frame = game_state["frame"]
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/game_state')
def get_state():
    return jsonify(game_state)

if __name__ == '__main__':
    app.run(debug=True)

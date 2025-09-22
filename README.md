🏏 Hand Cricket Game (AI + Flask + OpenCV + Mediapipe)
📌 Overview

This project is a Hand Cricket Game 🎮 that combines AI-powered hand recognition with Flask and OpenCV.
Play cricket with your webcam — no keyboard required! ✋
The system detects hand gestures, updates the score 🏏, plays sound effects 🔊, and finally announces the result (Win 🎉 or Lose ❌).

✨ Features

✅ AI Hand Gesture Recognition (via Mediapipe)

✅ Automatic Score Detection (no manual button clicks)

✅ Sound Effects 🎵

🔔 score.mp3 → When you score runs

💥 out.mp3 → When you get out

🎉 win.mp3 → When you win the game

✅ Real-time Webcam Feed (OpenCV + Flask Streaming)

✅ Interactive & Colorful Frontend (HTML + CSS + JS)

✅ Game End Alerts → Displays winner or loser at the end

📂 Project Structure
HAND_CRICKET/
│
├── app.py               # Flask backend
├── hand_utils.py        # Hand recognition + cricket logic
├── requirements.txt     # Dependencies
│
├── templates/
│   └── index.html       # Main frontend page
│
├── static/
│   ├── scripts.js       # JavaScript logic
│   └── style.css        # CSS for styling
│
└── sounds/              # Sound effects
    ├── out.mp3
    ├── score.mp3
    └── win.mp3

⚙️ Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/your-username/hand-cricket.git
cd hand-cricket


2️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Run the Application

python app.py


5️⃣ Open in Browser
👉 http://127.0.0.1:5000

🕹️ How to Play

🎥 Show your hand ✋ in front of the webcam.

☝️ 1 finger → Run = 1

✌️ 2 fingers → Run = 2

… up to 6 fingers

🤖 Computer will also choose a number.

If both numbers match → OUT ❌

Otherwise, your score increases ✅

🎯 Game ends when:

You get OUT ❌, OR

You win by reaching the target 🏆

📸 Screenshots

📷 Add gameplay screenshots here (from static/ or taken while playing).

🚀 Tech Stack

🔹 Backend → Flask

🔹 Frontend → HTML, CSS, JavaScript

🔹 AI/ML → Mediapipe (Hand Tracking)

🔹 Computer Vision → OpenCV

🔹 Audio → HTML5 <audio> + JS

🎯 Future Improvements

👥 Multiplayer Mode

📱 Mobile-friendly UI

🎚️ Difficulty Levels

📊 Scoreboard History

🙌 Acknowledgements

🤝 Mediapipe
 → For hand recognition

🤝 OpenCV
 → For computer vision

🤝 Flask
 → For backend framework

✨ Developed with ❤️ for fun and learning.

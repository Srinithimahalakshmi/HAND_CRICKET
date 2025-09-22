function updateGameState() {
    fetch("/game_state")
        .then(response => response.json())
        .then(data => {
            document.getElementById("player_score").innerText = data.player_score;
            document.getElementById("computer_score").innerText = data.computer_score;
            document.getElementById("status").innerText = data.status === "playing" ? "Game in Progress..." :
                                                         data.status === "out" ? "You're OUT! ❌" :
                                                         `Game Over! Winner: ${data.winner}`;

            // Play sounds
            if (data.status === "out") {
                document.getElementById("outSound").play();
            } else if (data.status === "ended") {
                document.getElementById("winSound").play();
            } else {
                document.getElementById("scoreSound").play();
            }
        });
}

setInterval(updateGameState, 2000);

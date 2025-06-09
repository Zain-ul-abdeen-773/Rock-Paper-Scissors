# 🎮 Rock-Paper-Scissors AI Challenge

Welcome to the **Rock-Paper-Scissors** AI project — a console-based game where your AI player competes against various intelligent bots! 🤖✊✋✌️

---

## 🚀 Project Overview

This project challenges you to create a smart AI that **learns and adapts** to opponents’ moves to consistently win Rock-Paper-Scissors games. Unlike random play, your AI should analyze the opponent's history and predict their next move to win at least **60% of games** against four different AI bots.

---

## 🧩 How It Works

- Your AI player function receives the opponent’s **last move** every turn.
- It keeps track of the opponent's move history to identify **patterns and tendencies**.
- By analyzing recent moves, it predicts the opponent’s next move.
- Then it **counters** the prediction by choosing the winning move:
  - Rock (🪨) beats Scissors (✌️)
  - Paper (📄) beats Rock (🪨)
  - Scissors (✌️) beats Paper (📄)

---

## 🤖 Opponent Bots Included

- **Quincy**: Cycles through moves in a fixed pattern.
- **Mrugesh**: Tracks most frequent moves in last 10 plays.
- **Kris**: Counters opponent’s last move.
- **Abbey**: Uses two-move sequences to predict next play.

---

## 📂 Project Structure

- `RPS.py` — Your AI logic goes here.
- `RPS_game.py` — Game engine simulating matches and bots.
- `main.py` — Run and test your AI against different opponents.
- `test_module.py` — Unit tests to validate your AI’s performance.

---

## 💻 Running the Project

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/rock-paper-scissors.git
   cd rock-paper-scissors

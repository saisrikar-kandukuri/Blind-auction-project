# Blind Auction System (Python)

This project is a simple **Blind Auction program** built using Python. It allows multiple users to place bids privately and determines the winner based on the highest bid. The program also handles **tie situations**, where multiple bidders have the same highest bid.

---

## 🚀 Features

- Collects multiple user bids
- Stores data using Python dictionaries
- Determines the highest bidder
- Handles **draw/tie cases**
- Simple terminal-based interaction
- Clean and modular logic

---

## 🧠 How It Works

1. Each user enters:
   - Their name
   - Their bid amount
2. The program asks if there are more bidders.
3. If yes → clears the screen and continues
4. If no → calculates the winner
5. Checks:
   - If one highest bidder → prints winner
   - If multiple highest bidders → prints draw

---


---

## 🛠️ Concepts Used

- Dictionaries (`key-value pairs`)
- Loops (`while`, `for`)
- Conditional statements (`if-else`)
- Lists
- Functions (optional improvement)
- Built-in functions:
  - `max()`
  - `.values()`
  - `.append()`
  - `.join()`

---

## 📁 Project Structure
blind-auction/
│
├── main.py
├── art.py
└── README.md

## ⚠️ Limitations

- No input validation (e.g., non-numeric bids)
- Same names overwrite previous bids
- Console-based UI only

---

## 🔮 Future Improvements

- Add input validation
- Prevent duplicate names
- Use GUI (Tkinter or web app)
- Store bids in file/database
- Add tie-break rules

---

## 👨‍💻 Author

SaiSrikar  

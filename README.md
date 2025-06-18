# 💰 Affordability Checker - Budget Comparison Script

## 🎯 Project Overview

This is a simple Python console script that allows users to enter a budget and check whether they can afford any predefined items (e.g. cars) based on their input. The script continuously prompts the user until they choose to exit.

This project demonstrates fundamental concepts in Python such as:

- User input handling
- Conditional logic
- Loops
- Exception handling
- Dynamic user interaction

---

## 🚀 Features

- Console-based interactive budget checker.
- Predefined price list for multiple items.
- Graceful exit option (`0` to quit).
- Input validation with error handling for non-integer inputs.
- Infinite loop with exit option for continuous checking.

---

## 🧠 How It Works

1. The script defines a price list for multiple items:
    - Car 1: $10,000
    - Car 2: $20,000
    - Car 3: $40,000

2. The user is repeatedly prompted to enter their available budget or type `0` to exit.

3. For each budget input:
   - The script checks which cars are affordable.
   - If none are affordable, an appropriate message is shown.
   - The loop continues until the user types `0`.

---

## 🛠️ Technologies Used

- **Python 3.x**
- Standard Python libraries only

---

## 📂 File Structure


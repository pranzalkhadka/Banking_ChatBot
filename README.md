# Banking_ChatBot

This is a chatbot project built using Rasa. The chatbot allows users to check their account balance and transaction history.

## Installation

1. Install rasa:
pip install rasa

2. Clone the repository:
git clone https://github.com/pranzalkhadka/Banking_ChatBot.git

3. Navigate to the project directory:
cd Banking_ChatBot

4. Create and activate a virtual environment (optional):
python3 -m venv rasavenv
source venv/bin/activate

5. Install the required dependencies:
pip install -r requirements.txt

## Usage

1. Train the chatbot model:
rasa train

2. Start the chatbot server:
rasa run actions
rasa shell

3. Interact with the chatbot:
User: hi

Chatbot: Hello! How can I assist you today?

User: I want to check my acount balance 

Chatbot: Please provide your account number.

User: 8904

Chatbot: Dear Pranjal Khadka, your account 8904 has a balance of Rs. 200.


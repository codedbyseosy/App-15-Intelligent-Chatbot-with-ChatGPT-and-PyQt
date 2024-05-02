from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys
from backend import Chatbot
import threading

class ChatbotWinndow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        self.input_field.returnPressed.connect(self.send_message) # allow message to be sent to 
                                                                  # chat area when user presses the enter key

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show() # used when not using a setCentralWidget


    def send_message(self): # method that gets the user's message
        user_input = self.input_field.text().strip() # get prompt from the user input
        self.chat_area.append(f"Me:{user_input}") # display prompt from user input in the chat area
        self.input_field.clear() # clear the field after sending prompt

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, )) # allows chat area to display user prompt before response
        thread.start()


    def get_bot_response(self, user_input): # method that gets the response 
        response = self.chatbot.get_response(f"<p style='color:#333333'>Me: {user_input}</p>") # get response from the 'get_response' method
                                                         # from the chatbot class
        self.chat_area.append(f"<p style='color:#333333; background-color: #E9E9E9'>Bot: {response}</p>") # display response in the chat area



app = QApplication(sys.argv) # instantiate the class the represent the actual application
main_window = ChatbotWinndow() # instantiate the main window
sys.exit(app.exec())
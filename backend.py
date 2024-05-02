import openai

class Chatbot():
    def __init__(self):
        openai.api_key = "sk-proj-1XBW28seV9JEiBTQAJ51T3BlbkFJbRSyeJx2uyMcMHiSVTbW"

#pip install openai==0.28
    def get_response(self, user_input):
        response = openai.completions.create(
            model = "gpt-3.5-turbo-instruct",
            prompt = user_input,
            max_tokens = 3000,
            temperature = 0.5
        ).choices[0].text
        return response
    
if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)
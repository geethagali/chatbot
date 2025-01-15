import google.generativeai as ai

#API_KEY
API_KEY=""
ai.configure(api_key=API_KEY)
model=ai.GenerativeModel("gemini-pro")
chat=model.start_chat()

while True:
    message=input('you:')
    if message.lower()=='bye':
        print('chatbot: Goddbye!')
        break
    response=chat.send_message(message)
    print('chatbot:',response.text)

import openai

openai.api_key = "[Your openai API key]"

def chatgpt(prompt):
    responce = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return responce.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in  ["exit","bye","quit"]:
            print("Goodbye! Have a greate day.")
            break

        responce = chatgpt(user_input)
        print("Chat Bot: ", responce)

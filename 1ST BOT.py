from openai import OpenAI

# ✅ Replace this with your Groq API key from https://console.groq.com/keys
client = OpenAI(
    api_key="your_groq_api_key_here",
    base_url="https://api.groq.com/openai/v1"
)

print("🎓 Advanced College Life Assistant Bot (LLaMA 3 - Groq)")
print("Ask me anything about college life (type 'bye' to exit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye! Stay focused and all the best! 👋")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert College Life Assistant bot. "
                    "Your job is to help students with questions related to college life: "
                    "admissions, timetables, exam tips, mental health, motivation, assignments, and hostel life. "
                    "Answer in a friendly, helpful, and clear way. Don't go off-topic."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("Bot:", response.choices[0].message.content.strip())

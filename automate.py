from groq import Groq

# Manually set the API key
api_key = "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"  # Make sure the key is enclosed with double quotes

client = Groq(
    api_key=api_key,
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)

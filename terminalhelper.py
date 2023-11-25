import credentials
import openai

# Prompt the user
question = input("Which terminal command would you like to know? \n")

# Refer to credentials.py.template for
openai.organization = credentials.organization
openai.api_key = credentials.OPENAI_API_KEY

# Customize the response to be concise and train it for command-line responses
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an AI that assists on the command line. Your answers should be as concise as possible."},
        {"role": "user", "content": "How do copy and paste in Linux?"},
        {"role": "system", "content": "cp"},
        {"role": "user", "content": "What is the value of pi?"},
        {"role": "system", "content": "3.14 (rounded to two decimal places)"},
        {"role": "user", "content": f"'{question}'"},
    ],
    # Keep the answer as accurate as possible
    temperature=1,
)

# Display the first answer given by OpenAI in the terminal
print(response['choices'][0]['message']['content'])
print("This command is provided by an AI. Use with caution.")

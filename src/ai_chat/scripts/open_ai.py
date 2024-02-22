import os

from openai import AzureOpenAI

ai_client = AzureOpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    api_version="2023-07-01-preview",
    azure_endpoint="https://aaimbostdev8269258341.openai.azure.com",
)


def respond(input):
    completion = ai_client.chat.completions.create(
        model="gpt-4", messages=[{"role": "user", "content": f"{input}"}]
    )

    return completion.choices[0].message.content



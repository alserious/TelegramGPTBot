import openai

from telegramgpt.config import OPENAI_API_KEY


def send_message_to_openai(message: str) -> str:

    openai.api_key = OPENAI_API_KEY

    response = openai.Completion.create(
        model="text-davinci-003", prompt=message, temperature=0, max_tokens=7
    )

    return response




# @dp.message_handler()
# async def gpt(message: types.Message):
#     response = openai.Completion.create(
#         model="text-davinci-003", # text-davinci-003 text-ada-001 -> select model to use 
#         prompt=message.text,
#         temperature=0.5,
#         max_tokens=100,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.0,
#     )
#     await message.reply(response.choices[0].text)
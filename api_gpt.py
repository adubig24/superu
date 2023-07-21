import openai

class API_GPT:

    __API_Key="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"

    @classmethod
    def demande_GPT(cls, query):

        openai.api_key=cls.__API_Key
        completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": query}], max_tokens=1000)

        return completion['choices'][0]['message']['content']
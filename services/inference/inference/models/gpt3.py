import logging
import os

from openai import OpenAI

client = OpenAI(api_key=open_api_key)

# Create a logger
logger = logging.getLogger(__name__)

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
)


class GPT3:
    def __init__(self, open_api_key: str = OPENAI_API_KEY):
        self.api_key = open_api_key
        

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """
        Generates a completion from the GPT-3 model
        :param prompt: The text used to prompt the model
        :param max_tokens: Maximum number of tokens in the completion
        :return: The completion generated by the GPT-3 model
        """
        try:
            logger.info("Generating")
            response = client.completions.create(engine="text-davinci-003",  # gpt-4-0613 # Specify the GPT-3 engine to use
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0)
            return response.choices[0].text
        except Exception as e:
            logger.error(f"An error occurred during GPT-3 completion: {e}")
            return None

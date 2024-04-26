import logging
import os

from transformers import RobertaTokenizer, T5ForConditionalGeneration

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


"""
Generate from text using the CodeT5 model
:param prompt: Input text to generate  from
:param max_length: Maximum length of the generated text
:param num_return_sequences: Number of text sequences to return
:return: Generated text
"""


# TODO this seemm to return nonsense output - maybe that's just a bad test prompt?
def generate(
    prompt,
    max_length: int = 1024,
    num_return_sequences: int = 1,
) -> str:

    try:
        model_name = "Salesforce/codet5-base"
        tokenizer = RobertaTokenizer.from_pretrained(model_name)
        model = T5ForConditionalGeneration.from_pretrained(model_name)
        logger.info(f"Model {model_name} loaded.")

        logger.info("Generating")
        input_ids = tokenizer.encode(prompt, return_tensors="pt")
        outputs = model.generate(
            input_ids,
            max_length=max_length,
            num_return_sequences=num_return_sequences,
        )
        response = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
        return response[0]
    except Exception as e:
        logger.error(f"An error occurred during codet5 generation: {e}")

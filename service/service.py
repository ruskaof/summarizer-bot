import requests
import json

from . import OPENAI_API_LINK, OPENAI_API_SECRET, SBER_API_LINK


def summarize(text: str, api="sber") -> str:
    """Summarizes the given text

    Args:
        text (str): the text to be summarized
        api (str, optional): Should be "openai" or "sber" depending on the api.
        Defaults to "sber".

    Returns:
        str: Summarized text
    """

    if (api == "sber"):
        return _make_sberapi_summarize_call(text)
    elif (api == "openai"):
        return _make_openai_summarize_call(text)
    else:
        raise ValueError("api arg must be 'openai' or 'sber'")


def _make_sberapi_summarize_call(text: str) -> str:
    """Makes a request to the basic sber api

    Args:
        text (str): the text to be summarized

    Returns:
        str: Summarized text
    """
    response = requests.post(SBER_API_LINK + "/predict", json={
        "instances": [
            {
                "text": text,
                "num_beams": 50,  # ???
                "num_return_sequences": 15,  # ???
                # Penalty for the length of the summarizer result (a value in (0, 1))
                "length_penalty": 0.9999
            }
        ]
    })

    response.raise_for_status()  # Raise an exception for any HTTP errors

    response_obj = json.loads(response.text)

    return response_obj['prediction_best']['bertscore']


def _make_openai_summarize_call(text: str, prompt="Summarize the text below (try to be as short as possible but do not miss anything important):\n") -> str:
    """
    Makes a request to the the 'gpt-3.5-turbo' version of chat gpt asking
    to summarize the provided text.

    Args:
        text (str): the text to be summarized
        prompt (str, optional): The prompt that will.
            Defaults to "Summarize the text below (try to be as short as possible but do not miss anything important):\n".

    Returns:
        str: Summarized text
    """

    response = requests.post(OPENAI_API_LINK, headers={
        "Content-Type": "application/json",
        'Authorization': 'Bearer ' + OPENAI_API_SECRET
    }, json={
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt + " " + text}]
    })

    response.raise_for_status()  # Raise an exception for any HTTP

    response_obj = json.loads(response.text)

    return response_obj["choices"][0]["message"]["content"]

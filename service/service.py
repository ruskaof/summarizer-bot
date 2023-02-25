import requests
import json
import service.constants as constants


def summarize(text: str) -> str:
    return _make_sberapi_summarize_call(text)


def _make_sberapi_summarize_call(text: str) -> str:
    response = requests.post(constants.SBER_API_LINK + "/predict", json={
        "instances": [
            {
                "text": text,
                "num_beams": 15,  # ???
                "num_return_sequences": 15,  # ???
                "length_penalty": 0.5  # Penalty for the length of the summarizer result (a value in (0, 1))
            }
        ]
    })
    print(response.text)

    response.raise_for_status()  # Raise an exception for any HTTP errors

    response_obj = json.loads(response.text)

    return response_obj['prediction_best']['bertscore']

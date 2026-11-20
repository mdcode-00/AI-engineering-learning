MODEL_PRICES = {
  "Model A": {
    "input": 2.00,
    "output": 8.00
  },
  "Model B": {
      "input": 0.50,
      "output": 2.00
    },
}


def calculater_cost(
    input_tokens: int,
    output_tokens: int,
    model: str
) -> float:
  prices = MODEL_PRICES[model]

  input_cost= (
    input_tokens / 1_000_000
  ) * prices["input"]

  output_tokens = (
    output_tokens / 1_000_000
  ) * prices["output"]

  return input_cost + output_tokens

def calculate_multiple_request(
    cost: float
) -> dict:

  return {
    "100_requests": cost * 100,
    "1000_requests": cost * 1000,
    "10000_requests": cost * 10000
  }
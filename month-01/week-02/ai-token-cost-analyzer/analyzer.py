import tiktoken

def count_characters(text: str) -> int:
  return len(text)

def count_words(text:str) -> int:
  return len(text.split())


def estimate_tokens(text:str) -> int:
  try: 
    encoding = tiktoken.get_encoding("cl100k_base")
    return len(encoding.encode(text))
  except Exception:
    # Fallback estimate
    return len(text) // 4


def analyze_text(text: str) -> dict:
  return {
    "characters": count_characters(text),
        "words": count_words(text),
        "input_tokens": estimate_tokens(text)
  }

def check_prompt_length(token:int) -> str:
  if token > 8000:
    return "WARNING: Your prompt is unusually long!"
  elif token > 4000:
    return "Notice: Your prompt is quite long."

  return "Prompt length is acceptable."

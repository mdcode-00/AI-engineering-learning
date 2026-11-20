import json

def save_analysis(data: dict) -> None:
  try:
    with open(
      "analysis.json",
      "w",
      encoding="utf-8"
    ) as file:
      json.dump(
        data,
        file,
        indent=4
      )

      print("\nAnlysis saved successfully")

  except OSError as error:
    print(f"Error saving file: {error}")
    
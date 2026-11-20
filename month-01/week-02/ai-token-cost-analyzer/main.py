from analyzer import analyze_text, check_prompt_length
from pricing import (
  MODEL_PRICES,
  calculate_multiple_request,
  calculater_cost
)
from storage import save_analysis


def get_multiline_input() -> str:
  print("\n Enter your prompt.")
  print("Type End on a new line to finish: \n")

  lines = []

  while True:
    line = input()

    if line.strip() == "END":
      break

    lines.append(line)

  return "\n".join(lines)

def get_output_tokens() -> int:
  while True:
    try:
      tokens = int(
        input("Expected out tokens:")
      )

      if tokens < 0:
         print("Please enter a non-negative number.")
         continue

      return tokens
    except ValueError:
      print("Invalid input. Enter a whole number.")

def display_result(
    analysis: dict,
    output_tokens:int
) -> dict:
  input_tokens = analysis["input_tokens"]

  total_tokens = input_tokens + output_tokens

  print("\n========== ANALYSIS RESULTS ==========")

  print("Characters:", analysis["characters"])
  print("Words:", analysis["words"])
  print("Estimated input tokens:", input_tokens)
  print("Expected output tokens:", output_tokens)
  print("Total estimated tokens:", total_tokens)

  warning = check_prompt_length(input_tokens)

  print("\nPrompt Status:", warning)

  results = {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "models": {}
    }

  print("\n========== API COST COMPARISON ==========")

  for model in MODEL_PRICES:

        cost = calculater_cost(
            input_tokens,
            output_tokens,
            model
        )

        multiple_costs = calculate_multiple_request(cost)

        print(f"\n{model}: ${cost:.8f}")

        for request, amount in multiple_costs.items():
            print(f"{request}: ${amount:.4f}")

        results["models"][model] = {
            "cost_per_request": cost,
            "multiple_requests": multiple_costs
        }

  return results



def main() -> None:
    print("=" * 40)
    print("       AI TOKEN & COST ANALYZER")
    print("=" * 40)

    text = get_multiline_input()

    if not text.strip():
        print("Error: Prompt cannot be empty.")
        return

    output_tokens = get_output_tokens()

    analysis = analyze_text(text)

    results = display_result(
        analysis,
        output_tokens
    )

    final_data = {
        "prompt": text,
        "analysis": analysis,
        "results": results
    }

    choice = input(
        "\nSave analysis to JSON? (yes/no): "
    ).strip().lower()

    if choice in ("yes", "y"):
        save_analysis(final_data)

    print("\nThank you for using AI Token & Cost Analyzer!")


if __name__ == "__main__":
    main()
from decision_tree import DecisionTree
from guardrails import validate_input

def run_agent():
print("\n Daily Reflection AI Agent")
print("=" * 40)

```
try:
    # Take user input
    mood = input(
        "Enter your mood (happy/sad/stressed): "
    ).strip().lower()

    reason = input(
        "Enter reason (achievement/social/failure/personal/work/time): "
    ).strip().lower()

    # Guardrail validation
    is_valid, message = validate_input(mood, reason)

    if not is_valid:
        print(f"\n Error: {message}")
        return

    # Decision tree evaluation
    tree = DecisionTree()
    result = tree.evaluate(mood, reason)

    # Output section
    print("\n Reflection")
    print("-" * 40)
    print(result["reflection"])

    print("\n Suggested Action")
    print("-" * 40)
    print(result["action"])

    print("\n Thank you for using Reflection AI Agent!")

except KeyboardInterrupt:
    print("\n\n Session cancelled by user.")

except Exception as e:
    print(f"\n Unexpected error: {e}")
```

if **name** == "**main**":
run_agent()

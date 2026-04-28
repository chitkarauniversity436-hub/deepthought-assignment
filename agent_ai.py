from decision_tree import DecisionTree
from guardrails import validate_input

def run_agent():
    print(" Daily reflection AI Agent")
    print("--------------------------------")

    mood = input("Enter your mood (happy/sad/stressed): ")
    reason = input("Enter reason (achievement/social/failure/personal/work/time): ")

    # Guardrail check
    is_valid, message = validate_input(mood, reason)

    if not is_valid:
        print(" Error:", message)
        return

    tree = DecisionTree()
    result = tree.evaluate(mood, reason)

    print("\n Reflection:")
    print(result["reflection"])

    print("\n Suggested Action:")
    print(result["action"])


if __name__ == "__main__":
    run_agent()
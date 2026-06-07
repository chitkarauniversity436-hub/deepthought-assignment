from datetime import datetime
from decision_tree import DecisionTree
from guardrails import validate_input


def display_header():
    print("\n Daily Reflection AI Agent")
    print("-" * 40)
    print(f"Date & Time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("-" * 40)


def run_agent():
    history = []

    while True:
        display_header()

        name = input("Enter your name: ").strip()
        mood = input("Enter your mood (happy/sad/stressed): ").strip().lower()
        reason = input(
            "Enter reason (achievement/social/failure/personal/work/time): "
        ).strip().lower()

        # Guardrail validation
        is_valid, message = validate_input(mood, reason)

        if not is_valid:
            print(" Error:", message)
            continue

        tree = DecisionTree()
        result = tree.evaluate(mood, reason)

        print(f"\n Hello {name}!")
        print("\n Reflection:")
        print(result["reflection"])

        print("\n Suggested Action:")
        print(result["action"])

        # Store session history
        history.append(
            {
                "name": name,
                "mood": mood,
                "reason": reason,
                "reflection": result["reflection"],
                "action": result["action"],
            }
        )

        choice = input("\nWould you like another reflection? (yes/no): ").lower()

        if choice != "yes":
            break

    # Display session summary
    print("\n Session Summary")
    print("-" * 40)

    for idx, entry in enumerate(history, start=1):
        print(f"\nReflection #{idx}")
        print(f"User      : {entry['name']}")
        print(f"Mood      : {entry['mood']}")
        print(f"Reason    : {entry['reason']}")
        print(f"Reflection: {entry['reflection']}")
        print(f"Action    : {entry['action']}")

    print("\nThank you for using Daily Reflection AI Agent!")


if __name__ == "__main__":
    run_agent()

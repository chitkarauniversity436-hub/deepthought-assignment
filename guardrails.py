ALLOWED_MOODS = ["happy", "sad", "stressed"]
ALLOWED_REASONS = [
    "achievement", "social",
    "failure", "personal",
    "work", "time"
]

def validate_input(mood, reason):
    mood = mood.lower()
    reason = reason.lower()

    if mood not in ALLOWED_MOODS:
        return False, "Invalid mood. Choose from: happy, sad, stressed"

    if reason not in ALLOWED_REASONS:
        return False, "Invalid reason. Use predefined categories only"

    return True, "Valid input"
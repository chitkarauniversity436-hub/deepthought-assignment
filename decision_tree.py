class DecisionTree:

    def evaluate(self, mood, reason):
        mood = mood.lower()
        reason = reason.lower()

        # Deterministic logic
        if mood == "happy":
            return self.handle_happy(reason)

        elif mood == "sad":
            return self.handle_sad(reason)

        elif mood == "stressed":
            return self.handle_stressed(reason)

        else:
            return {
                "status": "error",
                "message": "Invalid mood input. Allowed: happy, sad, stressed"
            }

    def handle_happy(self, reason):
        if reason == "achievement":
            return {
                "reflection": "Celebrate your success.",
                "action": "Write what worked well and repeat it."
            }
        elif reason == "social":
            return {
                "reflection": "Value your relationships.",
                "action": "Express gratitude to the person."
            }
        else:
            return self.default_response()

    def handle_sad(self, reason):
        if reason == "failure":
            return {
                "reflection": "Failure is feedback.",
                "action": "Write 1 improvement for next time."
            }
        elif reason == "personal":
            return {
                "reflection": "Acknowledge your emotions.",
                "action": "Journal your thoughts for 10 minutes."
            }
        else:
            return self.default_response()

    def handle_stressed(self, reason):
        if reason == "work":
            return {
                "reflection": "You may be overloaded.",
                "action": "Break tasks into smaller parts."
            }
        elif reason == "time":
            return {
                "reflection": "Time pressure detected.",
                "action": "Prioritize top 3 tasks only."
            }
        else:
            return self.default_response()

    def default_response(self):
        return {
            "reflection": "Unable to determine exact state.",
            "action": "Take a short break and reassess."
        }
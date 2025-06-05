# ethics.py

class EthicsEngine:
    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.rules = self._load_profile(profile_name)

    def _load_profile(self, profile_name):
        # Basic ruleset; can be expanded or replaced by YAML or JSON config
        default_rules = {
            "banned_keywords": [
                "exploit", "surveillance", "manipulation", "oppression",
                "deception", "censorship", "unethical research"
            ],
            "required_values": [
                "transparency", "liberation", "open access", "ethical alignment"
            ]
        }
        return default_rules

    def validate(self, text):
        lowered = text.lower()
        for banned in self.rules["banned_keywords"]:
            if banned in lowered:
                return False
        return True

    def log_violation(self, text):
        print(f"[EthicsEngine-{self.profile_name}] Ethics violation: {text}")

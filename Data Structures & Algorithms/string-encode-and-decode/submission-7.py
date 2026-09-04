class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_message = ""
        if len(strs) == 0:
            return "empty"
        for index, word in enumerate(strs):
            if index < len(strs) - 1:
                encoded_message += word + "Ω"
            else:
                encoded_message += word
        return encoded_message

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        return s.split("Ω")
# Ω
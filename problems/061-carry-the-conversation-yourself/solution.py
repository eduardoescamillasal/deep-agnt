class Chat:
    """A conversation with a model."""

    def __init__(self, llm, system):
        self.llm = llm
        self.system = system
        self.messages = []

    def send(self, text):
        """Send the user's message. Return the model's reply."""
        usr_message = {"role": "user", "content": text}
        historic_messages =[*self.messages, usr_message]
        response = self.llm.messages.create(
            system=self.system,
            messages=historic_messages,
            max_tokens=300,
        )
        reply = response.text
        self.messages = [
            *historic_messages,
            {"role": "assistant", "content": reply}
        ]
        return reply

def _render_chat(messages, add_generation_prompt):
    if getattr(tokenizer, "chat_template", None):
        return tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=add_generation_prompt
        )
    return "\n".join(f"{m['role']}: {m['content']}" for m in messages)

def format_chat(messages):
    """The prompt string, ready for the assistant to continue."""
    return _render_chat(messages, add_generation_prompt=True)


def format_for_training(messages):
    """The full conversation including the assistant's reply."""
    return _render_chat(messages, add_generation_prompt=False)

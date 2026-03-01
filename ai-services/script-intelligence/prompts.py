def get_script_prompt(topic: str, style: str) -> str:
    # TODO: Implement prompt generation logic
    return f"Write a {style} script about {topic}."


# Reference Implementation
"""
def get_script_prompt(topic: str, style: str) -> str:
    if style == "informative":
        return f"""You are a helpful assistant that writes informative video scripts.

        Topic: {topic}

        Please write a clear and concise script on the given topic. The script should be easy to understand and engaging for the viewer.
        """
    elif style == "horror":
        return f"""You are a horror story writer. Write a scary story on the given topic.

        Topic: {topic}

        The story should be suspenseful and have a terrifying ending.
        """
    else:
        return f"Write a script about {topic}."
"""

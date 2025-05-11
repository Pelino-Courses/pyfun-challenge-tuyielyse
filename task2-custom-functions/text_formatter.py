def format_text(text: str, prefix: str = "", suffix: str = "" , capitalize: bool = False, max_length: int = None):

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    if not isinstance(prefix, str):
        raise TypeError("prefix must be a string")
    
    if not isinstance(suffix, str):
       raise TypeError("suffix must be a string")
    
    if not isinstance(capitalize, bool):
       raise TypeError("capitalize must be a boolean")
    
    if max_length is not None:
       if not isinstance(max_length, int) or max_length<=0:
        raise ValueError("Maximum length must be a positive integer")
    result = f"{prefix}{text}{suffix}"

    if capitalize:
        result = text.capitalize()

    if max_length is not None :
        result = result[:max_length]
    return result

print(format_text("understanding",prefix="[",suffix="]", capitalize=True))
print(format_text("education is very useful", max_length=13))

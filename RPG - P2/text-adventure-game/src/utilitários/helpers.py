def validate_input(prompt, valid_options):
    choice = input(prompt).strip().lower()
    while choice not in valid_options:
        print(f"Opção inválida. Por favor, escolha entre: {"".join(valid_options)}.")
        choice = input(prompt).strip().lower()
    return choice

def format_text(text):
    return text.strip().capitalize()

def display_message(message):
    print("\n" + message + "\n")
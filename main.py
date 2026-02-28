from assistant.speech import take_command
from assistant.speak import speak
from assistant.commands import execute_command

def run_assistant():
    speak("Athena is ready.")

    while True:
        command = take_command()

        if command:
            if "athena" in command:
                execute_command(command)

if __name__ == "__main__":
    run_assistant()
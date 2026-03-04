from assistant.speech import take_command
from assistant.speak import speak
from assistant.commands import execute_command
from assistant.config import WAKE_WORD

def run_assistant():

    speak("Athena is ready")

    while True:

        command = take_command()

        if command:

            if WAKE_WORD in command:

                status = execute_command(command)

                if status == False:
                    break


if __name__ == "__main__":
    run_assistant()
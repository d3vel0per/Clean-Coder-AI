import itertools
import sys
import time
import random
from termcolor import colored
from time import sleep
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.live import Live
import threading
import os
current = os.path.dirname(os.path.realpath(__file__))
grandparent = os.path.dirname(os.path.dirname(current))
sys.path.append(grandparent)
from src.utilities.print_formatters import print_formatted

def print_ascii_logo():
    with open("assets/ascii-art.txt", "r") as f:
        logo = f.read()
    with open("assets/Clean_Coder_writing.txt", "r") as f:
        writing = f.read()
    print(colored(logo, color="yellow"))
    print(colored(writing, color="white"))


def loading_animation(message="I'm thinking...", color="cyan"):
    frames = [
        "🌘🌑🌑🌑🌑🌑🌑🌑",
        "🌗🌘🌑🌑🌑🌑🌑🌑",
        "🌖🌗🌘🌑🌑🌑🌑🌑",
        "🌕🌖🌗🌘🌑🌑🌑🌑",
        "🌕🌕🌖🌗🌘🌑🌑🌑",
        "🌕🌕🌕🌖🌗🌘🌑🌑",
        "🌕🌕🌕🌕🌖🌗🌘🌑",
        "🌕🌕🌕🌕🌕🌖🌗🌘",
        "🌕🌕🌕🌕🌕🌕🌖🌗",
        "🌕🌕🌕🌕🌕🌕🌕🌖",
        "🌕🌕🌕🌕🌕🌕🌕🌕",
        "🌔🌕🌕🌕🌕🌕🌕🌕",
        "🌓🌔🌕🌕🌕🌕🌕🌕",
        "🌒🌓🌔🌕🌕🌕🌕🌕",
        "🌑🌒🌓🌔🌕🌕🌕🌕",
        "🌑🌑🌒🌓🌔🌕🌕🌕",
        "🌑🌑🌑🌒🌓🌔🌕🌕",
        "🌑🌑🌑🌑🌒🌓🌔🌕",
        "🌑🌑🌑🌑🌑🌒🌓🌔",
        "🌑🌑🌑🌑🌑🌑🌒🌓",
        "🌑🌑🌑🌑🌑🌑🌑🌒",
    ]
    print_formatted(message, color=color, end=' ')  # Print the message with color and stay on the same line
    sys.stdout.flush()
    print('\033[?25l', end='')  # Hide cursor
    try:
        for frame in itertools.cycle(frames):
            print_formatted(frame, color=color,
                            end='\r' + message + ' ')  # Print the frame on the same line after the message
            time.sleep(0.07)  # Adjust the sleep time for better animation speed
            if not loading_animation.is_running:
                break
    finally:
        print('\033[?25h', end='')  # Show cursor
        sys.stdout.write('\r' + ' ' * (len(message) + len(frames[0]) + 2) + '\r')  # Clear the entire line
        sys.stdout.flush()


loading_animation.is_running = True

def task_completed_animation():
    console = Console()
    width = console.width  # Get console width

    # Adjusted ASCII celebration art to fit console width
    celebration_art = """
   🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟
   
       🎊 TASK COMPLETED! 🎊
       
   🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟 🌟
   """

    # Symbols for animation
    symbols = ["✨", "🎊", "🌟"]

    # Initial celebration panel
    console.clear()
    panel = Panel(
        Text(celebration_art, justify="center"),
        border_style="bright_yellow",
        padding=(1, 2)
    )
    console.print(panel)

    # Calculate how many symbols fit in the width (considering each symbol + more spaces takes about 6 characters)
    symbols_per_line = width // 6  # Increased space between symbols

    # Animated confetti - full width but spaced out
    with Live(console=console, refresh_per_second=15) as live:
        for frame in range(20):
            lines = []
            for _ in range(5):  # 5 lines of confetti
                line = "".join(
                    f"{random.choice(symbols)}    "  # Added more spaces between symbols
                    for _ in range(symbols_per_line)
                )
                lines.append(line)
            
            live.update(Text("\n".join(lines), justify="center"))
            sleep(0.05)  # Fast animation

    # Final message
    final_panel = Panel(
        Text("✨ Great job! Moving on to the next task... ✨",
             justify="center"),
        border_style="green"
    )
    console.print(final_panel)


class LoadingAnimation:
    def __init__(self, message="I'm thinking...", color="cyan", interval=0.07):
        self.message = message
        self.color = color
        self.interval = interval

        # Define your frames once in the constructor
        self.frames = [
            "🌘🌑🌑🌑🌑🌑🌑🌑",
            "🌗🌘🌑🌑🌑🌑🌑🌑",
            "🌖🌗🌘🌑🌑🌑🌑🌑",
            "🌕🌖🌗🌘🌑🌑🌑🌑",
            "🌕🌕🌖🌗🌘🌑🌑🌑",
            "🌕🌕🌕🌖🌗🌘🌑🌑",
            "🌕🌕🌕🌕🌖🌗🌘🌑",
            "🌕🌕🌕🌕🌕🌖🌗🌘",
            "🌕🌕🌕🌕🌕🌕🌖🌗",
            "🌕🌕🌕🌕🌕🌕🌕🌖",
            "🌕🌕🌕🌕🌕🌕🌕🌕",
            "🌔🌕🌕🌕🌕🌕🌕🌕",
            "🌓🌔🌕🌕🌕🌕🌕🌕",
            "🌒🌓🌔🌕🌕🌕🌕🌕",
            "🌑🌒🌓🌔🌕🌕🌕🌕",
            "🌑🌑🌒🌓🌔🌕🌕🌕",
            "🌑🌑🌑🌒🌓🌔🌕🌕",
            "🌑🌑🌑🌑🌒🌓🌔🌕",
            "🌑🌑🌑🌑🌑🌒🌓🌔",
            "🌑🌑🌑🌑🌑🌑🌒🌓",
            "🌑🌑🌑🌑🌑🌑🌑🌒",
        ]

        # Use an Event to signal the animation thread to stop
        self._stop_event = threading.Event()
        self._thread = None

    def _animate(self):
        """
        Private method that performs the animation loop.
        Runs on a separate thread when start() is called.
        """
        # Hide cursor
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

        # Print initial message once
        print_formatted(self.message, color=self.color, end=" ")
        sys.stdout.flush()

        try:
            for frame in itertools.cycle(self.frames):
                if self._stop_event.is_set():
                    break
                # Print the current frame on the same line after the message
                print_formatted(frame, color=self.color, end="\r" + self.message + " ")
                time.sleep(self.interval)
        finally:
            # Show cursor again
            sys.stdout.write("\033[?25h")
            sys.stdout.flush()
            # Clear the entire line
            sys.stdout.write('\r' + ' ' * (len(self.message) + len(self.frames[0]) + 2) + '\r')
            sys.stdout.flush()

    def start(self):
        """
        Starts the animation if it is not already running.
        """
        if self._thread is not None and self._thread.is_alive():
            # Already running
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._animate)
        self._thread.daemon = True
        self._thread.start()

    def stop(self):
        """
        Signals the animation thread to stop and waits for it to finish.
        """
        if self._thread is None:
            return
        self._stop_event.set()
        self._thread.join()
        self._thread = None
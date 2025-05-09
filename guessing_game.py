# guessing_game.py

class GuessingBot:
    def __init__(self, sock):
        self.sock = sock

    def choose_difficulty(self, choice):
        self.sock.sendall(f"{choice}\n".encode())
        if choice == '1':
            return 1, 10
        elif choice == '2':
            return 1, 50
        else:
            return 1, 100

    def binary_guess(self, low, high):
        while low <= high:
            guess = (low + high) // 2
            print(f"Bot guesses: {guess}")
            self.sock.sendall(f"{guess}\n".encode())

            response = self.sock.recv(1024).decode().strip()
            print(response)

            if "CORRECT!" in response:
                return guess
            elif "Lower" in response:
                high = guess - 1
            elif "Higher" in response:
                low = guess + 1
            else:
                raise ValueError("Unexpected response from server.")
        return None

import unittest
from unittest.mock import MagicMock
from guessing_game import GuessingBot

class TestGuessingBot(unittest.TestCase):

    def test_choose_difficulty_easy(self):
        mock_socket = MagicMock()
        bot = GuessingBot(mock_socket)
        result = bot.choose_difficulty("1")
        self.assertEqual(result, (1, 10))
        mock_socket.sendall.assert_called_with(b"1\n")

    def test_choose_difficulty_medium(self):
        mock_socket = MagicMock()
        bot = GuessingBot(mock_socket)
        result = bot.choose_difficulty("2")
        self.assertEqual(result, (1, 50))
        mock_socket.sendall.assert_called_with(b"2\n")


    def test_choose_difficulty_default_hard(self):
        mock_socket = MagicMock()
        bot = GuessingBot(mock_socket)
        result = bot.choose_difficulty("99")
        self.assertEqual(result, (1, 100))
        mock_socket.sendall.assert_called_with(b"99\n")
    
    def test_binary_guess_correct_first_try(self):
        mock_socket = MagicMock()
        mock_socket.recv.return_value = b"CORRECT!"
        bot = GuessingBot(mock_socket)
        self.assertEqual(bot.binary_guess(1, 10), 5)

    def test_binary_guess_multiple_steps(self):
        mock_socket = MagicMock()
        mock_socket.recv.side_effect = [
            b"Higher", b"Lower", b"Higher", b"CORRECT!"
        ]
        bot = GuessingBot(mock_socket)
        self.assertEqual(bot.binary_guess(1, 10), 7)

    def test_binary_guess_all_lower(self):
        # Simulate: guess 5 -> Lower, guess 3 -> Lower, guess 2 -> Lower, guess 1 -> CORRECT!
        mock_socket = MagicMock()
        mock_socket.recv.side_effect = [
            b"Lower", b"Lower", b"Lower", b"CORRECT!"
        ]
    def test_binary_guess_all_higher(self):
        # Simulate: guess 5 -> Higher, guess 8 -> Higher, guess 9 -> Higher, guess 10 -> CORRECT!
        mock_socket = MagicMock()
        mock_socket.recv.side_effect = [
            b"Higher", b"Higher", b"Higher", b"CORRECT!"
        ]
        bot = GuessingBot(mock_socket)
        self.assertEqual(bot.binary_guess(1, 10), 10)

if __name__ == '__main__':
    unittest.main()
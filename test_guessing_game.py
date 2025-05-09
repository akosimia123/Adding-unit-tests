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

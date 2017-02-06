from unittest import TestCase

class TestMyGame(TestCase):
    def test_setup(self):
        from main import MyGame
        game = MyGame(100, 100, 'Test')
        assert game.is_stopped is True

    def test_not_stopped(self):
        from main import MyGame
        game = MyGame(100, 100, 'Test')
        game.is_stopped = False
        game.on_draw()
        assert game.is_stopped
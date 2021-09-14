class GameStats():
    """Track statistics for Catch the eggs."""

    def __init__(self, game_settings):
        """Initialize statistics."""
        self.game_settings = game_settings
        self.reset_stats()

        # Start game in an active state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.score = 0






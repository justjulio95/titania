class GameStats():
    """Track statistics for Titania."""

    def __init__(self, tt_settings):
        """Initialize statistics."""
        self.tt_settings = tt_settings
        self.reset_stats()

        # Start game in an inactive state. 
        self.game_active = False

        # High score should never be reset
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.tt_settings.ships_left
        self.score = 0
        self.level = 1
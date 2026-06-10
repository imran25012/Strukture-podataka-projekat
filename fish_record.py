from datetime import datetime


class FishRecord:
    """
    Predstavlja jedan događaj u lancu snabdijevanja ribom.
    """

    def __init__(self, fish_id, location, status):
        self.fish_id = fish_id
        self.location = location
        self.status = status
        self.timestamp = datetime.now()

    def __str__(self):
        return (
            f"Fish ID: {self.fish_id}\n"
            f"Lokacija: {self.location}\n"
            f"Status: {self.status}\n"
            f"Vrijeme: {self.timestamp}"
        )

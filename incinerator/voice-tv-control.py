class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.current = channels[0]

    def first_channel(self) -> str:
        self.current = self.channels[0]
        return self.current

    def last_channel(self) -> str:
        self.current = self.channels[-1]
        return self.current

    def turn_channel(self, channel_n0: int) -> str:
        self.current = self.channels[channel_n0-1]
        return self.current

    def previous_channel(self) -> str:
        current_idx = self.channels.index(self.current)
        try:
            self.current = self.channels[current_idx - 1]
            return self.current
        except IndexError:
            return self.last_channel()

    def next_channel(self) -> str:
        current_idx = self.channels.index(self.current)
        try:
            self.current = self.channels[current_idx + 1]
            return self.current
        except IndexError:
            return self.first_channel()

    def current_channel(self) -> str:
        return self.current

    def is_exist(self, channel_identifier) -> str:
        Y = "Yes"
        N = "No"

        if isinstance(channel_identifier, int):
            try:
                self.channels[channel_identifier]
                return Y
            except IndexError:
                return N
        elif isinstance(channel_identifier, str):
            return Y if channel_identifier in self.channels else N
        else:
            return N


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
    print("Coding complete? Let's try tests!")

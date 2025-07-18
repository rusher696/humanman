import random
class organs:
    def heart(bpm=72, blood_per_beat=70, minutes=1):
        """
        Calculates blood from heart beating for t seconds.
        Uses formula total = ta, where t = time, a = amount
        """
        try:
            beats = bpm * minutes
            blood = beats * blood_per_beat
            return {
            "beats": beats,
            "blood_per_beat": blood_per_beat,
            "total_blood": blood,
            "error": None
            }
        except Exception as ez:
            return {
            "beats": None,
            "blood_per_beat": None,
            "total_blood": None,
            "error": str(ez)
            }
    def breathe(rate=16, time=1, tidal_vol=500):
        """
        Calculates oxygen and CO2 from breathing for t seconds.
        Uses average oxygen to CO2 conversion ratio. (1:0.8)
        """
        try:
            breaths = rate * time
            oxygen_ml = breaths * tidal_vol
            return {
            "breaths": breaths,
            "tidal_vol": tidal_vol,
            "time": time,
            "oxygen_used": oxygen_ml,
            "co2": oxygen_ml * 0.8,
            "error": None
            }
        except Exception as e:
            return {
            "breaths": None,
            "tidal_vol": None,
            "time": time,
            "oxygen_used": None,
            "co2": None,
            "error": str(e)
            }
    def think(thought="Why is a boxing ring called a boxing ring if it isn't a ring?", tired=False):
        """
        Estimates neuron usage based on thought.
        Example:
            Tired: False
            Thought: Why are things called weird names?
            Neurons Used: 51_000_000-85_000_000
            """
        try:
            return {
            "thought": thought,
            "neurons_used": len(str(thought)) * random.randint(500_000, 1_000_000) if tired else len(thought) * random.randint(1_500_000, 2_500_000),
            "error": None
            }
        except Exception as e:
            return {
            "thought": None,
            "neurons_used": None,
            "error": str(e)
            }
    class bladder:
        def __init__(self):
            self.volume = 0
            self.capacity = 600
        def fill(self, amount):
            self.volume += amount
            if self.volume >= self.capacity:
                return {"status": "peed pants", "volume": self.volume, "message": "Maybe go next time?"}
            elif self.volume >= self.capacity - 200:
                return {"status": "urgent", "volume": self.volume, "message": "YOU URGENTLY HAVE TO GO"}
            return {"status": "ok", "volume": self.volume, "message": "You're safe for now..."}
        def release(self):
            if self.volume <= 10:
                return {"status": "DRY", "volume": self.volume}
            released = self.volume
            self.volume = 0         
            return {"status": f"relieved ({released}mL)", "volume": self.volume}        
class Cell:
    def __init__(self, type="human"):
        self.type = type.lower().strip()
        self.organelles = ["nucleus", "mitochondria", "ribosome", "endoplasmic reticulum", "golgi apparatus", "lysosome", "cytoplasm", "membrane"]
        self.has_dna = True
        self.has_membrane = True
        self.energy_stored = 0
    def info(self):
        return {
        "type": self.type,
        "organelles": self.organelles,
        "dna": self.has_dna,
        "membrane": self.has_membrane,
        "energy_stored": self.energy_stored
        }
    def use_glucose(self, mmol=1):
        """
        Simulates celluar respiration.
        1 glucose = ~30 ATP molecules
        1 mmol = 6.022e20 molecules
        """
        try:
            atp = mmol * 30
            self.energy_stored += atp
            return {
            "glucose_used": mmol,
            "atp_gained": atp,
            "total_energy": self.energy_stored,
            "error": None
            }
        except Exception as e:
            return {
            "glucose_used": None,
            "atp_gained": None,
            "total_energy": None,
            "error": str(e)
            }
    def mutate(self):
        try:
            if not "mutated mitochondria" in self.organelles:
                self.organelles.append("mutated mitochondria")
            self.has_dna = False
            return {
            "status": "Mutation occured",
            "organelles": self.organelles,
            "has_dna": self.has_dna,
            "error": None
            }
        except Exception as e:
            return {
            "status": "Mutation failed",
            "organelles": None,
            "has_dna": None,
            "error": str(e)
            }
    def mitosis(self):
        try:
            new_cell = Cell(self.type)
            return new_cell
        except Exception as e:                 
            return None         
    def communicate(self, other=None, shared_energy=0):
        if not isinstance(other, self.__class__):
            return {"status": "Failed", "error": f"Must share with class {type(self)}, not {type(other)}."}
        if shared_energy > 0:
            if shared_energy > self.energy_stored:
                return {"status": "Failed", "error": f"Maximum {self.energy_stored} energy, got {shared_energy}."}
            self.energy_stored -= shared_energy
            other.energy_stored += shared_energy
            return {"status": f"Successfully transfered {shared_energy} energy to the other cell.", "error": None}
        return {"status": "Failed", "error": "Not enough energy"}    
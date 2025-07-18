class nerves:
    def __init__(self):
        self.connected_cells = []
        self.stimuli = []
    def connect_cell(self, cell):
        from humanman import Cell
        if isinstance(cell, Cell):
            self.connected_cells.append(cell)
    def transmit(self, signal="pain", speed="fast", location="hand"):
        delay = 0.02 if speed == "fast" else 0.3
        atp_used = 2 if speed == "fast" else 1
        energy_logs = []
        for cell in self.connected_cells:
            cell.use_glucose(0.05 * atp_used)
            energy_logs.append(cell.info())
        self.stimuli.append((signal, location))
        return {
        "signal": signal,
        "location": location,
        "atp_used_total": len(self.connected_cells) * atp_used,
        "cell_energies": energy_logs,
        "message": f"Signal '{signal}' caused ATP use in {len(self.connected_cells)} cells."
        }           
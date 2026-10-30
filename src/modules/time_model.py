class TimeModel:
    def __init__(self): self.actual, self.stopped, self.history, self.minimum = 0, True, [], None
    def tick(self): self.actual += 1
    def format_time(self, t): return f"{(t // 3600):02d}:{((t // 60) % 60):02d}:{(t % 60):02d}"
    def format_short(self, t): return f"{(t // 3600):02d}:{((t // 60) % 60):02d}:{(t % 60):02d}" if (t // 3600) > 0 else f"{((t // 60) % 60):02d}:{(t % 60):02d}"
    def record_and_reset(self): 
        if self.actual > 0: self.history.append(self.format_time(self.actual)); self.minimum = self.actual if self.minimum is None or self.actual < self.minimum else self.minimum
        self.actual, self.stopped = 0, True
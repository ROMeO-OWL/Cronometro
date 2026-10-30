class TimeModel:
    def __init__(self): self.actual, self.stopped, self.history, self.minimum, self.maximum = 0, True, [], None, None
    def tick(self): self.actual += 1
    def format_time(self, t): return f"{(t // 3600):02d}:{((t // 60) % 60):02d}:{(t % 60):02d}"
    def format_short(self, t): return f"{(t // 3600):02d}:{((t // 60) % 60):02d}:{(t % 60):02d}" if (t // 3600) > 0 else f"{((t // 60) % 60):02d}:{(t % 60):02d}"
    def get_average(self): return int(sum(self.history) / len(self.history)) if self.history else 0
    def record_and_reset(self): 
        if self.actual > 0: 
            self.history.append(self.actual)
            self.minimum = self.actual if self.minimum is None or self.actual < self.minimum else self.minimum
            self.maximum = self.actual if self.maximum is None or self.actual > self.maximum else self.maximum
        self.actual, self.stopped = 0, True
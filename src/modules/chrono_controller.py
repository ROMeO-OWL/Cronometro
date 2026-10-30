from modules.time_model import TimeModel
class ChronoController:
    def __init__(self, app, view): self.model, self.app, self.view = TimeModel(), app, view
    def toggle(self): self.model.stopped = not self.model.stopped; self.model.stopped and self._stop() or self._start()
    def _start(self): self.view.set_stop_state(); self._loop()
    def _loop(self): not self.model.stopped and (self.model.tick(), self.view.update_time(self.model.format_time(self.model.actual)), self.app.after(1000, self._loop))
    def _stop(self):
        self.model.record_and_reset()
        m = self.model.format_short(self.model.minimum) if self.model.minimum else "--:--"
        x = self.model.format_short(self.model.maximum) if self.model.maximum else "--:--"
        a = self.model.format_short(self.model.get_average()) if self.model.history else "--:--"
        self.view.set_start_state(m, x, a)
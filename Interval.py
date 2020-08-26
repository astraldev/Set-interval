#!python3
k=0
val = 0
"""
  Set interval 
@param interval:
  Time to perform function.
  In Seconds
@param  Function:
  function to perform
@param  end:
  Time to end interval after
  Defaults to 1000 seconds
"""
from threading import Timer
class SetInterval:
  def __init__(self, interval, function, end=1000):
    global k
    self.k = k
    k = self.k
    self.interval = interval
    self.function = function
    self.end = end
    self._interval()
  def _interval(self):
    global val 
    self.k2 = Timer(self.interval,self._interval)
    if self.k == self.end:
      self.k2.cancel()
      return
    val = self.function()
    self.val = val    
    self.k = self.k+1
    self.k2.start()
  def cancel(self):
    self.k2.cancel()
    return


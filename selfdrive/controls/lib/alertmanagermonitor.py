from selfdrive.controls.lib.alertmanager2 import AlertManager2

class AlertManagerMonitor:
    """Alert Manager Monitor"""

    managers = []
    
    def __init__(self):
        man1 = AlertManager2()
        man2 = AlertManager2()
        self.managers.append(man1)
        self.managers.append(man2)

    def monitor(self):
        for man in self.managers:
           if man.is_fail() == True:
              self.recover(man)
        
        
    def recover(self, a: AlertManager2):
        a.recover()     
        
    def voting(self) -> AlertManager2 :
       if self.managers[0].is_fail == False:
          return self.managers[0]  
       elif self.managers[1].is_fail == False:
          return self.managers[1]   
       else:
          monitor(self)
          return self.managers[0]

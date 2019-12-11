class base:
   
    @staticmethod
    def basefunction():
        print("inside base function")
class derived(base):
    
    def derivedfunction(self):
        print("inside derived class static method")
        base.basefunction()
        derived.basefunction()
        self.basefunction()
        super().basefunction()

obj=derived()        
obj.derivedfunction()
    

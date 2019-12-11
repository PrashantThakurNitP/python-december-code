class base:
    x=11#STATIC METHOD
    @staticmethod
    def basefunction():
        print("inside base function")
class derived(base):
    @staticmethod
    def derivedfunction():
        print("inside derived class static method")
        base.basefunction()
        derived.basefunction()
        print("using base.x is perfect way x= ",base.x)
        print("but we can also access usind deived.x hence x=",derived.x)
derived.derivedfunction()
    

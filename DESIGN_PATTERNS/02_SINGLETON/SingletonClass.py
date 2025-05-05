class Singleton:
    __instance = None

    def __new__(cls,*args,**kwargs):
        if cls.__instance == None:
            cls.__instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        
        return cls.__instance
    
obj_singleton1 = Singleton()
obj_singleton2 = Singleton()

print(obj_singleton1 == obj_singleton2)

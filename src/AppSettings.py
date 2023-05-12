import json

class Config:
    def toJson(self):
        return json.dumps(self,default=lambda o: o.__dict__,sort_keys=True,indent = 4)
    
    def fromJson(self,json_file : str):
        with open(json_file) as json_data:
            data = json.load(json_data)
        
        return data
    

class AppSettings:
    __json_data = None
    
    def __init__(self):
        pass

    def __new__(cls,json_file):
        if not hasattr(cls, 'instance'):
            cls.instance = super(AppSettings,cls).__new__(cls)
        return cls.instance
    
    def __init__(self,json_file):
        self.__json_data = Config().fromJson(json_file)
        
    def __enter__(self):
        return self
    
    def get_value(self,key : str):
        """Used to get json value

        Parameters
        ----------
        key : str
        json key which value you want to get
        """
        return self.__json_data[key]
 
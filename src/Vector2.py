import math

class Vector2:
    def __init__(self,x : int = 0, y : int = 0) -> int:
        self.x = x
        self.y = y
    
    def Length(self) -> float:
        """
        Returns
        ----------
        Length
        """
        return math.sqrt(self.x * self.x + self.y * self.y)

    def Magnitude(self) -> float:
        """
        Returns
        ----------
        Magnitude
        """
        return self.Length();
    
    def IsEmpty(self) -> bool:
        return (self.x == 0 and self.y == 0)  
    
    @staticmethod
    def DotProduct(lhs, rhs) -> float:
        """Used to get DotProduct of two vectors

        Parameters
        ----------
        lhs : Vector2
            left vector
        rhs : Vector2
            right vector
        Raises
        ------
        TypeError
            If one of parameter types not equal to Vector2
        """
        if not (isinstance(lhs, Vector2) and isinstance(rhs, Vector2)):
                raise TypeError("lhs and rhs supposed to be of Vector2 type")
        return lhs.x * rhs.x + lhs.y * rhs.y
    
    # Operators overloading

    def __add__(self, other):
        if isinstance(other,Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        else:
            return Vector2(self.x + other, self.y + other)
    
    def __sub__(self, other):
        if isinstance(other,Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        else:
            return Vector2(self.x - other, self.y - other)
    
    def __mul__(self, other):
        if isinstance(other,Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        else:
            return Vector2(self.x * other, self.y * other)

    # reversed operators overloading
    def __radd__(self, other):
        return self + other
    
    def __rsub__(self, other):
        return self - other
    
    def __rmul__(self, other):
        return self * other
    

    # comparison operators
    def __eq__(self,other):
        if isinstance(other,Vector2):
            return (self.x == other.x and self.y == other.y)
        else:
            raise TypeError("overloaded only for Vector2 type")
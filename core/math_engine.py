import math

class Vector3:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    # الجمع: v1 + v2
    def __add__(self, other):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    # الطرح: v1 - v2
    def __sub__(self, other):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    # الضرب في رقم (Scaling): v * n
    def __mul__(self, scalar):
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    # طول المتجه (Magnitude)
    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    # تطبيع المتجه (Normalize): جعل طوله 1 مع الحفاظ على اتجاهه
    def normalize(self):
        mag = self.length()
        if mag > 0:
            return self * (1.0 / mag)
        return Vector3()

    # الضرب القياسي (Dot Product): مفيد لحساب الإضاءة
    @staticmethod
    def dot(v1, v2):
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    # الضرب الاتجاهي (Cross Product): مفيد لحساب "النورمال" (اتجاه الوجه)
    @staticmethod
    def cross(v1, v2):
        return Vector3(
            v1.y * v2.z - v1.z * v2.y,
            v1.z * v2.x - v1.x * v2.z,
            v1.x * v2.y - v1.y * v2.x
        )

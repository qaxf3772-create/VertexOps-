from core.math_engine import Vector3

class Face:
    """كائن يمثل وجهاً واحداً من المجسم (غالباً مثلث أو رباعي)"""
    def __init__(self, vertex_indices, color=(200, 200, 200)):
        self.vertex_indices = vertex_indices # قائمة بأرقام النقاط في قائمة الـ Mesh
        self.color = color
        self.normal = Vector3() # سيتم حسابه ديناميكياً للإضاءة

class Mesh:
    """كائن يمثل مجسماً كاملاً يتكون من نقاط وأوجه"""
    def __init__(self, vertices, faces, position=None):
        # قائمة من كائنات Vector3
        self.vertices = [Vector3(v[0], v[1], v[2]) for v in vertices]
        # قائمة من كائنات Face
        self.faces = [Face(f[0], f[1]) for f in faces]
        
        self.position = position if position else Vector3(0, 0, 0)
        self.rotation = Vector3(0, 0, 0)
        self.scale = Vector3(1, 1, 1)

    def translate(self, dx, dy, dz):
        self.position += Vector3(dx, dy, dz)

    def rotate(self, rx, ry, rz):
        self.rotation += Vector3(rx, ry, rz)

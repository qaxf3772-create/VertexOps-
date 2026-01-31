from core.mesh import Mesh

class Box(Mesh):
    """مصنع لإنشاء مكعب ببارامترات محددة"""
    def __init__(self, size=1.0, color=(100, 150, 255), pos=None):
        s = size / 2.0
        # تعريف النقاط (Vertices)
        vertices = [
            [-s, -s,  s], [ s, -s,  s], [ s,  s,  s], [-s,  s,  s], # الأمام
            [-s, -s, -s], [ s, -s, -s], [ s,  s, -s], [-s,  s, -s]  # الخلف
        ]
        
        # تعريف الأوجه (Faces) باستخدام الـ Indices
        # كل وجه يتكون من (قائمة النقاط، اللون)
        faces = [
            ([0, 1, 2, 3], color), # أمام
            ([1, 5, 6, 2], color), # يمين
            ([5, 4, 7, 6], color), # خلف
            ([4, 0, 3, 7], color), # يسار
            ([3, 2, 6, 7], color), # أعلى
            ([4, 5, 1, 0], color)  # أسفل
        ]
        
        super().__init__(vertices, faces, pos)

class Pyramid(Mesh):
    """مصنع لإنشاء هرم رباعي"""
    def __init__(self, size=1.0, color=(255, 100, 100), pos=None):
        s = size / 2.0
        vertices = [
            [-s, 0, -s], [s, 0, -s], [s, 0, s], [-s, 0, s], # القاعدة
            [0, size, 0] # القمة
        ]
        faces = [
            ([0, 1, 2, 3], color), # القاعدة
            ([0, 1, 4], color),    # الأوجه الجانبية
            ([1, 2, 4], color),
            ([2, 3, 4], color),
            ([3, 0, 4], color)
        ]
        super().__init__(vertices, faces, pos)

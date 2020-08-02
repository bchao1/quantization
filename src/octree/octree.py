
class OctreeNode(object):
    def __init__(self):
        self.refs = 0
        self.red = None
        self.green = None
        self.blue = None
        self.children = [None] * 8
    
    def increment_ref(self):
        self.refs += 1
    
    def set_color(self, color):
        r, g, b = color
        self.red = r
        self.green = g 
        self.blue = b

    
class Octree(object):
    def __init__(self):
        self.root = OctreeNode()
    
    def insert(self, color):
        p = self.root
        r, g, b = color  # decompose
        for i in range(8):  # 8 bits for each color channel
            r_msb = (r >> (7 - i)) & 1
            g_msb = (g >> (7 - i)) & 1
            b_msb = (b >> (7 - i)) & 1
            c_id = (r_msb << 2) + (g_msb << 1) + b_msb
            if p.children[c_id] is None:
                p.children[c_id] = OctreeNode()
            p = p.children[c_id]
        p.set_color(color)
        p.increment_ref()

            
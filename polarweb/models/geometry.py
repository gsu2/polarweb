__author__ = 'sandy_000'

from euclid import Vector2

class Rectangle():
    size = Vector2()
    position = Vector2()

    def __init__(self, size=Vector2(100, 100),
                 position=Vector2(0, 0)):
        self.size = size
        self.position = position

    def contains(self, p):
        return self.position.x < p.x < (self.size.x + self.position.x) \
                and self.position.y < p.y < (self.size.y + self.position.y)

    def __str__(self):
        return u"Rectangle size %s,%s and pos %s,%s" % (self.size.x, self.size.y, self.position.x, self.position.y)

    def height_to_width(self):
        if self.size.x != 0.0:
            return self.size.y / self.size.x
        else:
            return 1.0





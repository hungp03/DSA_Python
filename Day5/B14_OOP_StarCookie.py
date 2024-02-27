class StarCookie:
    def __init__(self, color, weight):
        self.color = color
        self.weight = weight
    
    def to_string(self):
        return f'The Star Cookie is {self.color} in color and weighs {self.weight} gram(s).'

star_cookie1 = StarCookie('red', 16)
print(star_cookie1.to_string())

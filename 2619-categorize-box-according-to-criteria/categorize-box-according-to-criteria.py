class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        box1=''
        box2=''

        if length >= 10000 or width >= 10000 or height >= 10000 or length * width * height >= 1000000000:
            box1='bulky'

        if mass >= 100:
            box2='heavy'

        if box1=='bulky' and box2=='heavy':
            return "Both"
        elif box1=='bulky' and box2!='heavy':
            return "Bulky"
        elif box1!='bulky' and box2=='heavy':
            return "Heavy"
        else:
            return "Neither"
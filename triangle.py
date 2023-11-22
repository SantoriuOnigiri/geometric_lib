import unittest

class TriangleTestCase(unittest.TestCase):

    def area_test_zero(self):
        res = area(0,0)
        self.assertEqual(res,0)

    def area_test_number(self):
        res = area(7,4)
        self.assertEqual(res,14.0)

    def area_test_float_number(self):
        res = area(9.46,5.345)
        self.assertEqual(res,25.281850000000002)

    def perimeter_test_zero(self):
        res = perimeter(0,14,5)
        self.assertEqual(res,0)

    def perimeter_test_float_number(self):
        res = perimeter(7.4567,8.919082,6.014142)
        self.assertEqual(res,22.389924)

    def perimeter_test_number(self):
        res = perimeter(3,4,5)
        self.assertEqual(res,12)

    def perimeter_test_number2(self):
        res = perimeter(2,2,6)
        self.assertEqual(res,"ERROR")




def area(a,h):
    '''
        Возвращает площадь треугольника с основанием a и высотой h.

            Параметры:
                a(int): основание треугольника
                h(int): высота проведенная к стороне h

            Возвращаемое значение:
                 a * h/2(int): площадь  треугольника
        '''
    return a * h/2

def perimeter(a,b,c):
    '''
        Возвращает периметр треугольника со сторонами a b c.

            Параметры:
                a(int): первая сторона треугольника
                b(int): вторая сторона треугольника
                b(int): третья сторона треугольника

            Возвращаемое значение:
                a + и + с: периметр треугольника
    '''
    return a + b + c

print(perimeter(7.4567,8.919082,6.014142))
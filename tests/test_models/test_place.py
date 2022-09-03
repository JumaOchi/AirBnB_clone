#!/usr/bin/python3
'''Unittest for base_model.py([..])'''
from datetime import datetime
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''Define unit test for the Place Class'''
    def test_init_a(self):
        '''Tests the __init__ function'''
        a = Place()
        self.assertEqual(type(a), Place)
        self.assertEqual(type(a.id), str)
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)

    def test_init_b(self):
        '''Tests the __init__ function'''
        b = Place()
        self.assertEqual(type(b), Place)
        self.assertEqual(type(b.id), str)
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)

    def test_add_attribute_a(self):
        a = Place()
        a.name = 'KSI'
        a.number = 999
        self.assertEqual(a.name, 'KSI')
        self.assertEqual(a.number, 999)
        self.assertEqual(type(a.name), str)
        self.assertEqual(type(a.number), int)

    def test_add_attribute_b(self):
        b = Place()
        b.name = 'Swarmz'
        b.number = 0
        self.assertEqual(b.name, 'Swarmz')
        self.assertEqual(b.number, 0)
        self.assertEqual(type(b.name), str)
        self.assertEqual(type(b.number), int)

    def test_str_a(self):
        '''Tests the __str__ function'''
        a = Place()
        nm = a.__class__.__name__
        dc = a.__dict__
        self.assertEqual(a.__str__(), f"[{nm}] ({a.id}) {dc}")

    def test_str_b(self):
        '''Tests the __str__ function'''
        b = Place()
        nm = b.__class__.__name__
        dc = b.__dict__
        self.assertEqual(b.__str__(), f"[{nm}] ({b.id}) {dc}")

    def test_save_a(self):
        '''Tests the save function'''
        a = Place()
        cd = a.created_at.isoformat()
        ud = a.updated_at.isoformat()
        self.assertEqual(cd, ud)
        a.save()
        self.assertNotEqual(ud, a.updated_at.isoformat())

    def test_save_b(self):
        '''Tests the save function'''
        b = Place()
        cd = b.created_at.isoformat()
        ud = b.updated_at.isoformat()
        self.assertEqual(cd, ud)
        b.save()
        self.assertNotEqual(ud, b.updated_at.isoformat())

    def test_to_dict_a(self):
        '''Tests the to_dict function'''
        a = Place()
        dc = a.to_dict()
        self.assertEqual(type(a.created_at), datetime)
        self.assertEqual(type(a.updated_at), datetime)
        self.assertEqual(dc['__class__'], 'Place')
        self.assertEqual(type(dc['updated_at']), str)
        self.assertEqual(type(dc['created_at']), str)

    def test_to_dict_b(self):
        '''Tests the to_dict function'''
        b = Place()
        dc = b.to_dict()
        self.assertEqual(type(b.created_at), datetime)
        self.assertEqual(type(b.updated_at), datetime)
        self.assertEqual(dc['__class__'], 'Place')
        self.assertEqual(type(dc['updated_at']), str)
        self.assertEqual(type(dc['created_at']), str)

    def test_attr_1(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.city_id, '')

    def test_attr_2(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.user_id, '')

    def test_attr_3(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.name, '')

    def test_attr_4(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.description, '')

    def test_attr_5(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.number_bathrooms, 0)

    def test_attr_6(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.max_guest, 0)

    def test_attr_7(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.price_by_night, 0)

    def test_attr_8(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.number_rooms, 0)

    def test_attr_9(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertAlmostEqual(a.latitude, 0.0)

    def test_attr_10(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertAlmostEqual(a.longitude, 0.0)

    def test_attr_11(self):
        '''Tests an attribute of Place'''
        a = Place()
        self.assertEqual(a.amenity_ids, [])


if __name__ == '__main__':
    unittest.main()

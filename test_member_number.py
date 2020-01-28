from member_number import get_org_id,get_sequential_id,create_id,check_id
import unittest

class GeneralTest(unittest.TestCase):

    def test_initial_number(self):
        id_a = create_id(0)
        self.assertTrue(check_id(id_a))
        self.assertEqual(get_org_id(id_a), '123')
        self.assertEqual(get_sequential_id(id_a), '00001')

        id_b = create_id('016234569991')
        self.assertTrue(check_id(id_b))
        self.assertEqual(get_org_id(id_b), '016')
        self.assertEqual(get_sequential_id(id_b), '23457')

    def test_create_sequential_numbers(self):
        id_a = create_id(0)
        id_b = create_id(id_a)
        id_c = create_id(id_b)
        id_d = create_id(id_c)
        id_e = create_id(id_d)

        print(id_a)
        print(id_b)
        print(id_c)
        print(id_d)
        print(id_e)

        self.assertTrue(check_id(id_a))
        self.assertTrue(check_id(id_b))
        self.assertTrue(check_id(id_c))
        self.assertTrue(check_id(id_d))
        self.assertTrue(check_id(id_e))

        self.assertNotEqual(id_a, id_b)
        self.assertNotEqual(id_b, id_c)
        self.assertNotEqual(id_c, id_d)
        self.assertNotEqual(id_d, id_e)


    def test_get_org_id(self):
        self.assertEqual(get_org_id(123100019871), '123')
        self.assertEqual(get_org_id(456100019871), '456')
        self.assertEqual(get_org_id(789100019871), '789')
        self.assertNotEqual(get_org_id(123100019871), '456')

    def test_get_sequential_id(self):
        self.assertEqual(get_sequential_id(123100019871), '10001')
        self.assertEqual(get_sequential_id(456134519871), '13451')
        self.assertEqual(get_sequential_id(789745019871), '74501')

    def test_check_id(self):
        id_a = create_id(0)
        id_b = create_id(123100000000)
        self.assertTrue(check_id(id_a))
        self.assertTrue(check_id(id_b))
        self.assertNotEqual(id_a, id_b)

        id_c = create_id(id_b)

        self.assertTrue(check_id(id_c))
        self.assertNotEqual(id_b, id_c)
        self.assertNotEqual(id_a, id_c)

        self.assertFalse(check_id(123100025806))


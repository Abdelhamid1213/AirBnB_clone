import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_save(self):
        obj = BaseModel()
        initial_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(initial_updated_at, obj.updated_at)

    def test_to_dict(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

def test_str(self):
    obj = BaseModel()
    obj_str = str(obj)

    self.assertIsInstance(obj_str, str)
    self.assertIn('BaseModel', obj_str)
    self.assertIn(obj.id, obj_str)

    created_at_str = obj.created_at.isoformat()
    updated_at_str = obj.updated_at.isoformat()

    created_at_dt = datetime.fromisoformat(created_at_str)
    updated_at_dt = datetime.fromisoformat(updated_at_str)

    self.assertIn(created_at_dt, obj_str)
    self.assertIn(updated_at_dt, obj_str)

if __name__ == '__main__':
    unittest.main()

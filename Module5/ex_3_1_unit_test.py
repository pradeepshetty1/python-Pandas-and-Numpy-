import unittest
import mock

class RegularPyClass(object):
    @classmethod
    def getClassName(cls):
        return cls.__name__

    def __init__(self):
        self._i_m_bool = True
        self._i_m_stng = 'String'
        self._i_m_list = [1,2,3,4]
        self._i_m_dict = {'a': 1,
                          'b': 2,
                          'c': 3}

    # returns boolean
    def getBool(self):
        return self._i_m_bool

    # returns string
    def getString(self):
        # Enforcing constraint to accept non-unicode strings. This is not recommended.
        # Always check against basestring to support both unicode and normal inputs.
        if not isinstance(self._i_m_stng, str):
            raise TypeError
        else:
            return self._i_m_stng

    def setString(self, new_string):
        if not isinstance(new_string, str):
            raise TypeError

        self._i_m_stng = new_string

    # returns list
    def getList(self):
        return self._i_m_list

    # returns dictionary
    def getDict(self):
        # First confirm if the object is dictionary
        try:
            assert isinstance(self._i_m_dict, dict), "_i_m_dict should be a dictionary"
            return self._i_m_dict
        except AssertionError as e:
            raise TypeError("{0}. Expected dictionary but got {1}".format(e.message, type(self._i_m_dict)))


    # looks up supplied key in dictionary and returns its value
    def getValueFromDict(self, key):
        if key not in self.getDict():
            raise KeyError
        else:
            return self.getDict()[key]

    # abstract method to be implemented by subclassess
    def yetToBeImplemented(self):
        raise NotImplementedError


class RegularPyClass_Tests(unittest.TestCase):
    # Setup test environment - hack classes, methods, attributes and much more
    def setUp(self):
        print "Initiating setup"
        self.reference = RegularPyClass()
        self.expected_list = [1,2,3,4]
        self.expected_strng = unicode('Unicode and str subclass from basestring')
        self.expected_dict = {'a': 1,
                              'b': 2,
                              'c': 3}

    def testBool(self):
        #self.reference._i_m_bool = True
        self.reference._i_m_bool = False
        self.assertFalse(self.reference._i_m_bool)

    def testGetStringEquality(self):
        self.expected_strng = self.reference._i_m_stng
        self.assertEqual(self.expected_strng, self.reference._i_m_stng)

    def testGetStringException(self):
        self.reference._i_m_stng = unicode('abcd')
        self.assertRaises(TypeError, self.reference.getString)

    def testSetStringException(self):
        self.assertRaises(TypeError, self.reference.setString('its unicode'))

    def testList(self):
        # self.reference._i_m_list = dict()
        self.assertIsInstance(self.reference._i_m_list, list)

    def testListElements(self):
        # self.expected_list = self.expected_list[:3]
        self.assertListEqual(self.expected_list, self.reference._i_m_list)

    def testElementInList(self):
        self.assertIn(4,self.reference._i_m_list)
        self.assertNotIn(5,self.reference._i_m_list)
       # self.assertNotIn(3,self.reference._i_m_list)

    def testGetDict(self):
        # self.reference._i_m_dict = []
        self.assertIsInstance(self.reference._i_m_dict, dict)

    def testDictEqual(self):
        self.assertEqual(self.reference._i_m_dict, self.expected_dict)

    def testGetValueFromDict(self):
        #self.reference._i_m_dict = self.reference._i_m_list
        self.assertRaises(KeyError, self.reference.getValueFromDict, 'd')
        #self.assertIn('a', self.reference._i_m_dict)

    def testClassName(self):
        self.reference.getClassName = mock.MagicMock(return_value="TestClass")
        # print "Class Name :", self.reference.getClassName()
        self.assertEqual("TestClass",self.reference.getClassName())

    def testYetToBeImplemented(self):
        self.assertRaises(NotImplementedError, self.reference.yetToBeImplemented)

    def tearDown(self):
        # Release external resources defined under setup. Example : close test connections
        print "Tearing down"


def suite():
    st = unittest.TestSuite()
    st.addTests( unittest.TestLoader().loadTestsFromTestCase(RegularPyClass_Tests))
    return st

if __name__ == "__main__":
    unittest.main()



    #Other ways to execute in console (-m opiton of python - Run library module as a script)
    #python -m unittest ex_3_1_unit_test
    #python -m unittest ex_3_1_unit_test.RegularPyClass_Tests
    #python -m unittest ex_3_1_unit_test.RegularPyClass_Tests.testBool
    #python ex_3_1_unit_test.py -v

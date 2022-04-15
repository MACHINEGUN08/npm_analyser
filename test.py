import unittest
from src.npm_analyser.npm_analyser import npm_analyser

class Test(unittest.TestCase):
    def test_cases(self):
        """
        Test Case1: babel-core
        """
        package_details = npm_analyser('babel-core')

        self.assertEqual(package_details.package_name, 'babel-core')
        self.assertEqual(package_details.license, 'MIT')
        self.assertEqual(package_details.version, '8.7.0')
        self.assertEqual(package_details.last_published, '15 hours ago')
        self.assertEqual(package_details.number_of_dependents, '4830')
        self.assertEqual(package_details.get_dev_dependencies, '2')
        self.assertEqual(package_details.total_versions, '470')
        self.assertEqual(package_details.unpacked_size, '8.75 MB')
        self.assertEqual(package_details.weekly_downloads, '4,196,615')
        self.assertEqual(package_details.total_files, '1821')
             
if __name__ == '__main__':
    unittest.main()
    

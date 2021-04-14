import unittest,os
import fetch_data

class TestGetRquest(unittest.TestCase):
    def test_get_request(self):
        url = "https://reqres.in/api/users?page=2"
        data = fetch_data.get_request(url)
        assert type(data) is dict

        url = "https://non-existing-url"
        data = fetch_data.get_request(url)
        assert type(data) is not dict

class TestListUsers(unittest.TestCase):
    def test_list_users(self):
        url = "https://reqres.in/api/users?page=2"
        self.assertEqual(fetch_data.list_users(url), True, "Should be True")

    def test_error_list_users(self):
        url = "https://non-existing-url"
        self.assertEqual(fetch_data.list_users(url), False, "Should be False")

class TestWriteFile(unittest.TestCase):
    def test_Write_file(self):
        fetch_data.write_file("testfile","testusername", "testmail", "https://reqres.in/img/faces/10-image.jpg")
        os.path.isfile("testfile")
        os.remove("testfile")

if __name__ == '__main__':
    unittest.main()

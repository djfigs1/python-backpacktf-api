import unittest, json, os

class UserRequesterTests(unittest.TestCase):
    def setUp(self):
        from pyPackTF import UserRequester
        UR = UserRequester()
        json = UR.requestSteamIDS(["76561198138725392"])
        users = UR.getBPKUsers(steamids=None, json=json)
        self.UR = UR
        self.classJSON = json
        self.users = users

        def isResponseSuccessful(self):
            success = self.classJSON['response']['success']
            if success == 1:
                return True
            else:
                return False

        def getMessage(self):
            try:
                message = self.classJSON['response']['message']
            except KeyError:
                raise (Exceptions.NoErrorMessage)
            return str(message)

        def getCurrentTime(self):
            current_time = self.classJSON['response']['current_time']
            return current_time

    def test_IsValid(self):
        success = self.classJSON['response']['success']
        self.assertEqual(success, True)

    def test_CurrentTime(self):
        current_time = self.classJSON['response']['current_time']
        self.assertEqual(type(current_time), int)

    def test_ErrorMessage(self):
        valid = False
        try:
            message = self.classJSON['response']['message']
        except KeyError:
            valid = True
        self.assertEqual(valid, True)


    def test_getUserSuccess(self):
        valid = True
        for user in self.users:
            if not user.getSuccess():
                valid = False

        self.assertEqual(valid, True)


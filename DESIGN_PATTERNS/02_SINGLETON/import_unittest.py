import unittest
import json
import os
from PYTHON_MACK.DESIGN_PATTERNS._02_SINGLETON.singleton_configure import ConfigManager

# PYTHON_MACK/DESIGN_PATTERNS/02_SINGLETON/test_singleton_configure.py


class TestConfigManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config_data = {
            "database_url": "http://localhost:5432/meubanco",
            "debug_mode": True,
            "max_connections": 10,
            "api_key": "12345-abcde-67890-fghij",
            "email_service": {
                "smtp_server": "smtp.exemplo.com",
                "smtp_port": 587,
                "use_tls": True
            }
        }
        with open('config.json', 'w') as file:
            json.dump(cls.config_data, file)

    @classmethod
    def tearDownClass(cls):
        os.remove('config.json')

    def test_singleton_behavior(self):
        config_manager1 = ConfigManager()
        config_manager2 = ConfigManager()
        self.assertIs(config_manager1, config_manager2)

    def test_get_config_existing_key(self):
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_config("database_url"), "http://localhost:5432/meubanco")
        self.assertEqual(config_manager.get_config("debug_mode"), True)
        self.assertEqual(config_manager.get_config("max_connections"), 10)
        self.assertEqual(config_manager.get_config("api_key"), "12345-abcde-67890-fghij")
        self.assertEqual(config_manager.get_config("email_service")['smtp_server'], "smtp.exemplo.com")

    def test_get_config_non_existing_key(self):
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_config("non_existing_key"), "Configuração não encontrada")

if __name__ == '__main__':
    unittest.main()import unittest
import json
import os
from PYTHON_MACK.DESIGN_PATTERNS._02_SINGLETON.singleton_configure import ConfigManager

# PYTHON_MACK/DESIGN_PATTERNS/02_SINGLETON/test_singleton_configure.py


class TestConfigManager(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.config_data = {
            "database_url": "http://localhost:5432/meubanco",
            "debug_mode": True,
            "max_connections": 10,
            "api_key": "12345-abcde-67890-fghij",
            "email_service": {
                "smtp_server": "smtp.exemplo.com",
                "smtp_port": 587,
                "use_tls": True
            }
        }
        with open('config.json', 'w') as file:
            json.dump(cls.config_data, file)

    @classmethod
    def tearDownClass(cls):
        os.remove('config.json')

    def test_singleton_behavior(self):
        config_manager1 = ConfigManager()
        config_manager2 = ConfigManager()
        self.assertIs(config_manager1, config_manager2)

    def test_get_config_existing_key(self):
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_config("database_url"), "http://localhost:5432/meubanco")
        self.assertEqual(config_manager.get_config("debug_mode"), True)
        self.assertEqual(config_manager.get_config("max_connections"), 10)
        self.assertEqual(config_manager.get_config("api_key"), "12345-abcde-67890-fghij")
        self.assertEqual(config_manager.get_config("email_service")['smtp_server'], "smtp.exemplo.com")

    def test_get_config_non_existing_key(self):
        config_manager = ConfigManager()
        self.assertEqual(config_manager.get_config("non_existing_key"), "Configuração não encontrada")

if __name__ == '__main__':
    unittest.main()
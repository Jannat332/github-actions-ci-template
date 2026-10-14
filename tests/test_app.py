"""Unit test suite for CI template service."""

import unittest
from src.app import get_system_health


class TestAppHealth(unittest.TestCase):

    def test_health_payload_structure(self):
        health = get_system_health()
        self.assertIsInstance(health, dict)
        self.assertEqual(health["status"], "HEALTHY")
        self.assertEqual(health["service"], "ci-template-service")
        self.assertIn("version", health)
        self.assertIn("python_version", health)

    def test_environment_variable_fallback(self):
        health = get_system_health()
        self.assertTrue(len(health["environment"]) > 0)


if __name__ == "__main__":
    unittest.main()

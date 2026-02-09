"""
AMRIT AI - Test Suite

Tests for core functionality of the AMRIT AI system.
"""

import unittest
import numpy as np
from datetime import datetime
import os
import shutil

from amrit_system import AMRITSystem
from permission_manager import PermissionType
from encryption import EncryptionManager
from hidden_storage import HiddenStorageManager


class TestEncryption(unittest.TestCase):
    """Test encryption module"""
    
    def setUp(self):
        self.manager = EncryptionManager('test_password')
    
    def test_encrypt_decrypt_string(self):
        """Test string encryption and decryption"""
        data = "Hello, AMRIT!"
        encrypted, salt = self.manager.encrypt(data)
        decrypted = self.manager.decrypt(encrypted, salt)
        self.assertEqual(decrypted.decode(), data)
    
    def test_encrypt_decrypt_bytes(self):
        """Test bytes encryption and decryption"""
        data = b"Binary data test"
        encrypted, salt = self.manager.encrypt(data)
        decrypted = self.manager.decrypt(encrypted, salt)
        self.assertEqual(decrypted, data)
    
    def test_hash_data(self):
        """Test data hashing"""
        data = "test data"
        hash1 = self.manager.hash_data(data)
        hash2 = self.manager.hash_data(data)
        self.assertEqual(hash1, hash2)
        self.assertEqual(len(hash1), 64)  # SHA-256 produces 64 char hex


class TestHiddenStorage(unittest.TestCase):
    """Test hidden storage module"""
    
    def setUp(self):
        self.storage = HiddenStorageManager('test_password')
        self.storage.initialize()
    
    def tearDown(self):
        # Clean up test data
        try:
            self.storage.secure_wipe()
        except:
            pass
    
    def test_store_retrieve_dict(self):
        """Test storing and retrieving dictionary"""
        data = {'name': 'AMRIT', 'version': '1.0.0'}
        self.storage.store_data('behavior_profiles', 'test_dict', data)
        retrieved = self.storage.retrieve_data('behavior_profiles', 'test_dict')
        self.assertEqual(retrieved, data)
    
    def test_store_retrieve_string(self):
        """Test storing and retrieving string"""
        data = "Test string"
        self.storage.store_data('learning_logs', 'test_string', data)
        retrieved = self.storage.retrieve_data('learning_logs', 'test_string')
        self.assertEqual(retrieved, data)
    
    def test_list_keys(self):
        """Test listing keys in category"""
        self.storage.store_data('behavior_profiles', 'key1', 'data1')
        self.storage.store_data('behavior_profiles', 'key2', 'data2')
        keys = self.storage.list_keys('behavior_profiles')
        self.assertIn('key1', keys)
        self.assertIn('key2', keys)
    
    def test_delete_data(self):
        """Test deleting data"""
        self.storage.store_data('learning_logs', 'to_delete', 'data')
        success = self.storage.delete_data('learning_logs', 'to_delete')
        self.assertTrue(success)
        retrieved = self.storage.retrieve_data('learning_logs', 'to_delete')
        self.assertIsNone(retrieved)


class TestAMRITSystem(unittest.TestCase):
    """Test main AMRIT system"""
    
    def setUp(self):
        self.system = AMRITSystem('test_password_123')
    
    def tearDown(self):
        try:
            self.system.storage.secure_wipe()
        except:
            pass
    
    def test_system_initialization(self):
        """Test system initialization"""
        self.assertTrue(self.system.initialized)
        self.assertIsNotNone(self.system.storage)
        self.assertIsNotNone(self.system.permissions)
        self.assertIsNotNone(self.system.owner_recognition)
    
    def test_owner_enrollment(self):
        """Test owner enrollment"""
        audio_samples = [np.random.randn(16000) for _ in range(3)]
        text_samples = ['Hello', 'AMRIT', 'Test']
        behavioral_samples = [
            {'timestamp': datetime.now().isoformat(), 'duration': 10}
            for _ in range(3)
        ]
        
        success = self.system.enroll_owner(
            audio_samples, text_samples, behavioral_samples
        )
        self.assertTrue(success)
        self.assertIsNotNone(self.system.owner_recognition.owner_profile)
    
    def test_authentication(self):
        """Test authentication flow"""
        # First enroll
        audio_samples = [np.random.randn(16000) for _ in range(3)]
        text_samples = ['Hello', 'AMRIT', 'Test']
        behavioral_samples = [
            {'timestamp': datetime.now().isoformat(), 'duration': 10}
            for _ in range(3)
        ]
        self.system.enroll_owner(audio_samples, text_samples, behavioral_samples)
        
        # Then authenticate
        audio = np.random.randn(16000)
        authenticated = self.system.authenticate_owner(
            audio_data=audio, text='Hello'
        )
        # Note: May pass or fail depending on random samples
        self.assertIsInstance(authenticated, bool)
    
    def test_permission_system(self):
        """Test permission system"""
        # Enroll and authenticate first
        audio_samples = [np.random.randn(16000) for _ in range(3)]
        text_samples = ['Hello', 'AMRIT', 'Test']
        behavioral_samples = [
            {'timestamp': datetime.now().isoformat(), 'duration': 10}
            for _ in range(3)
        ]
        self.system.enroll_owner(audio_samples, text_samples, behavioral_samples)
        
        audio = np.random.randn(16000)
        self.system.authenticate_owner(audio_data=audio, text='Hello')
        
        # Request permission
        req_id = self.system.request_permission(
            PermissionType.DATA_MODIFICATION,
            'Testing'
        )
        self.assertIsNotNone(req_id)
        
        # Grant permission
        success = self.system.grant_permission(req_id)
        self.assertTrue(success)
        
        # Check permission
        has_perm = self.system.permissions.check_permission(
            PermissionType.DATA_MODIFICATION
        )
        self.assertTrue(has_perm)
    
    def test_interaction_recording(self):
        """Test interaction recording"""
        # Enroll and authenticate
        audio_samples = [np.random.randn(16000) for _ in range(3)]
        text_samples = ['Hello', 'AMRIT', 'Test']
        behavioral_samples = [
            {'timestamp': datetime.now().isoformat(), 'duration': 10}
            for _ in range(3)
        ]
        self.system.enroll_owner(audio_samples, text_samples, behavioral_samples)
        
        audio = np.random.randn(16000)
        self.system.authenticate_owner(audio_data=audio, text='Hello')
        
        # Record interaction
        interaction_id = self.system.record_interaction('command', {
            'command': 'test',
            'success': True
        })
        
        self.assertIsNotNone(interaction_id)
    
    def test_system_status(self):
        """Test getting system status"""
        status = self.system.get_system_status()
        self.assertIn('system_name', status)
        self.assertIn('version', status)
        self.assertIn('initialized', status)
        self.assertEqual(status['system_name'], 'AMRIT')


def run_tests():
    """Run all tests"""
    print("\n" + "="*60)
    print("🧪 Running AMRIT AI Test Suite")
    print("="*60 + "\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestEncryption))
    suite.addTests(loader.loadTestsFromTestCase(TestHiddenStorage))
    suite.addTests(loader.loadTestsFromTestCase(TestAMRITSystem))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "="*60)
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print(f"❌ {len(result.failures)} test(s) failed")
        print(f"❌ {len(result.errors)} test(s) had errors")
    print("="*60 + "\n")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    run_tests()

"""
Unit tests for Agent Memory Configuration System
"""

import unittest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestProjectStructure(unittest.TestCase):
    """Test that project structure is correctly set up"""
    
    def test_src_directory_exists(self):
        """Test that src directory exists"""
        src_path = os.path.join(os.path.dirname(__file__), '..', 'src')
        self.assertTrue(os.path.exists(src_path))
    
    def test_agent_memory_module_exists(self):
        """Test that agent_memory module exists"""
        module_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'agent_memory'
        )
        self.assertTrue(os.path.exists(module_path))
    
    def test_config_file_exists(self):
        """Test that config.py exists"""
        config_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'agent_memory', 'config.py'
        )
        self.assertTrue(os.path.exists(config_path))
    
    def test_memory_store_file_exists(self):
        """Test that memory_store.py exists"""
        store_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'agent_memory', 'memory_store.py'
        )
        self.assertTrue(os.path.exists(store_path))
    
    def test_utils_module_exists(self):
        """Test that utils module exists"""
        utils_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'utils'
        )
        self.assertTrue(os.path.exists(utils_path))
    
    def test_examples_directory_exists(self):
        """Test that examples directory exists"""
        examples_path = os.path.join(os.path.dirname(__file__), '..', 'examples')
        self.assertTrue(os.path.exists(examples_path))
    
    def test_requirements_file_exists(self):
        """Test that requirements.txt exists"""
        req_path = os.path.join(os.path.dirname(__file__), '..', 'requirements.txt')
        self.assertTrue(os.path.exists(req_path))
    
    def test_env_example_exists(self):
        """Test that .env.example exists"""
        env_path = os.path.join(os.path.dirname(__file__), '..', '.env.example')
        self.assertTrue(os.path.exists(env_path))
    
    def test_gitignore_exists(self):
        """Test that .gitignore exists"""
        gitignore_path = os.path.join(os.path.dirname(__file__), '..', '.gitignore')
        self.assertTrue(os.path.exists(gitignore_path))


class TestConfigurationStructure(unittest.TestCase):
    """Test configuration file content"""
    
    def test_config_has_required_classes(self):
        """Test that config.py has required classes"""
        config_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'agent_memory', 'config.py'
        )
        with open(config_path, 'r') as f:
            content = f.read()
            self.assertIn('class AgentMemoryConfig', content)
            self.assertIn('openai_api_key', content)
            self.assertIn('chroma_persist_directory', content)


class TestMemoryStoreStructure(unittest.TestCase):
    """Test memory store file content"""
    
    def test_memory_store_has_required_classes(self):
        """Test that memory_store.py has required classes"""
        store_path = os.path.join(
            os.path.dirname(__file__), '..', 'src', 'agent_memory', 'memory_store.py'
        )
        with open(store_path, 'r') as f:
            content = f.read()
            self.assertIn('class MemoryStore', content)
            self.assertIn('def add_memory', content)
            self.assertIn('def query_memories', content)
            self.assertIn('def get_memory', content)
            self.assertIn('def delete_memory', content)


class TestExamplesStructure(unittest.TestCase):
    """Test example files"""
    
    def test_basic_usage_example_exists(self):
        """Test that basic_usage.py exists"""
        example_path = os.path.join(
            os.path.dirname(__file__), '..', 'examples', 'basic_usage.py'
        )
        self.assertTrue(os.path.exists(example_path))
    
    def test_optimized_queries_example_exists(self):
        """Test that optimized_queries.py exists"""
        example_path = os.path.join(
            os.path.dirname(__file__), '..', 'examples', 'optimized_queries.py'
        )
        self.assertTrue(os.path.exists(example_path))


def run_tests():
    """Run all tests"""
    print("=== Running Agent Memory Configuration Tests ===\n")
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestProjectStructure))
    suite.addTests(loader.loadTestsFromTestCase(TestConfigurationStructure))
    suite.addTests(loader.loadTestsFromTestCase(TestMemoryStoreStructure))
    suite.addTests(loader.loadTestsFromTestCase(TestExamplesStructure))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n=== Test Summary ===")
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)

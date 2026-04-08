import unittest
import importlib.util
from pathlib import Path


def _load_exercise_module():
    module_path = Path(__file__).with_name("exercise.py")
    spec = importlib.util.spec_from_file_location("step04_exercise", module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module


exercise = _load_exercise_module()


class TestSanitizeTags(unittest.TestCase):
    def test_empty_input(self):
        """Test sanitize_tags with empty list."""
        result = exercise.sanitize_tags([])
        self.assertEqual(result, [])

    def test_duplicate_tags_with_mixed_case(self):
        """Test sanitize_tags removes duplicates and lowercases."""
        result = exercise.sanitize_tags(["Python", "python", "PYTHON", "Java"])
        self.assertEqual(result, ["python", "java"])
        self.assertEqual(len(result), 2)

    def test_tags_with_punctuation(self):
        """Test sanitize_tags removes punctuation except hyphens."""
        result = exercise.sanitize_tags(["Python@2.0", "C++", "node-js"])
        self.assertEqual(result, ["python20", "c", "node-js"])
        self.assertIn("node-js", result)

    def test_tags_with_leading_trailing_whitespace(self):
        """Test sanitize_tags trims whitespace."""
        result = exercise.sanitize_tags(["  Python  ", "\tJava\n", "  Go  "])
        self.assertEqual(result, ["python", "java", "go"])
        self.assertEqual(len(result), 3)

    def test_combined_edge_cases(self):
        """Test sanitize_tags with multiple issues combined."""
        result = exercise.sanitize_tags([
            "  TypeScript!  ",
            "typescript",
            "  C#-Sharp  ",
            "c#-sharp"
        ])
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "typescript")
        self.assertEqual(result[1], "c-sharp")

    def test_tags_becoming_empty_after_cleanup(self):
        """Test sanitize_tags removes tags that become empty after punctuation removal."""
        result = exercise.sanitize_tags(["@@@", "!!!", "python", "***"])
        self.assertEqual(result, ["python"])
        self.assertEqual(len(result), 1)


if __name__ == "__main__":
    unittest.main()
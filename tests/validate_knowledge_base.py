#!/usr/bin/env python3
"""
Validate Knowledge Base JSON Files Against Schemas

This script validates all knowledge base JSON files against their JSON schemas
to ensure data integrity and catch errors early.

Usage:
    python tests/validate_knowledge_base.py
    python tests/validate_knowledge_base.py --file system_config
"""

import json
import sys
from pathlib import Path
from typing import Dict, Tuple

try:
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("[ERROR] jsonschema library not installed")
    print("Install with: pip install jsonschema")
    sys.exit(1)


def load_json_file(file_path: Path) -> Dict:
    """Load JSON file and return data."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {file_path}: {e}")
        return None
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return None


def validate_json_file(data_file: Path, schema_file: Path) -> Tuple[bool, str]:
    """Validate JSON data against schema."""
    
    # Load schema
    schema = load_json_file(schema_file)
    if schema is None:
        return False, f"Failed to load schema: {schema_file}"
    
    # Load data
    data = load_json_file(data_file)
    if data is None:
        return False, f"Failed to load data file: {data_file}"
    
    # Validate
    try:
        validate(instance=data, schema=schema)
        return True, "Valid"
    except ValidationError as e:
        return False, f"Validation error: {e.message}\nPath: {' -> '.join(str(p) for p in e.path)}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"


def main():
    """Main validation function."""
    
    # Define files to validate
    validations = [
        {
            "name": "System Configuration",
            "data": Path("knowledge_base/system_config.json"),
            "schema": Path("knowledge_base/schemas/system_config.schema.json")
        },
        {
            "name": "User Requirements",
            "data": Path("knowledge_base/user_requirements.json"),
            "schema": Path("knowledge_base/schemas/user_requirements.schema.json")
        },
        {
            "name": "Design Decisions",
            "data": Path("knowledge_base/design_decisions.json"),
            "schema": Path("knowledge_base/schemas/design_decisions.schema.json")
        }
    ]
    
    print("=" * 60)
    print("Knowledge Base Validation")
    print("=" * 60)
    print()
    
    # Check if running from project root
    if not Path("knowledge_base").exists():
        print("[ERROR] Please run from project root directory")
        print("        Current directory should contain 'knowledge_base/' folder")
        sys.exit(1)
    
    all_valid = True
    results = []
    
    # Validate each file
    for item in validations:
        name = item["name"]
        data_file = item["data"]
        schema_file = item["schema"]
        
        print(f"Validating {name}...")
        print(f"  Data: {data_file}")
        print(f"  Schema: {schema_file}")
        
        # Check if data file exists
        if not data_file.exists():
            print(f"  [SKIP] Data file not found (may not exist yet)")
            print()
            results.append({"name": name, "status": "SKIP", "message": "File not found"})
            continue
        
        # Check if schema exists
        if not schema_file.exists():
            print(f"  [FAIL] Schema file not found: {schema_file}")
            print()
            results.append({"name": name, "status": "FAIL", "message": "Schema not found"})
            all_valid = False
            continue
        
        # Validate
        is_valid, message = validate_json_file(data_file, schema_file)
        
        if is_valid:
            print(f"  [PASS] {message}")
            results.append({"name": name, "status": "PASS", "message": message})
        else:
            print(f"  [FAIL] {message}")
            results.append({"name": name, "status": "FAIL", "message": message})
            all_valid = False
        
        print()
    
    # Summary
    print("=" * 60)
    print("Validation Summary")
    print("=" * 60)
    print()
    
    passed = sum(1 for r in results if r["status"] == "PASS")
    failed = sum(1 for r in results if r["status"] == "FAIL")
    skipped = sum(1 for r in results if r["status"] == "SKIP")
    
    print(f"Total: {len(results)} files")
    print(f"[PASS] Passed: {passed}")
    print(f"[FAIL] Failed: {failed}")
    print(f"[SKIP] Skipped: {skipped}")
    print()
    
    if all_valid:
        print("[SUCCESS] All knowledge base files are valid!")
        return 0
    else:
        print("[WARNING] Some validations failed. Please fix errors above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

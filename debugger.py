# debugger.py

import traceback
import subprocess
import tempfile
import os

# ---------------------- PYTHON SYNTAX CHECK ----------------------
def check_python_syntax(code: str) -> str:
    """
    Checks Python code for syntax errors.
    """
    try:
        compile(code, "<string>", "exec")
        return "No syntax errors found in Python code!"
    except Exception:
        return f"Python Syntax Error:\n{traceback.format_exc()}"

# ---------------------- C++ SYNTAX CHECK -------------------------
def check_cpp_syntax(code: str) -> str:
    """
    Checks C++ code for syntax errors using g++.
    """
    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.cpp', delete=False) as tmp_file:
            tmp_file.write(code)
            tmp_file_path = tmp_file.name

        result = subprocess.run(
            ["g++", "-fsyntax-only", tmp_file_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "No syntax errors found in C++ code!"
        else:
            return f"C++ Syntax Errors:\n{result.stderr}"

    finally:
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)

# ---------------------- JAVA SYNTAX CHECK ------------------------
def check_java_syntax(code: str) -> str:
    """
    Checks Java code for syntax errors using javac.
    """
    try:
        class_name = "TempDebugClass"
        full_code = code if "class" in code else f"public class {class_name} {{\n{code}\n}}"

        with tempfile.NamedTemporaryFile(mode='w', suffix='.java', delete=False) as tmp_file:
            tmp_file.write(full_code)
            tmp_file_path = tmp_file.name

        result = subprocess.run(
            ["javac", tmp_file_path],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "No syntax errors found in Java code!"
        else:
            return f"Java Syntax Errors:\n{result.stderr}"

    finally:
        if os.path.exists(tmp_file_path):
            os.remove(tmp_file_path)

# ---------------------- UNIVERSAL ENTRY --------------------------
def run_syntax_check(code: str, language: str) -> str:
    """
    Unified syntax checker entry point.
    """
    language = language.lower()

    if language == "python":
        return check_python_syntax(code)
    elif language == "cpp" or language == "c++":
        return check_cpp_syntax(code)
    elif language == "java":
        return check_java_syntax(code)
    else:
        return f"Unsupported language: {language}"

from datetime import datetime
import platform

print("=" * 45)
print("       SWE40006 DOCKER PYTHON APP")
print("=" * 45)
print("Application Status : Running successfully")
print(f"Python Version     : {platform.python_version()}")
print(f"System             : {platform.system()}")
print(f"Execution Time     : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 45)
print("Python application completed successfully.")
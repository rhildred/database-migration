import json
import sys
import base64
try:
    json_data = json.load(sys.stdin)
    # Now 'json_data' contains your JSON data as a Python object (e.g., dictionary or list)
    sBase64 = json_data['data']['postgres-password']
    decoded_bytes = base64.b64decode(sBase64)
    decoded_string = decoded_bytes.decode('utf-8')
    print(f"the postgres credentials are postgres/{decoded_string}")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
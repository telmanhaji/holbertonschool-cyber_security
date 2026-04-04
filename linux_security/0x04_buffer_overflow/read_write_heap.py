#!/usr/bin/python3
"""
Task0 PROJECT: BUFFER OVERFLOW
Task 0: Heap Manipulation via /proc filesystem.

This script demonstrates how Linux handles process memory as a file.
By accessing /proc/[PID]/mem, we can bypass standard process 
restrictions (if we have root privileges).
"""

import sys
import os

def print_usage():
    """Prints clear instructions for the team."""
    print("Usage: sudo ./read_write_heap.py pid search_string replace_string")
    print("Example: sudo ./read_write_heap.py 1234 'Holberton' 'Hackerton'")

def main():
    # --- 1. ARGUMENT VALIDATION ---
    # We need exactly 3 arguments (plus the script name).
    if len(sys.argv) != 4:
        print_usage()
        sys.exit(1)

    pid = sys.argv[1]
    search_str = sys.argv[2]
    replace_str = sys.argv[3]

    # Convert strings to bytes immediately. 
    # Python 3 strings are Unicode, but memory is raw BYTES.
    search_bytes = search_str.encode('ascii')
    replace_bytes = replace_str.encode('ascii')

    # --- 2. SECURITY CHECK: BUFFER INTEGRITY ---
    # In C, if we write a longer string than the original, 
    # we cause a 'Buffer Overflow' and corrupt the heap metadata.
    if len(replace_bytes) > len(search_bytes):
        print(f"[!] Warning: Replace string is longer than search string.")
        print(f"    This will likely cause a Segfault in the target process.")
        # Optional: sys.exit(1) if you want to be strictly 'Safety First'

    # --- 3. PARSING /proc/[PID]/maps ---
    # This file is the 'Map' of the process's Virtual Memory.
    try:
        with open(f"/proc/{pid}/maps", "r") as maps_file:
            heap_found = False
            for line in maps_file:
                # We only care about the memory region tagged as [heap]
                if "[heap]" in line:
                    # Line format: 'start-end permissions offset device inode [heap]'
                    # Use .split() without args to catch any whitespace (tabs/spaces)
                    parts = line.split()
                    addr_range = parts[0].split('-')
                    
                    # Convert Hex strings to Python Integers
                    heap_start = int(addr_range[0], 16)
                    heap_end = int(addr_range[1], 16)
                    
                    # Ensure the heap is writable ('w' must be in permissions)
                    if 'w' not in parts[1]:
                        print(f"[!] Error: Heap region at {parts[0]} is not writable.")
                        sys.exit(1)
                        
                    heap_found = True
                    print(f"[*] Found [heap] at: {addr_range[0]} - {addr_range[1]}")
                    break
            
            if not heap_found:
                print(f"[!] Error: Could not locate [heap] for PID {pid}")
                sys.exit(1)

        # --- 4. ACCESSING /proc/[PID]/mem ---
        # This is a special file that maps directly to the process's RAM.
        # 'r+b' = Read and Write in Binary mode.
        with open(f"/proc/{pid}/mem", "r+b") as mem_file:
            # Move the 'cursor' to the start of the heap in RAM
            mem_file.seek(heap_start)
            
            # Read the entire heap into local memory for scanning
            heap_data = mem_file.read(heap_end - heap_start)

            # --- 5. SEARCH AND REPLACE ---
            # Search for the bytes in the heap dump
            offset = heap_data.find(search_bytes)
            
            if offset == -1:
                print(f"[!] Error: '{search_str}' not found in the heap.")
                sys.exit(1)

            print(f"[*] Found '{search_str}' at offset: {hex(heap_start + offset)}")

            # Prepare the payload using your 'Padding' logic.
            # If the new string is shorter, we pad it with Null Bytes (0x00) 
            # to keep the memory 'clean' and valid for C's string functions.
            payload = replace_bytes.ljust(len(search_bytes), b'\x00')

            # Move the file cursor to the EXACT location of the string
            mem_file.seek(heap_start + offset)
            
            # OVERWRITE!
            mem_file.write(payload)
            print(f"[*] Successfully wrote '{replace_str}' to memory.")

    except PermissionError:
        print("[!] Access Denied: You MUST run this script with 'sudo'.")
    except FileNotFoundError:
        print(f"[!] Error: Process {pid} does not exist.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

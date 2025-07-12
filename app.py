#!/usr/bin/env python3

import datetime
import os

def main():
    print("🐳 Hello from Docker!")
    print(f"Current time: {datetime.datetime.now()}")
    print(f"Python version: {os.sys.version}")
    print("This is a simple demo app for GitHub Actions Docker workflow")
    
    # Keep the container running for a bit to show it's working
    print("Application started successfully!")

if __name__ == "__main__":
    main() 
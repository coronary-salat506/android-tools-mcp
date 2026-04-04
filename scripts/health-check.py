#!/usr/bin/env python3
"""
Health check for the Android Tools MCP server.

Usage:
    python health-check.py [PORT]

Exits with 0 if the server is reachable, 1 otherwise.
"""

import http.client
import sys


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 24601

    print(f"Checking MCP server on port {port}...")
    try:
        conn = http.client.HTTPConnection("127.0.0.1", port, timeout=3)
        conn.request("GET", "/sse")
        status = conn.getresponse().status
        conn.close()

        if status == 200:
            print(f"MCP server is running on port {port}")
            sys.exit(0)
        else:
            print(f"MCP server returned unexpected status {status}")
            sys.exit(1)
    except Exception:
        print(f"MCP server is NOT reachable on port {port}")
        print("Make sure Android Studio is running with a project open.")
        sys.exit(1)


if __name__ == "__main__":
    main()

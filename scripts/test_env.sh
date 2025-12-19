#!/bin/bash
echo "Testing..."
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
echo "Project root: $PROJECT_ROOT"
hash=$(echo "test" | md5)
echo "Hash: $hash"
echo "Done."

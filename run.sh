#!/usr/bin/env bash

# If on macOS, ensure that the Homebrew libraries are included in the library path

if [[ "$OSTYPE" == "darwin"* ]]; then
  export DYLD_LIBRARY_PATH="/opt/homebrew/lib:${DYLD_LIBRARY_PATH:-}"
fi
uv run python generate_resume_pdf.py

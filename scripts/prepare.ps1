# Exit immediately if any command fails
$ErrorActionPreference = "Stop"

# Optional: Activate virtual environment if needed
# & "venv\Scripts\Activate.ps1"

Write-Output "Running code formatter (ruff)..."
ruff format .

Write-Output "Running tests (pytest)..."
pytest --rich ./tests

Write-Output "All tasks completed successfully."

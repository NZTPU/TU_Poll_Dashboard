# TU Poll Dashboard

This repository will host the TU Poll Dashboard, a lightweight dashboard for tracking monthly polling results.

## Project layout

- `frontend/`: UI source files.
- `backend/`: Placeholder for future API services.
- `data/`: Stores the monthly Excel data files.
- `scripts/`: Utilities for importing and normalizing data.

## Monthly Excel updates

1. Drop the latest monthly Excel workbook into `data/` using the naming pattern `tu_poll_YYYY_MM.xlsx`.
2. Run the import script to convert the workbook into normalized data for the dashboard:
   ```bash
   python scripts/import_poll_excel.py data/tu_poll_YYYY_MM.xlsx
   ```
3. Commit the updated data outputs alongside any dashboard changes.

The import script is currently a placeholder so we have a defined target for future ingestion logic.

# PDF Invoices to Excel

Reads a folder of invoice PDFs and turns them into one clean Excel spreadsheet, using Python and the Gemini API.
## Example

**Input:** three invoice PDFs

<p align="center">
  <img height="351" src="https://github.com/user-attachments/assets/948e1ffb-185d-4c88-9982-896b73f9ada0" width="32%" alt="Invoice 1">
  <img src="https://github.com/user-attachments/assets/c564a270-c053-4b34-8124-fda3938c4ebc" width="32%" alt="Invoice 2">
  <img src="https://github.com/user-attachments/assets/f224bfdf-3cec-4472-b9a9-3ef4821ff58c" width="32%" alt="Invoice 3">
</p>

<p align="center">⬇</p>

**Output:** one Excel file, `invoices.xlsx`

<p align="center">
  <img width="1118" height="168" alt="image" src="https://github.com/user-attachments/assets/ee1a03bd-0a9c-474a-984b-e5063fe47383" />
</p>



## How to run it

1. Install Python and get a free Gemini API key
2. Download this repo and open a terminal in the folder
3. `pip install -r requirements.txt`
4. Create a `.env` file containing `GEMINI_API_KEY=your_key`
5. Put your PDFs in the `invoices` folder
6. `python pdf_to_csv.py`
7. Your spreadsheet appears as `invoices.xlsx`

Skips non-PDF files and reports any file it can't read.

## Limitations

Works on PDFs with real text and reads the first page only. Scanned PDFs are not supported yet.


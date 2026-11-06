# PDF Invoices to Excel

Reads a folder of invoice PDFs and turns them into one clean Excel spreadsheet, using Python and the Gemini API.
## Example

**Input:** three invoice PDFs

<p align="center">
  <img height="351" src="https://github.com/user-attachments/assets/b4c65096-1286-4e2f-9923-97ddec220400" width="32%" alt="Invoice 1">
  <img src="https://github.com/user-attachments/assets/98f07e26-6883-4cda-a659-6e4aad041132" width="32%" alt="Invoice 2">
  <img src="https://github.com/user-attachments/assets/18d20ee0-756f-46cc-9669-75d7936533bd" width="32%" alt="Invoice 3">
</p>

<p align="center">⬇</p>

**Output:** one Excel file, `invoices.xlsx`

<p align="center">
  <img width="1118" height="168" alt="Screenshot 2026-11-04 100755" src="https://github.com/user-attachments/assets/d65c4944-fe0f-4920-aef3-6e8cd92d06bc" />
</p>



## How to run it

1. Install Python and get a free Gemini API key
2. Download this repo and open a terminal in the folder
3. `pip install -r requirements.txt`
4. Create a `.env` file containing `GEMINI_API_KEY=your_key`
5. Put your PDFs in the `invoices` folder
6. `python pdf_to_excel.py`
7. Your spreadsheet appears as `invoices.xlsx`

Skips non-PDF files and reports any file it can't read.

## Limitations

Works on PDFs with real text and reads the first page only. Scanned PDFs are not supported yet.


import requests

url = "http://127.0.0.1:8000/get-lab-tests"
filepath = r"C:\Users\manha\OneDrive\Desktop\New folder\lab_reports_samples\lbmaske\1161458 GUR-0425-PA-0054886_Q-112714RASMITA_250427_1433@F.pdf_page_32.png"

with open(filepath, "rb") as f:
    files = {"file": f}
    resp = requests.post(url, files=files)
    print(resp.status_code)
    print(resp.json())

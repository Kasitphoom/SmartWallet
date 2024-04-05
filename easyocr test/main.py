# import easyocr

# image = 'test_image/EfB3wE7VAAA1VX6.jpg'
# reader = easyocr.Reader(['en', 'th'], gpu=False)
# result = reader.readtext(image, detail=0)
# for text in result:
#     print(text)

import json
import requests

url = "https://ocr.asprise.com/api/v1/receipt"
image = 'test_image/EfB3wE7VAAA1VX6.jpg'

# res = requests.post(
#     url,
#     data={
#         'api_key': 'TEST',
#         'recognizer': 'auto',
#         'ref_no': 'oct_python_123'
#     },
#     files={
#         'file': open(image, 'rb')
#     }
# )

# with open('test.json', 'w') as f:
#     json.dump(res.json(), f, indent=4)

with open('test.json', 'r') as f:
    data = json.load(f)

for data in data['receipts']:
    for item in data['items']:
        print(item['description'], item['amount'])
# app/utils/ocr.py
# OCR extraction using PaddleOCR
# run: python -m app.utils.ocr

from paddleocr import PaddleOCR

def extract_text_from_image(pdf_path: str) -> str:
    ocr = PaddleOCR(use_textline_orientation=True, lang='en')
    result = ocr.predict(pdf_path)
    data = result[0]
    text = ''
    for t in data['rec_texts']:
        if data['rec_scores'][data['rec_texts'].index(t)] > 0.8:
            text += t + '\n'
    # print('\n\n OCR Results with Confidence Scores:\n')
    # Loop through text + scores
    # for text, score in zip(data['rec_texts'], data['rec_scores']):
        # print(f"{text} (Confidence: {score:.2f})")
    return text

if __name__ == "__main__":
    text = extract_text_from_image('aadhar2.jpg')
    print(text)

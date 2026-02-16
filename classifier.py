from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="valhalla/distilbart-mnli-12-1"
)

LABELS = ["Real News", "Fake News"]

def classify_text(text):
    result = classifier(text, LABELS)

    label = result["labels"][0]
    confidence = round(result["scores"][0], 3)

    explanation = (
        f"The model predicts this is '{label}' "
        f"with {confidence*100}% confidence."
    )

    return label, confidence, explanation
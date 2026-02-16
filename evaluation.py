import pandas as pd
import time
from classifier import classify_text
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

data = pd.read_csv("data/fake_news.csv")

true_labels = []
pred_labels = []
errors = []

start_time = time.time()

for i, row in data.iterrows():
    print(f"Processing sample {i+1}/{len(data)}")

    label, confidence, _ = classify_text(row["text"])

    pred_labels.append(label)
    true_labels.append(row["label"])

    if label != row["label"]:
        errors.append({
            "text": row["text"],
            "true_label": row["label"],
            "predicted": label,
            "confidence": confidence
        })

end_time = time.time()

print("\n=== Classification Report ===")
print(classification_report(true_labels, pred_labels))

print("\n=== Confusion Matrix ===")
print(confusion_matrix(true_labels, pred_labels))

accuracy = accuracy_score(true_labels, pred_labels)

print("\n=== Summary ===")
print(f"Accuracy: {accuracy}")
print(f"Total Time: {round(end_time-start_time,2)} sec")
print(f"Avg Time per Sample: {round((end_time-start_time)/len(data),2)} sec")

if errors:
    pd.DataFrame(errors).to_csv("misclassified_samples.csv", index=False)
    print("\nMisclassified samples saved.")
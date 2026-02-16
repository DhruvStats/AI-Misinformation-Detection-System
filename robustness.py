from classifier import classify_text

tests = [
    "NASA confirms discovery of water on Mars.",
    "Nassa confims discovry of wator on Mars.",
    "Scientists report that water has been detected on Mars."
]

results = []

for text in tests:
    label, confidence, _ = classify_text(text)
    results.append((text, label, confidence))

print("\n=== Robustness Results ===")
for r in results:
    print(r)
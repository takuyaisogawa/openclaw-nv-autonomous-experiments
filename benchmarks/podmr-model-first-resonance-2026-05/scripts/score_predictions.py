#!/usr/bin/env python3
import csv
import collections
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
LABELS = {r["case_id"]: r["resonance_label"] for r in csv.DictReader((ROOT / "labels" / "gold_labels.csv").open(encoding="utf-8-sig"))}


def summarize(rows):
    tp = tn = fp = fn = 0
    for row in rows:
        gold = row.get("gold_label") or LABELS[row["case_id"]]
        pred = row["prediction"]
        if gold == "present" and pred == "resonance_present":
            tp += 1
        elif gold == "absent" and pred == "resonance_absent":
            tn += 1
        elif gold == "absent" and pred == "resonance_present":
            fp += 1
        elif gold == "present" and pred == "resonance_absent":
            fn += 1
    n = tp + tn + fp + fn
    return {"n": n, "tp": tp, "tn": tn, "fp": fp, "fn": fn, "accuracy": (tp + tn) / n}


def score(path):
    rows = list(csv.DictReader(path.open(encoding="utf-8-sig")))
    print(path.relative_to(ROOT))
    groups = collections.defaultdict(list)
    for row in rows:
        groups[row.get("context_id", path.parent.name)].append(row)
    for name in sorted(groups):
        print(name, summarize(groups[name]))


for path in sorted((ROOT / "results").rglob("joined_predictions.csv")):
    score(path)

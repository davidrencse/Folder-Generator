import csv
import os
import random
import re


def sanitize_name(name: str) -> str:
    name = name.strip()
    name = re.sub(r"\s+", " ", name)
    name = re.sub(r"[^A-Za-z0-9 _-]", "", name)
    return name if name else "untitled"


def load_words_from_csv(csv_path: str):
    words = []
    with open(csv_path, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no headers.")
        if "word" not in reader.fieldnames:
            raise ValueError("CSV must contain a header named 'word'.")

        for row in reader:
            w = (row.get("word") or "").strip()
            if w:
                words.append(w)

    seen = set()
    deduped = []
    for w in words:
        key = w.lower()
        if key not in seen:
            seen.add(key)
            deduped.append(w)
    return deduped


def generate_folder_names(words, count: int):
    if not words:
        raise ValueError("No words loaded from CSV.")
    if count <= 0:
        raise ValueError("Folder count must be positive.")

    suffixes = [
        "notes", "labs", "assignments", "design", "spec", "docs", "scratch",
        "drafts", "revA", "revB", "v1", "v2", "archive", "refs", "bench",
        "diagrams", "tests", "build", "release"
    ]

    used = set()
    results = []

    while len(results) < count:
        style = random.randint(1, 3)

        if style == 1:
            base = random.choice(words)
            raw = f"{base}_{random.randint(1, 999):03d}"
        elif style == 2:
            w1 = random.choice(words)
            w2 = random.choice(words)
            raw = f"{w1}_{w2}_{random.choice(suffixes)}_{random.randint(1, 999):03d}"
        else:
            base = random.choice(words)
            raw = f"{base}_{random.choice(suffixes)}_{random.randint(1, 999):03d}"

        name = sanitize_name(raw)

        if name.upper() in ("CON", "PRN", "AUX", "NUL"):
            continue

        key = name.lower()
        if key in used:
            continue

        used.add(key)
        results.append(name)

    return results


def create_folders(target_dir: str, folder_names):
    os.makedirs(target_dir, exist_ok=True)

    created = 0
    for name in folder_names:
        path = os.path.join(target_dir, name)
        if os.path.exists(path):
            continue
        os.mkdir(path)
        created += 1
    return created


def run_topic(csv_file: str, topic_label: str):
    print(f"Generating folder set for {topic_label}...")

    base_dir = input(r"Base directory (e.g., E:\comp architecture): ").strip().strip('"')
    if not base_dir:
        print("No base directory provided.")
        return

    # Always create inside an "output" folder
    output_dir = os.path.join(base_dir, "output")

    count_str = input("How many folders? (default 88): ").strip()
    folder_count = 88
    if count_str:
        try:
            folder_count = int(count_str)
        except ValueError:
            print("Invalid number; using default 88.")
            folder_count = 88

    words = load_words_from_csv(csv_file)
    names = generate_folder_names(words, folder_count)
    created = create_folders(output_dir, names)

    print(f"Done. Created {created} folders in: {output_dir}")
    if created < folder_count:
        print("Some names already existed and were skipped.")


def main():
    print("Choose a topic below to generate folders from:")
    print("1. Computer Architecture")
    print("2. Object Oriented Programming")
    print("3. Operating Systems")
    print("4. Data Structures")
    print("5. Computer Networking")

    user_input = input("Enter a topic number: ").strip()

    match user_input:
        case "1":
            run_topic("computer_architecture_words.csv", "Computer Architecture")
        case "2":
            run_topic("oop_words.csv", "Object Oriented Programming")
        case "3":
            run_topic("operating_systems_words.csv", "Operating Systems")
        case "4":
            run_topic("data_structures_words.csv", "Data Structures")
        case "5":
            run_topic("computer_networking_words.csv", "Computer Networking")
        case _:
            print("Invalid selection. Choose 1-5.")


if __name__ == "__main__":
    main()

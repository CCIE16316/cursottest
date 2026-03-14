import re
from pathlib import Path

def show_matches(text, patterns, col_width=56):
    for name, pattern in patterns.items():
        matches = [m.group() for m in re.finditer(pattern, text)]
        print("\n" + "=" * (col_width + 12))
        print(f"  {name}")
        print("=" * (col_width + 12))
        if not matches:
            print("  (无匹配)")
            continue
        sep = "+------+" + "-" * (col_width + 2) + "+"
        print(sep)
        print("| {:^4} | {:<{w}} |".format("序号", "匹配内容", w=col_width))
        print(sep)
        for i, s in enumerate(matches, 1):
            one = s.replace("\n", " ").replace("\r", " ").strip()
            if len(one) > col_width:
                one = one[: col_width - 3] + "..."
            print("| {:^4} | {:<{w}} |".format(i, one, w=col_width))
        print(sep)
        print(f"  共 {len(matches)} 处")

base_dir = Path(__file__).parent
file_path = base_dir / "content.txt"
text = file_path.read_text(encoding="utf-8", errors="ignore")

patterns = {
   # "non_ascii": r"[^\x00-\x7F]+",
    "long_alnum": r"\b[A-Za-z0-9]{10,}\b",
   # "suspicious_token": r"\b[A-Za-z0-9+_/\-]{10,}={0,2}\b",
   # "base64_like": r"\b(?:[A-Za-z0-9+/]{4}){3,}(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?\b",
}

show_matches(text, patterns)

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "AGENTS.md",
    "ROADMAP.md",
    "ARCHITECTURE.md",
    "README.md",
    "docs/index.md",
    "skills",
    "evals",
    "profiles",
)


def main() -> None:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]

    if missing:
        raise SystemExit(
            "Missing required repository paths:\n" + "\n".join(f"- {path}" for path in missing)
        )

    print("repository structure: OK")


if __name__ == "__main__":
    main()

"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (at most 280 characters) to entry.txt in the
output directory, for the make.fun bounty
u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363.

Deterministic: no network, no randomness, no time dependence.
The same text is written on every run.
"""

import os

TEXT = (
    "The rice cooker clicked at six and the whole house filled with steam, "
    "and for one breath I was seven again, barefoot in my grandmother's "
    "kitchen while she hummed and the windows fogged."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"Wrote {len(TEXT)} characters to {path}")


if __name__ == "__main__":
    main()

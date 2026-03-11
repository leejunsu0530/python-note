"""
README.md에 docs 내의 파일들의 목차를 만들어주는 스크립트입니다.
"""

from pathlib import Path
from typing import LiteralString, Callable
from datetime import datetime

README_PATH = Path(__file__).parent / "README.md"
DOCS_PATH = Path(__file__).parent / "docs"

docs_files = sorted(DOCS_PATH.glob("*.md"))

TMPL = """# python-note

last updated: {time}

<!-- TOC -->
{toc}
<!-- /TOC -->"""


def make_toc(sort_: Callable[[list[Path]], list[Path]]) -> LiteralString:
    toc = []

    for file in sort_(docs_files):
        name = file.stem
        toc.append(f"- [{name}](./docs/{file.name})")
    return "\n".join(toc)


if __name__ == "__main__":
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"found docs files:\n{docs_files}")
    TOC = make_toc(sorted)
    print(f"made TOC:\n{TOC}")
    with README_PATH.open("w", encoding='utf-8') as f:
        f.write(TMPL.format(toc=TOC, time=current_time))
        print(f"README.md updated at {current_time}")

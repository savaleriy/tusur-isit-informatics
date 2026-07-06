import shutil
from pathlib import Path


def on_post_build(config, **kwargs):
    docs_dir = Path(config["docs_dir"])
    site_dir = Path(config["site_dir"])
    for data_dir in docs_dir.rglob("data"):
        rel = data_dir.relative_to(docs_dir)
        dest = site_dir / rel
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(data_dir, dest)

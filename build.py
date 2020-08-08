#!/usr/bin/env python3
import argparse
import jinja2
import sys
import yaml

from datetime import date


def parse_args():
    parser = argparse.ArgumentParser(description="Build taskqueues.com")
    parser.add_argument(
        "--config",
        type=argparse.FileType("rb"),
        help="the config yaml",
    )
    parser.add_argument(
        "output",
        type=argparse.FileType("w", encoding="utf-8"),
        help="the output file",
    )
    return parser.parse_args()


def main():
    arguments = parse_args()
    config = yaml.full_load(arguments.config)
    templates = jinja2.Environment(loader=jinja2.FileSystemLoader("."))
    template = templates.get_template("template.html")
    arguments.output.write(template.render(
        now=date.today().isoformat(),
        **config,
    ))
    return 0


if __name__ == "__main__":
    sys.exit(main())

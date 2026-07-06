"""MathJax 3 integration via MkDocs hooks.

- on_config: injects MathJax CDN into extra_javascript
- on_post_page: injects inline MathJax config into <head>

Works with pymdownx.arithmatex (generic: true) which wraps
$...$ and $$...$$ in \(...\) and \[...\] inside .arithmatex elements.
"""

MATHJAX_CDN = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"

BS = "\\"   # single literal backslash

# JS delimiters: \\\( and \\) etc. in Python produce \( and \) in browser JS.
# Using single quotes to avoid quote-escaping headaches.
CONFIG = (
    "window.MathJax = {\n"
    "  tex: {\n"
    "    inlineMath: [['" + BS + BS + "(" + "', '" + BS + BS + ")" + "'], ['$', '$']],\n"
    "    displayMath: [['" + BS + BS + "[" + "', '" + BS + BS + "]" + "'], ['$$', '$$']],\n"
    "    processEscapes: true,\n"
    "    processEnvironments: true,\n"
    "  },\n"
    "  options: {\n"
    '    processHtmlClass: "arithmatex",\n'
    "  },\n"
    "};\n"
    "document$.subscribe(() => {\n"
    "  MathJax.startup.output.clearCache();\n"
    "  MathJax.typesetClear();\n"
    "  MathJax.texReset();\n"
    "  MathJax.typesetPromise();\n"
    "});\n"
)


def on_config(config, **kwargs):
    js = config.get("extra_javascript") or []
    if MATHJAX_CDN not in js:
        js.append(MATHJAX_CDN)
    config["extra_javascript"] = js
    return config


def on_post_page(output, page, config, **kwargs):
    # Use string replacement (not re.sub) to preserve backslashes
    tag = "<script>" + CONFIG + "</script>"
    return output.replace("</head>", tag + "\n</head>", 1)

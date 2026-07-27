# Undergraves

Command-line web crawler for domain mapping and endpoint discovery. Performs breadth-first search (BFS) restricted strictly to the target's base domain, collecting active URLs and page titles in real time.

---

## Installation

### Via PyPI
```bash
pip install undergraves

```

### Local Installation (Development)

```bash
git clone https://github.com/GabrielDillDev/undergraves.git
cd undergraves
pip install -e .

```

---

## Usage

```bash
undergraves <URL> [LEVEL]

```

If no scan level is provided, **T3** is used by default.

### Scan Levels

| Level | Page Limit |
| --- | --- |
| **T1** | 50 |
| **T2** | 200 |
| **T3** | 500 *(Default)* |
| **T4** | 2000 |
| **T5** | Unlimited |

### Examples

Default scan (T3 - 500 pages):

```bash
undergraves https://example.com

```

Quick scan (T1 - 50 pages):

```bash
undergraves https://example.com T1

```

Full scan (T5 - Runs until queue is empty):

```bash
undergraves https://example.com T5

```

---

## Output Files

Upon completion, the tool automatically generates two files in the current working directory:

* `resultado.json`: Array of objects containing `url` and `title`.
* `resultado.csv`: Table formatted with `URL` and `Title` columns.

---

## Testing

Run the unit test suite using `pytest`:

```bash
pip install pytest
pytest

```

---

## License

MIT

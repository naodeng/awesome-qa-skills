# Output Format Options

This skill **defaults to Markdown**. To get **Excel**, **CSV**, or **JSON**, add a short instruction at the **end of your request**.

---

## 1. Markdown (default)

The AI follows the functional-testing Standard-version Markdown template (test plan, test cases, etc.).

---

## 2. Excel format

**How to request:** e.g. “Please also output the test cases / test plan as **tab-separated values** so I can paste them into Excel.”

**Conventions:** First row = header; columns separated by **Tab**; paste into Excel to split columns.

---

## 3. CSV format

**How to request:** e.g. “Please output the result as **CSV** (comma-separated, header row first).”

**Conventions:** Header row first; comma `,` between columns; wrap cells containing comma or newline in `"`.

---

## 4. JSON format

**How to request:** e.g. “Please output the test cases / plan as **JSON**.”

**Conventions:** Valid JSON; table-like content as array of objects with fields consistent with the Markdown (e.g. id, title, priority, preconditions, steps, expectedResult).

---

See repo `_output-formats-template-en.md` for generic examples.

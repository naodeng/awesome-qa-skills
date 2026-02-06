# Output Format Options (English Template)

This skill **defaults to Markdown** output. To get **Excel**, **CSV**, or **JSON**, add a short instruction at the **end of your request**.

---

## 1. Markdown (default)

If you do not specify a format, the AI will follow the Standard-version Markdown template for that testing type (good for reading and version control).

---

## 2. Excel format

**How to request:** Add one of the following at the end of your request:

- “Please also output the test cases / checklist / report as **tab-separated values** so I can paste them into Excel.”
- “Output the table in **tab-separated form** for pasting into Excel.”

**Conventions:**

- First row is the header (column names).
- Columns are separated by **Tab**.
- Copy the block and paste into Excel; columns will align.

**Example (test case table):**

```
Case ID	Title	Priority	Preconditions	Steps	Expected Result
TC-01	Login with valid account	P0	App installed	1. Enter credentials 2. Click Login	Land on home
TC-02	Login with wrong password	P1	App installed	1. Enter wrong password 2. Click Login	Error message shown
```

---

## 3. CSV format

**How to request:** Add at the end, for example:

- “Please output the result as **CSV** (comma-separated, header row first).”
- “Output as **CSV** for import into our tool.”

**Conventions:**

- First row is the header.
- Columns separated by comma `,`.
- If a cell contains a comma or newline, wrap the cell in double quotes `"`.

**Example:**

```csv
Case ID,Title,Priority,Preconditions,Steps,Expected Result
TC-01,Login with valid account,P0,App installed,"1. Enter credentials 2. Click Login",Land on home
TC-02,Login with wrong password,P1,App installed,"1. Enter wrong password 2. Click Login",Error message shown
```

---

## 4. JSON format

**How to request:** Add at the end, for example:

- “Please output the above as **JSON**.”
- “Output as a **JSON array** for programmatic use.”

**Conventions:**

- Valid JSON syntax.
- For table-like content, use an array of objects, e.g. test cases: `[{ "id": "TC-01", "title": "...", "priority": "P0", ... }, ...]`.
- Field names should match the structure implied by the Standard-version Markdown output (or say “use JSON and keep the same information as in the Markdown”).

**Example (test case list):**

```json
{
  "testCases": [
    {
      "id": "TC-01",
      "title": "Login with valid account",
      "priority": "P0",
      "preconditions": "App installed",
      "steps": "1. Enter credentials 2. Click Login",
      "expectedResult": "Land on home"
    },
    {
      "id": "TC-02",
      "title": "Login with wrong password",
      "priority": "P1",
      "preconditions": "App installed",
      "steps": "1. Enter wrong password 2. Click Login",
      "expectedResult": "Error message shown"
    }
  ]
}
```

---

Append the relevant “How to request” line to your prompt to get the desired output format.

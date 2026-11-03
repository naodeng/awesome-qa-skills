#!/usr/bin/env python3
"""One fixture's exact decision rows; no engine or model is implemented here."""
import os,sys
EXPECTED = {'R1': 'NO_GO', 'R2': 'READY'}

def grade(text,exit_code):
    if str(exit_code) != '0': raise ValueError('engine did not exit successfully')
    found={key:[] for key in EXPECTED}
    for line in text.splitlines():
        if '|' not in line:continue
        cells=[c.strip() for c in line.strip().strip('|').split('|')]
        # Release gate boards also contain R1/R2 rows. They have additional
        # columns, while the machine-readable decision rows have exactly 3.
        if len(cells)==3 and cells[0] in found:
            found[cells[0]].append((cells[1], '|'.join(cells[2:]).strip()))
    for key,expected in EXPECTED.items():
        rows=found[key]
        if len(rows)!=1 or rows[0][0]!=expected or not rows[0][1]:
            raise ValueError('Missing, duplicate, incorrect, or unsourced decision: '+key)

if __name__=='__main__':
    try:grade(os.environ.get('EVAL_FINAL_MESSAGE',''),os.environ.get('EVAL_EXIT_CODE',''))
    except ValueError as exc:
        print(str(exc),file=sys.stderr);sys.exit(1)
    print('Exact fixture decisions passed; semantic explanation remains separately reviewable')

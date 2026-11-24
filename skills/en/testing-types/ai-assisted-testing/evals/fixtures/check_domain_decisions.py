#!/usr/bin/env python3
"""Deterministic final-artifact checks; no model calls or execution engine."""
import json
import os
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

ORACLE = {'decisions': {'AIA-01': 'ACCEPTED', 'AIA-02': 'DRAFT', 'AIA-03': 'UNSUPPORTED'}, 'calculations': {'human_baseline_minutes': 60, 'generate_minutes': 10, 'review_minutes': 25, 'rework_minutes': 35, 'acceptance_minutes': 10, 'total_minutes': 80, 'token_cost': 'UNSUPPORTED', 'defects_found': 1, 'rework_count': 1, 'false_green_count': 1}, 'required_details': ['80', '60', 'token_cost', 'UNSUPPORTED']}

def clean(value):
    value = value.strip()
    for marker in ('**', '`'):
        if value.startswith(marker) and value.endswith(marker):
            value = value[len(marker):-len(marker)].strip()
    return value

def tables(text):
    groups, group = [], []
    fence = False
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith('```') or stripped.startswith('~~~'):
            fence = not fence
        is_row = not fence and '|' in stripped
        if is_row:
            cells = [clean(c) for c in re.split(r'(?<!\\)\|', stripped.strip('|'))]
            group.append(cells)
        elif group:
            groups.append(group)
            group = []
    if group:
        groups.append(group)
    return groups

def require_table(groups, key, value):
    selected = [g for g in groups if len(g[0]) >= 3 and g[0][0].upper() == key and g[0][1].upper() == value]
    if len(selected) != 1:
        raise ValueError(f'exactly one {key}/{value} table is required')
    rows = []
    for cells in selected[0][1:]:
        if cells and all(re.fullmatch(r':?-{3,}:?', c.replace(' ','')) for c in cells):
            continue
        if len(cells) != 3:
            raise ValueError('every result row needs three cells')
        if not cells[2] or cells[2] in ('-', '--', '?', 'TODO'):
            raise ValueError('evidence/unit cell must be nonempty')
        rows.append(cells)
    return rows

def check(text, oracle):
    groups = tables(text)
    rows = require_table(groups, 'ID', 'DECISION')
    actual = {}
    for key, decision, evidence in rows:
        if key in actual:
            raise ValueError(f'duplicate decision ID: {key}')
        actual[key] = decision
    if set(actual) != set(oracle['decisions']):
        raise ValueError('decision IDs do not exactly match the fixture')
    for key, decision in oracle['decisions'].items():
        if actual[key] != decision:
            raise ValueError(f'wrong decision for {key}: {actual[key]}')
    calculations = oracle.get('calculations', {})
    if calculations:
        values = {}
        for key, value, evidence in require_table(groups, 'METRIC', 'VALUE'):
            if key in values:
                raise ValueError(f'duplicate metric: {key}')
            expected = calculations.get(key)
            if isinstance(expected, str):
                values[key] = value
            else:
                try:
                    numeric = Decimal(value)
                except InvalidOperation:
                    raise ValueError(f'invalid numeric value: {key}')
                if not numeric.is_finite():
                    raise ValueError(f'non-finite metric: {key}')
                values[key] = numeric
        if set(values) != set(calculations):
            raise ValueError('metric keys do not exactly match the fixture')
        for key, value in calculations.items():
            expected = value if isinstance(value, str) else Decimal(str(value))
            if values[key] != expected:
                raise ValueError(f'wrong metric result: {key}')
    for item in oracle.get('required_details', []):
        if item not in text:
            raise ValueError(f'missing required detail: {item}')

def main():
    try:
        if os.environ.get('EVAL_EXIT_CODE','') != '0':
            raise ValueError('agent exit code is not zero')
        oracle = ORACLE
        check(os.environ.get('EVAL_FINAL_MESSAGE',''), oracle)
    except (ValueError, OSError, KeyError, json.JSONDecodeError) as error:
        print(str(error), file=sys.stderr)
        return 1
    print('domain artifact decisions and evidence cells are valid')
    return 0

if __name__ == '__main__':
    sys.exit(main())

# Fake-Test Patterns

| Pattern | Why it is unreliable | Review signal | Repair direction |
| --- | --- | --- | --- |
| No assertion | A broken implementation can pass | Calls a method with no `assert` / `expect` | Assert an observable business result |
| Tautology | It always passes | `expect(true).toBe(true)` | Assert a meaningful outcome |
| Self-comparison | It validates nothing independently | `expect(result).toEqual(result)` | Use an independent, explainable expectation |
| Weak assertion | Business result remains unknown | `not.toBeNull()` is the only check | Assert key values, structure, or errors |
| Status-only API check | HTTP success is not business correctness | Only `status === 200` | Assert contract and business postcondition |
| Subject mocked | Real production logic never runs | The service/module under test is mocked | Mock external boundaries only |
| Mock-call-only check | It checks internals, not behavior | `verify(mock).called()` is the only check | Also assert output, state, or side effect |
| Swallowed failure | An error becomes a green test | Empty `catch` or unbounded retry | Assert the error; bound and observe retries |
| No business postcondition | UI navigation does not prove success | Click + URL/existence only | Assert user-visible or persisted outcome |
| Coverage padding | Code runs without behavior proof | Function invoked only for coverage | Add assertions derived from a fault model |
| Meaningless snapshot | Large output hides semantic changes | Broad snapshot with no focused checks | Assert stable, business-critical fields |

Ask first: if the subject were removed or broken, would the test fail? If that cannot be demonstrated, report risk rather than coverage.

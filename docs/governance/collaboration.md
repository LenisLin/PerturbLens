# Collaboration And Approval

## Roles

### Human Lead

- owns benchmark scope, release sign-off, and final wording choices
- approves changes to task definitions, denominators, and figure claims

### Codex

- owns implementation, doc updates, verification commands, and manifest-aware
  delivery
- keeps benchmark semantics aligned with the domain contracts linked from
  `docs/README.md`

### Review Model

- reviews semantic consistency, metric logic, and wording drift against the
  contract docs and audited outputs

## Review Flow

1. Identify the controlling contract, proposed changes, and observable checks.
2. Obtain Human Lead approval for semantic changes before implementing them.
3. Implement the approved scope and preserve unrelated working-tree changes.
4. Run the relevant checks and distinguish verified results from remaining
   limitations.
5. Review correctness, risk, and contract alignment before release sign-off.

Publication requires authorization. A document migration does not authorize
publishing unrelated local implementation work or modifying historical data.

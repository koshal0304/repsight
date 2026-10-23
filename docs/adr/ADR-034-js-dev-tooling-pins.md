# ADR-034 — JavaScript dev tooling pins: TypeScript, ESLint, Jest, Prettier

| Field | Value |
|---|---|
| Status | Proposed |
| Date | 2026-10-23 |
| Drafted by | Claude Code (E0-T02) |
| Decides | Tech lead (HITL-09) |
| Scope | Dev-only npm tools at the workspace root, the policy for dependency build scripts, and one dev-tree licence outside the GR-11 list. Mobile app libraries stay with ADR-001 and ADR-006 |

## Context

E0-T02 adds the repository's first npm dependencies. 05 §5.1 names the tools (ESLint flat config with typescript-eslint strict type-checked rules, Prettier), and 02 §12.3–§12.4 name Jest and `tsc --noEmit`. Only TypeScript has a pinned version: `~6.0.3` (canon §10.1, 05 §4.1). GR-17 and NFR-038 require exact pins. 05 §5.6 requires an ADR for a new dependency that is not on an allowlist, and no allowlist exists yet (E0-T05 adds the SDK allowlist).

## Decision

**Selection rule:** the same as ADR-033. Use the newest stable release published at least 14 days before the pin date (2026-10-23, so on or before 2026-10-09), within the canon range where one exists.

| Package | Pin | Released | Why |
|---|---|---|---|
| `typescript` | **6.0.3** | 2026-04-16 | Canon `~6.0.3`; the only 6.0.x release at or above 6.0.3. TypeScript 7 has no programmatic API (canon §10.5) |
| `eslint` | **10.12.0** | 2026-10-02 | The current release line. 9.x reached end of life on 2026-08-06 ([eslint.org/version-support](https://eslint.org/version-support/)) |
| `@eslint/js` | 10.0.1 | 2026-02-06 | ESLint's recommended rules; the newest 10.x |
| `typescript-eslint` | **8.71.1** | 2026-10-05 | Strict type-checked rules (05 §5.1); supports TypeScript `<6.1.0` and ESLint 10 |
| `@eslint-community/eslint-plugin-eslint-comments` | 4.8.1 | 2026-09-12 | `require-description`: every disable comment states why, which carries out 05 §5.1 "no `any` without a `// reason:` comment" (`any` itself is an error) |
| `jest`, `@jest/globals` | **30.5.2** | 2026-09-18 | The same major as `jest-expo` 58.0.12 (`babel-jest` ^30), so the mobile app can share it |
| `ts-jest` | 29.4.14 | 2026-09-25 | Runs the TypeScript tests; supports TypeScript `<7` and Jest 30 |
| `prettier` | **3.9.9** | 2026-09-23 | Formatter (05 §5.1); runs with its defaults plus `.editorconfig`, so there is no options file |

All of them are root `devDependencies`, so each version is written once. `@repsight/config` holds the shared `tsconfig.base.json` and `eslint.config.js`; each package depends on it through `workspace:*`.

**Dependency build scripts.** pnpm 12 fails an install while any dependency has a build script that has not been reviewed (`strictDepBuilds`, on by default). Two Jest dependencies have one. Both ship prebuilt native bindings as optional dependencies, so `pnpm-workspace.yaml` denies both scripts (`allowBuilds: false`):

| Package | Pulled in by | What its script does |
|---|---|---|
| `@parcel/watcher` 2.6.0 | `jest-haste-map` | `install` compiles from source, and only when `npm_config_build_from_source=true` |
| `unrs-resolver` 1.12.2 | `jest-resolve` | `postinstall` downloads the native binding when the optional dependency is missing |

**Licences.** `pnpm licenses list` covers the whole tree: 359 package versions, all dev-only, and none ship in the app or the API image.

| Licence | Package versions |
|---|---|
| MIT | 284 |
| ISC | 29 |
| Apache-2.0 | 16 |
| BSD-3-Clause / BSD-2-Clause | 11 / 8 |
| BlueOak-1.0.0 | 8 |
| MIT OR CC0-1.0 | 2 (`type-fest`) |
| CC-BY-4.0 | 1 (`caniuse-lite`) |

There is no AGPL, SSPL, RSAL or non-commercial licence. **BlueOak-1.0.0 is not on the GR-11 list**, and GR-11 says "anything else needs an ADR". It covers `glob` 13.0.6, `jackspeak` 3.4.3, `lru-cache` 11.5.3, `minimatch` 10.2.6, `minipass` 7.1.3, `package-json-from-dist` 1.0.1 and `path-scurry` 1.11.1 and 2.0.2. ESLint and Jest both depend on these packages. The Blue Oak Model License 1.0.0 is a permissive licence and has been OSI-approved since 2024-01-19 ([OSI](https://opensource.org/license/blue-oak-model-license)). **Accepting this ADR accepts BlueOak-1.0.0 for dev tooling.**

## Alternatives

1. **ESLint 9.39.5.** It matches `eslint-config-expo` 58.0.4, whose `eslint-plugin-react` and `eslint-plugin-import` declare ESLint ≤9. Rejected because 9.x has been end of life since 2026-08-06 and gets no security fixes.
2. **Babel or SWC instead of ts-jest.** `babel-jest` mirrors how Metro compiles the engine on the phone, but it needs a preset plus inline Babel config. SWC adds a native binary. ts-jest is one dependency and one config line, and either alternative can replace it later without changing the tests.
3. **`@types/jest` globals instead of `@jest/globals` imports.** Rejected because `@jest/globals` is released with Jest, so its types always match the runner. Under TypeScript 6, global types also need extra `types` config.
4. **Tool versions declared in each package, or through a pnpm catalog.** Rejected for now because one root list is the least to keep in step. Revisit if a package needs a different version, for example `apps/mobile` with `jest-expo`.
5. **The newest releases** (`eslint` 10.13.0, `typescript-eslint` 8.72.0, `ts-jest` 29.4.15, `prettier` 3.9.10). Rejected because each was less than 14 days old at pin time.

## Consequences

- **E2 must choose the mobile lint stack.** `eslint-plugin-react` 7.37.5 and `eslint-plugin-import` 2.32.0 (both used by `eslint-config-expo` 58.0.4) declare ESLint ≤9, and `eslint-plugin-react-native-a11y` 3.5.1 declares ESLint ≤8. `eslint-plugin-react-hooks` 7.1.1 supports ESLint 10. E2 either uses plugins that support ESLint 10 or runs a separate ESLint 9 in `apps/mobile`, with an ADR either way.
- The React Hooks and React Native accessibility rules from 05 §5.1 arrive with `apps/mobile` (E2-T01). The ESLint security rules arrive with SAST in E0-T06 (02 §10.13).
- `skipLibCheck` is on because Jest's type declarations reference Node types, and TypeScript 6 no longer loads `@types/*` automatically. The shared base sets `lib` to `es2024` only, so package source sees no DOM or Node globals. For example, `console` in engine source fails the type check, which suits code that runs on Hermes.
- A dependency that adds a new build script fails `pnpm install` until it is reviewed and listed under `allowBuilds`.
- Bumping any pin here needs a new ADR (02 §3.10) and an updated lockfile. `tools/ci/tests/test_workspace.py::test_nfr_038_npm_dependencies_are_pinned_exactly` fails on any version range.
- 02 Appendix C needs a row for ADR-034, added in a docs PR for the tech lead (05 §10.4 step 2).

## Evidence

Run on 2026-10-23, macOS arm64, Node 22.13.1, pnpm 12.10.1, uv 0.12.24:

- Release dates and peer ranges came from `npm view <package> time` and `npm view <package>@<version> peerDependencies`.
- `pnpm check:all` passed: ESLint and Prettier on 3 packages, `tsc` on 2, 2 Jest tests and 5 pytest tests.
- Each deliberate violation failed:
  - `any` with no disable comment (`no-explicit-any`)
  - a disable comment with no reason (`require-description`)
  - an unawaited promise (`no-floating-promises`, which shows type-aware linting works)
  - unchecked array indexing (TS2322)
  - `console` in engine source (TS2584)
  - a caret range in `package.json` (`test_nfr_038_npm_dependencies_are_pinned_exactly`)
- `pnpm licenses list --json` gave the counts above.

## Rollback plan

Revert the E0-T02 commits. They hold no data or schema, and the repository goes back to having no npm dependencies.

## Links

05 §4.1, §5.1, §5.6, §10.4 · 02 §3.10, §10.13, §12.3, §12.4, Appendix C · canon §10.1, §10.5 · GR-11, GR-17 · NFR-038 · ADR-033 · HITL-09

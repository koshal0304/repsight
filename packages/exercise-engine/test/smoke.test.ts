import { expect, test } from "@jest/globals";

import * as engine from "../src/index";

// E0-T02: proves the TypeScript toolchain and Jest run in this package.
test("package entry loads under Jest", () => {
  expect(engine).toBeDefined();
});

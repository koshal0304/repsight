// Shared ESLint config (05 §5.1); each package re-exports it from its own eslint.config.js.
import comments from "@eslint-community/eslint-plugin-eslint-comments/configs";
import js from "@eslint/js";
import { defineConfig } from "eslint/config";
import tseslint from "typescript-eslint";

export default defineConfig(
  js.configs.recommended,
  tseslint.configs.strictTypeChecked,
  { languageOptions: { parserOptions: { projectService: true } } },
  { files: ["**/*.js"], extends: [tseslint.configs.disableTypeChecked] },
  // `any` is an error; a disable needs a reason: `// eslint-disable-next-line <rule> -- reason: <why>`.
  comments.recommended,
  {
    rules: { "@eslint-community/eslint-comments/require-description": "error" },
  },
);

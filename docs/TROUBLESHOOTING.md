# Troubleshooting

## Unsupported instruction
Use a documented parser pattern. The first release is intentionally limited.

## Unsupported target
Use one of the ten target names in `docs/CLI.md`.

## Generated code differs between languages
Languages have different syntax and semantics. Translation is defined over supported IR operations, not identical source text.

## Native machine code
Machine code requires a CPU architecture and toolchain. Future LLVM or architecture-specific backends can provide this layer.

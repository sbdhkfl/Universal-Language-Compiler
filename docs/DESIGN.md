# Design principles

## Predictability
The compiler should never silently guess missing semantics.

## Separation
Natural language, IR, and target generation are separate layers.

## Extensibility
New languages should require a backend rather than changes throughout the parser.

## Safety
Generated code is data until the user explicitly chooses to compile or run it.

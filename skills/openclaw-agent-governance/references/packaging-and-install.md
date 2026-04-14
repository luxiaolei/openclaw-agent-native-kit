# Packaging and install

For public reuse, prefer a portable git repo first.

## Include
- reusable skills
- generic specialist templates
- an install script
- a sample config patch or registration flow
- docs showing which lanes each specialist owns

## Exclude
- secrets
- auth stores
- private memory
- user-specific notes that do not generalize

## Installation posture

The first install target should be predictable local copy + config registration.
A full plugin can come later if the pack proves stable across multiple machines.

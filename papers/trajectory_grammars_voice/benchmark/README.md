# Synthetic Spanish Voice-Agent Trajectory Benchmark

Frozen, schema-identical benchmark for `papers/trajectory_grammars_voice` (§5.4).
Generator replays schema-conformant Spanish conversation templates over the trajectory
grammar G=(Q,S,delta) with timing/tool-RTT distributions; stratified by scenario class
and terminal label; leave-one-campaign-out + temporal-blocking split manifests with
SHA-256 checksums; CC-BY-4.0 datasheet.

Build: python generate.py --seed 20261013 --out corpus/
Ship: after re-identification check (membership inference + singularity screen).

# stage3-test-faulty

Test controller for the KFUPM F1TENTH Stage 3 platform (organizer test, not a team).

## Official run

- Package: `kfupm_test_faulty`
- Entry point: `ros2 run kfupm_test_faulty controller`
- Starts moving: within 2 s

Corrected on branch `fix-ready`: uses F1TENTH_DATA_DIR and still drives with an empty data folder. The `stage3-final` tag is the faulty version (two deliberate mistakes: a hard-coded /home/... data path and a crash when no lap was saved).

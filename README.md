# stage3-test-faulty

Test controller for the KFUPM F1TENTH Stage 3 platform (organizer test, not a team).

## Official run

- Package: `kfupm_test_faulty`
- Entry point: `ros2 run kfupm_test_faulty controller`
- Starts moving: within 2 s

Like the learner, but with two typical mistakes (on purpose): a hard-coded /home/... data path and a crash when no lap was saved.

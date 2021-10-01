# MSIT · 0️⃣ 1️⃣ 2️⃣ 3️⃣ · 🤔 · ⬅️ ⬇️ ➡️

This Multi-Source Interference Task (MSIT) was built specifically for children and use in an MEG scanner using PsychoPy3 (v2021.1.4). Feel free to [contact me](julie.tseng@sickkids.ca) if you have any questions.

## Task configuration

### Breakdown:
```
Instructions -> Practice: 20 trials (randomized) -> Checkpoint -> Task: 200 trials (randomized)
             ->      4s x 20 trials = 1.33min     ->            -> 4s x 200 trials = 13.3min
```

### Trial breakdown:
```
Fixation + grating (0.5s) -> Triplet presentation (3.0s) -> Blank screen (0.5s)
```

### Additional info:

| Task component | Info |
| -------------- | ---- |
| Number of congruent trials | 10 (practice)<br>100 |
| Number of incongruent trials | 10 (practice)<br>100 |
| Fixation cross and grating duration | 0.5 seconds |
| Stimulus presentation duration | 3.0 seconds |
| Blank screen duration | 0.5 seconds |
| Congruent stim | 100, 020, 003 |
| Incongruent stim | 221, 331 <br> 212, 313 <br> 112, 211 <br> 332, 233 <br> 311, 131 <br> 322, 232 |
| Grating stim | Circular, phase 0.0, spatial frequency 3 |

## References

Gaetz, W., Liu, C., Zhu, H., Bloy, L., & Roberts, T. P. (2013). Evidence for a motor gamma-band network governing response interference. _Neuroimage_, 74, 245-253.

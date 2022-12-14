# MSIT · 0️⃣ 1️⃣ 2️⃣ 3️⃣ · 🤔 · ⬅️ ⬇️ ➡️

This Multi-Source Interference Task (MSIT) was built specifically for children and use in an MEG scanner using PsychoPy3 (v2021.1.4). Feel free to [contact me](julie.tseng@sickkids.ca) if you have any questions.

## To do list

- [x] Liz to identify task structure
    * Ended up differing from the MSIT implementation I found on Github.
- [x] Build skeleton of task from scratch on PsychoPy3 Builder
- [x] Add functionality to generate randomized trial lists
    * Works by creating an array of 0s and 1s (congruent, incongruent), shuffling, sampling from stim categories, and storing in a list of dicts. 
- [x] Add feedback during practice trials
    * For `list('122')`, find value with `count == 1` and look up correspondence with keyboard arrow button press
- [x] Liz to refine instructions text and other aesthetics (e.g., background colour, text size)
- [ ] ~Insert flashing square for photo diode~
- [x] Set up parallel port I/O for registering button presses
- [x] Set up triggers to be sent to MEG acquisition system
- [x] Confirm lower left field visual grating stim parameters
    * Actually, will be a square grating that appears alongside text stimulus
- [x] Make version compatible with PsychoPy2

## Task configuration

### Breakdown:
```
Instructions -> Practice: 15 trials (randomized) -> Checkpoint -> Task: 200 trials (randomized)
             ->      6s x 15 trials = 1.5min     ->            -> 4s x 200 trials = 13.3min
```

### Trial breakdown:
```
Practice (6 sec): Fixation (0.5s) -> Triplet presentation + grating (5.0s) -> Blank screen (0.5s)
Actual (4 sec): Fixation (0.5s) -> Triplet presentation + grating (3.0s) -> Blank screen (0.5s)
```

### Relevant markers in MEG file:
* PixMode (Triplet presentation)
* Congruent/incongruent
* Button_1, Button_2, Button_3
* Correct (lack of correct = incorrect)

Note that, because PsychoPy does fancy stuff with locking stimulus presentation to frame changes, pixel mode triggers line up perfectly to the "next frame" after a digital trigger is sent. 

### Additional info:

| Task component | Info |
| -------------- | ---- |
| Number of practice trials | 15 |
| Number of congruent trials | 100 |
| Number of incongruent trials | 100 |
| Fixation cross  duration | 0.5 seconds |
| Triplet and grating duration | 3.0 seconds |
| Blank screen duration | 0.5 seconds |
| Congruent stim | 100, 020, 003 |
| Incongruent stim | 221, 331 <br> 212, 313 <br> 112, 211 <br> 332, 233 <br> 311, 131 <br> 322, 232 |
| Grating stim | Square, phase 0.0, spatial frequency 3 |
| MEG event marker names | Condition: CONG/INCONG<br>Button: BUTTON_1, BUTTON_2, BUTTON_3<br>Performance: Correct|

Note that:
* It's possible for the same two triplets to appear in a row (e.g., fixation -> '100' -> blank -> fixation -> '100')
* Only the first button/key response is checked/registered

## References

Gaetz, W., Liu, C., Zhu, H., Bloy, L., & Roberts, T. P. (2013). Evidence for a motor gamma-band network governing response interference. _Neuroimage_, 74, 245-253.

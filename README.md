# Email Countdown Timer Generator

A lightweight Python script that generates a **branded countdown timer** for email campaigns.

It outputs:
- An **animated GIF** (30 seconds total, 500ms per frame)
- A **static PNG fallback** (first frame)

Built for email use where animated image support varies across clients.


## Features

- Countdown to a fixed UTC deadline
- Days / Hours / Minutes / Seconds layout
- Rounded boxes with UWGT colors
- Uses **Avenir** font (with fallback)
- Transparent background
- Email-safe dimensions
- PNG fallback in case GIF fails


## Output Files

| File | Description |
|------|-------------|
| `timer-email.gif` | Animated countdown GIF |
| `timer-email.png` | Static fallback PNG |


## Layout Details

- Canvas size: **1200 × 360**
- 4 boxes:
  - Days
  - Hours
  - Minutes
  - Seconds
- Rounded corners and centered text


## Requirements

- Python **3.9+**
- Pillow (PIL)

Install dependencies:

```bash
pip install pillow
```
## Configuration
### Deadline

Set the countdown deadline in UTC:

```bash
deadline = datetime(2025, 12, 31, 23, 59, tzinfo=timezone.utc)
```

Colors
```bash
RED = (218, 41, 28, 255)
WHITE = (255, 255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
```

Dimensions
```bash
WIDTH, HEIGHT = 1200, 360
BOX_W, BOX_H = 200, 180
GAP = 36
RADIUS = 40
```
Animation Settings

- Total duration: 30 seconds
- Frame interval: 500ms
- Total frames: 60
- duration=500  (milliseconds per frame)

## Usage

Run the script:

```bash
python count.py
```

The following files will be generated in the project root:
```bash
timer-email.gif
timer-email.png
```

## Email Usage Example
```bash
<img
src="https://nourin-abdelhadi.github.io/email-countdown/timer-email.gif"
alt="Countdown timer" width="600" style="display:block;">
```


For email clients that do not support GIF animation, the static PNG fallback will be displayed automatically.

## Important Notes
- Countdown values are calculated at render time, not live.
- Animated GIF timers do not update in real time once sent.
- Transparency allows the timer to be placed on any email background.
- Optimized for common email client rendering limitations.

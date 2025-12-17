from datetime import datetime, timezone, timedelta
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BASE_DIR, "fonts")

deadline = datetime(2025, 12, 31, 23, 59, tzinfo=timezone.utc)

RED = (218, 41, 28, 255)
WHITE = (255, 255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)

WIDTH, HEIGHT = 1200, 360
BOX_W, BOX_H = 200, 180
GAP = 36
RADIUS = 40


def load_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype(
                os.path.join(FONT_DIR, "Avenir-Heavy.ttf"), size
            )
        return ImageFont.truetype(
            os.path.join(FONT_DIR, "Avenir.ttf"), size
        )
    except OSError:
        return ImageFont.load_default()


def draw_frame(now):
    remaining = max(deadline - now, timedelta(0))

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    img = Image.new("RGBA", (WIDTH, HEIGHT), TRANSPARENT)
    draw = ImageDraw.Draw(img)

    font_big = load_font(80, bold=True)
    font_small = load_font(24)

    boxes = [
        ("Days", f"{days:02}"),
        ("Hours", f"{hours:02}"),
        ("Minutes", f"{minutes:02}"),
        ("Seconds", f"{seconds:02}")
    ]

    start_x = (WIDTH - (BOX_W * 4 + GAP * 3)) // 2
    y_box = 40

    for i, (label, value) in enumerate(boxes):
        x = start_x + i * (BOX_W + GAP)

        draw.rounded_rectangle(
            [x, y_box, x + BOX_W, y_box + BOX_H],
            radius=RADIUS,
            fill=RED
        )

        vw, vh = draw.textbbox((0, 0), value, font=font_big)[2:]
        draw.text(
            (x + (BOX_W - vw) // 2, y_box + (BOX_H - vh) // 2 - 4),
            value,
            font=font_big,
            fill=WHITE
        )

        lw, lh = draw.textbbox((0, 0), label, font=font_small)[2:]
        draw.text(
            (x + (BOX_W - lw) // 2, y_box + BOX_H + 10),
            label,
            font=font_small,
            fill=RED
        )

    return img


def generate_assets():
    frames = []

    start_time = datetime.now(timezone.utc)

    # 30 seconds total, 500ms per frame → 60 frames
    for i in range(60):
        frame_time = start_time + timedelta(milliseconds=500 * i)
        frames.append(draw_frame(frame_time))

    # 🔹 Animated GIF
    frames[0].save(
        "timer-email.gif",
        save_all=True,
        append_images=frames[1:],
        duration=500,  # 500ms
        loop=0,
        optimize=True,
        disposal=2
    )

    # 🔹 Static fallback PNG (first frame)
    frames[0].save("timer-email.png", optimize=True)


if __name__ == "__main__":
    generate_assets()

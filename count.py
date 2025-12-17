from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(BASE_DIR, "fonts")

deadline = datetime(2025, 12, 31, 23, 59, tzinfo=timezone.utc)

RED = (218, 41, 28, 255)
WHITE = (255, 255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)

def load_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype(
                os.path.join(FONT_DIR, "Avenir-Heavey.ttf"), size
            )
        return ImageFont.truetype(
            os.path.join(FONT_DIR, "Avenir.ttf"), size
        )
    except OSError:
        return ImageFont.load_default()

def generate_countdown_image():
    now = datetime.now(timezone.utc)
    remaining = deadline - now

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    img = Image.new("RGBA", (1200, 360), TRANSPARENT)
    draw = ImageDraw.Draw(img)

    font_big = load_font(80, bold=True)
    font_small = load_font(40)

    boxes = [
        ("Days", f"{days:02}"),
        ("Hours", f"{hours:02}"),
        ("Minutes", f"{minutes:02}"),
        ("Seconds", f"{seconds:02}")
    ]

    box_w, box_h = 200, 180
    gap = 36
    start_x = (img.width - (box_w * 4 + gap * 3)) // 2
    y_box = 40
    radius = 40

    for i, (label, value) in enumerate(boxes):
        x = start_x + i * (box_w + gap)

        # Red rounded box
        draw.rounded_rectangle(
            [x, y_box, x + box_w, y_box + box_h],
            radius=radius,
            fill=RED
        )

        # Number
        vw, vh = draw.textbbox((0, 0), value, font=font_big)[2:]
        draw.text(
            (x + (box_w - vw) // 2, y_box + (box_h - vh) // 2 - 4),
            value,
            font=font_big,
            fill=WHITE
        )

        # Label underneath
        lw, lh = draw.textbbox((0, 0), label, font=font_small)[2:]
        draw.text(
            (x + (box_w - lw) // 2, y_box + box_h + 10),
            label,
            font=font_small,
            fill=RED
        )

    img.save("timer-email.png", optimize=True)

if __name__ == "__main__":
    generate_countdown_image()


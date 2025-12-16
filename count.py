from datetime import datetime, timezone
from PIL import Image, ImageDraw, ImageFont

deadline = datetime(2025, 12, 31, 23, 59, tzinfo=timezone.utc)

RED = (218, 41, 28, 255)    # #da291c
WHITE = (255, 255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)

def load_font(size, bold=False):
    try:
        if bold:
            return ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", size)
        return ImageFont.truetype("C:/Windows/Fonts/arial.ttf", size)
    except OSError:
        return ImageFont.load_default()

def generate_countdown_image():
    now = datetime.now(timezone.utc)
    remaining = deadline - now

    days = remaining.days
    hours, rem = divmod(remaining.seconds, 3600)
    minutes, seconds = divmod(rem, 60)

    img = Image.new("RGBA", (600, 180), TRANSPARENT)
    draw = ImageDraw.Draw(img)

    font_number = load_font(40, bold=True)
    font_label = load_font(14)

    boxes = [
        ("Days", f"{days:02}"),
        ("Hours", f"{hours:02}"),
        ("Minutes", f"{minutes:02}"),
        ("Seconds", f"{seconds:02}")
    ]

    box_w, box_h = 100, 90
    gap = 18
    start_x = (img.width - (box_w * 4 + gap * 3)) // 2
    y_box = 20
    radius = 22

    for i, (label, value) in enumerate(boxes):
        x = start_x + i * (box_w + gap)

        # Red rounded box
        draw.rounded_rectangle(
            [x, y_box, x + box_w, y_box + box_h],
            radius=radius,
            fill=RED
        )

        # Number
        vw, vh = draw.textbbox((0, 0), value, font=font_number)[2:]
        draw.text(
            (x + (box_w - vw) // 2, y_box + (box_h - vh) // 2 - 4),
            value,
            font=font_number,
            fill=WHITE
        )

        # Label underneath
        lw, lh = draw.textbbox((0, 0), label, font=font_label)[2:]
        draw.text(
            (x + (box_w - lw) // 2, y_box + box_h + 10),
            label,
            font=font_label,
            fill=RED
        )

    img.save("timer-email.png", optimize=True)

if __name__ == "__main__":
    generate_countdown_image()

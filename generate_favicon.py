"""Generate a simple 32x32 favicon with the text 'GPA' on a blue background."""
import struct
import zlib


def create_favicon_ico(path):
    """Create a minimal 16x16 .ico file with a blue square and white 'G' pattern."""
    width, height = 16, 16
    blue = (0x0D, 0x6E, 0xFD, 0xFF)   # BGRA order for ICO
    white = (0xFF, 0xFF, 0xFF, 0xFF)

    # Simple 'G' pattern (rough pixel art)
    g_pattern = {
        (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3),
        (3, 4), (4, 4),
        (3, 5),
        (3, 6),
        (3, 7), (7, 7), (8, 7), (9, 7), (10, 7),
        (3, 8), (10, 8),
        (3, 9), (10, 9),
        (3, 10), (4, 10), (10, 10),
        (4, 11), (5, 11), (6, 11), (7, 11), (8, 11), (9, 11), (10, 11),
    }

    # Build pixel data (BGRA, bottom-up)
    pixel_data = bytearray()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            if (x, y) in g_pattern:
                pixel_data.extend(white)
            else:
                pixel_data.extend(blue)

    # AND mask (all transparent = 0)
    and_mask = bytes(height * (((width + 31) // 32) * 4))

    # BITMAPINFOHEADER
    bih = struct.pack('<IiiHHIIiiII',
        40,             # biSize
        width,          # biWidth
        height * 2,     # biHeight (double for AND mask)
        1,              # biPlanes
        32,             # biBitCount
        0,              # biCompression
        len(pixel_data) + len(and_mask),
        0, 0, 0, 0
    )

    image_data = bih + bytes(pixel_data) + and_mask

    # ICONDIR
    icondir = struct.pack('<HHH', 0, 1, 1)
    # ICONDIRENTRY (offset = 6 + 16 = 22)
    entry = struct.pack('<BBBBHHII',
        width if width < 256 else 0,
        height if height < 256 else 0,
        0,  # color count
        0,  # reserved
        1,  # planes
        32, # bit count
        len(image_data),
        22  # offset
    )

    with open(path, 'wb') as f:
        f.write(icondir + entry + image_data)

    print(f"Favicon written to {path}")


if __name__ == "__main__":
    import os
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "static", "img", "favicon.ico")
    create_favicon_ico(target)

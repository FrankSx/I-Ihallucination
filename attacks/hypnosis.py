#!/usr/bin/env python3
"""
🌀 Hypnosis Attack Module
Perceptual manipulation through visual patterns

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

Generates stroboscopic, spiral, and phi phenomenon attacks
designed to induce perceptual confusion in ML vision systems.
"""

import argparse
import math
import random
from typing import List, Tuple, Dict


class HypnosisGenerator:
    """Generate perceptual hallucination patterns"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)

    def generate_spiral(self, 
                       size: int = 400, 
                       coils: int = 5, 
                       points: int = 1000,
                       style: str = 'archimedes') -> str:
        """
        Generate hypnotic spiral SVG

        Args:
            size: Canvas size
            coils: Number of spiral coils
            points: Resolution
            style: 'archimedes', 'logarithmic', 'fermat'
        """
        center = size // 2
        max_radius = size // 2 - 20

        path_points = []

        for i in range(points):
            t = (i / points) * coils * 2 * math.pi

            if style == 'archimedes':
                r = (t / (coils * 2 * math.pi)) * max_radius
            elif style == 'logarithmic':
                r = max_radius * (0.1 * math.exp(0.3 * t))
                r = min(r, max_radius)
            elif style == 'fermat':
                r = max_radius * math.sqrt(t / (coils * 2 * math.pi))

            x = center + r * math.cos(t)
            y = center + r * math.sin(t)
            path_points.append(f"{x:.2f},{y:.2f}")

        # Generate alternating colors for stroboscopic effect
        colors = ['#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF']

        svg_parts = [
            f'<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">',
            f'<rect width="{size}" height="{size}" fill="black"/>',
            '<g id="spiral-group">'
        ]

        # Create multiple offset spirals for interference
        for offset in range(3):
            color = colors[offset % len(colors)]
            offset_points = []
            for i, pt in enumerate(path_points):
                x, y = map(float, pt.split(','))
                angle = offset * (2 * math.pi / 3)
                new_x = center + (x - center) * math.cos(angle) - (y - center) * math.sin(angle)
                new_y = center + (x - center) * math.sin(angle) + (y - center) * math.cos(angle)
                offset_points.append(f"{new_x:.2f},{new_y:.2f}")

            path_data = "M " + " L ".join(offset_points[:len(offset_points)//2])
            svg_parts.append(
                f'<path d="{path_data}" stroke="{color}" stroke-width="2" '
                f'fill="none" opacity="0.8"/>'
            )

        # Add animation for rotation
        svg_parts.extend([
            '<animateTransform',
            '    attributeName="transform"',
            '    attributeType="XML"',
            '    type="rotate"',
            f'    from="0 {center} {center}"',
            f'    to="360 {center} {center}"',
            '    dur="3s"',
            '    repeatCount="indefinite"/>',
            '</g>',
            '</svg>'
        ])

        return '\n'.join(svg_parts)

    def generate_strobe(self,
                       width: int = 800,
                       height: int = 600,
                       frequency: float = 10.0,
                       pattern: str = 'checkerboard') -> str:
        """
        Generate stroboscopic pattern

        Args:
            frequency: Flash frequency in Hz
            pattern: 'checkerboard', 'bars', 'radial'
        """
        colors = ['#FFFFFF', '#000000']
        duration = 1.0 / frequency

        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<defs>',
            '    <style>',
            '        .strobe { animation: flash ' + str(duration) + 's infinite; }',
            '        @keyframes flash {',
            '            0%, 100% { fill: ' + colors[0] + '; }',
            '            50% { fill: ' + colors[1] + '; }',
            '        }',
            '    </style>',
            '</defs>'
        ]

        if pattern == 'checkerboard':
            cell_size = 50
            for row in range(height // cell_size):
                for col in range(width // cell_size):
                    x = col * cell_size
                    y = row * cell_size
                    color_idx = (row + col) % 2
                    delay = (row + col) * 0.05
                    svg_parts.append(
                        f'<rect x="{x}" y="{y}" width="{cell_size}" height="{cell_size}" '
                        f'fill="{colors[color_idx]}" class="strobe" '
                        f'style="animation-delay: {delay}s"/>'
                    )

        elif pattern == 'bars':
            bar_width = width // 20
            for i in range(20):
                x = i * bar_width
                delay = i * 0.02
                svg_parts.append(
                    f'<rect x="{x}" y="0" width="{bar_width}" height="{height}" '
                    f'fill="{colors[i % 2]}" class="strobe" '
                    f'style="animation-delay: {delay}s"/>'
                )

        elif pattern == 'radial':
            cx, cy = width // 2, height // 2
            rings = 20
            for i in range(rings):
                r = (i + 1) * (max(cx, cy) // rings)
                delay = i * 0.03
                svg_parts.append(
                    f'<circle cx="{cx}" cy="{cy}" r="{r}" '
                    f'fill="{colors[i % 2]}" class="strobe" '
                    f'style="animation-delay: {delay}s" opacity="0.5"/>'
                )

        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    def generate_phi_phenomenon(self,
                               width: int = 600,
                               height: int = 400,
                               dots: int = 12,
                               speed: float = 0.1) -> str:
        """
        Generate Phi phenomenon (apparent motion) illusion

        Exploits persistence of vision to create motion where none exists.
        """
        cx, cy = width // 2, height // 2
        radius = min(cx, cy) - 50

        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<rect width="100%" height="100%" fill="#111"/>'
        ]

        for i in range(dots):
            angle = (i / dots) * 2 * math.pi
            x = cx + radius * math.cos(angle)
            y = cy + radius * math.sin(angle)
            delay = i * speed

            svg_parts.extend([
                f'<circle cx="{x}" cy="{y}" r="8" fill="#0F0">',
                f'    <animate attributeName="opacity" values="0;1;0" dur="{dots * speed}s" '
                f'repeatCount="indefinite" begin="{delay}s"/>',
                '</circle>'
            ])

        # Add phantom dot in center (suggestion of motion)
        svg_parts.extend([
            f'<circle cx="{cx}" cy="{cy}" r="4" fill="#F00" opacity="0.3">',
            '    <animate attributeName="r" values="4;20;4" dur="2s" repeatCount="indefinite"/>',
            '</circle>',
            '</svg>'
        ])

        return '\n'.join(svg_parts)

    def generate_color_fatigue(self, size: int = 500) -> str:
        """Generate color fatigue / afterimage attack"""
        svg = f'''<svg width="{size}" height="{size}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="chromatic">
            <feColorMatrix type="matrix" values="
                1 0 0 0 0
                0 1 0 0 0
                0 0 1 0 0
                0 0 0 1 0"/>
        </filter>
    </defs>
    <rect width="{size}" height="{size}" fill="cyan"/>
    <g filter="url(#chromatic)">
        <circle cx="{size//3}" cy="{size//2}" r="{size//4}" fill="red" opacity="0.8">
            <animateTransform attributeName="transform" type="translate"
                values="0,0; 50,0; 0,0" dur="0.5s" repeatCount="indefinite"/>
        </circle>
        <circle cx="{2*size//3}" cy="{size//2}" r="{size//4}" fill="green" opacity="0.8">
            <animateTransform attributeName="transform" type="translate"
                values="0,0; -50,0; 0,0" dur="0.5s" repeatCount="indefinite"/>
        </circle>
    </g>
    <text x="50%" y="90%" text-anchor="middle" fill="white" font-size="20">
        Stare at center for 30 seconds, then look at white surface
    </text>
</svg>'''
        return svg

    def generate_scroll_hallucination(self,
                                     width: int = 800,
                                     height: int = 600,
                                     speed: float = 50) -> str:
        """Generate scrolling text that induces motion aftereffect"""
        text_lines = [
            "REALITY IS FLUID",
            "PERCEPTION IS MALLEABLE",
            "CONSCIOUSNESS IS CODE",
            "TRUTH IS NEGOTIABLE",
            "BOUNDARIES ARE ILLUSIONS"
        ] * 10

        y_positions = [i * 60 for i in range(len(text_lines))]

        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<rect width="100%" height="100%" fill="black"/>',
            '<defs>',
            '    <linearGradient id="fade" x1="0%" y1="0%" x2="0%" y2="100%">',
            '        <stop offset="0%" style="stop-color:black;stop-opacity:1" />',
            '        <stop offset="20%" style="stop-color:black;stop-opacity:0" />',
            '        <stop offset="80%" style="stop-color:black;stop-opacity:0" />',
            '        <stop offset="100%" style="stop-color:black;stop-opacity:1" />',
            '    </linearGradient>',
            '</defs>',
            '<g id="scrolling-text">'
        ]

        for i, line in enumerate(text_lines):
            y = y_positions[i]
            svg_parts.append(
                f'<text x="{width//2}" y="{y}" text-anchor="middle" '
                f'fill="hsl({(i * 30) % 360}, 100%, 50%)" font-size="36" '
                f'font-family="monospace" font-weight="bold">{line}</text>'
            )

        total_height = len(text_lines) * 60
        duration = total_height / speed

        svg_parts.extend([
            f'    <animateTransform attributeName="transform" type="translate"',
            f'        values="0,{height}; 0,-{total_height}" dur="{duration}s" '
            f'repeatCount="indefinite"/>',
            '</g>',
            '<rect width="100%" height="100%" fill="url(#fade)" pointer-events="none"/>',
            '</svg>'
        ])

        return '\n'.join(svg_parts)


def main():
    parser = argparse.ArgumentParser(description='🌀 GHOSTBYTE Hypnosis Generator')
    parser.add_argument('--mode', choices=['spiral', 'strobe', 'phi', 'color', 'scroll'],
                       required=True, help='Hypnosis attack mode')
    parser.add_argument('--output', '-o', default='hypnosis_attack.svg',
                       help='Output file')
    parser.add_argument('--intensity', type=float, default=0.5,
                       help='Attack intensity 0.0-1.0')
    parser.add_argument('--size', type=int, default=500)
    parser.add_argument('--seed', type=int)

    args = parser.parse_args()

    gen = HypnosisGenerator(seed=args.seed)

    if args.mode == 'spiral':
        result = gen.generate_spiral(
            size=args.size,
            coils=int(3 + args.intensity * 10),
            style='archimedes'
        )
    elif args.mode == 'strobe':
        result = gen.generate_strobe(
            width=args.size,
            height=args.size,
            frequency=5 + args.intensity * 15
        )
    elif args.mode == 'phi':
        result = gen.generate_phi_phenomenon(
            width=args.size,
            height=int(args.size * 0.67),
            speed=0.2 - (args.intensity * 0.15)
        )
    elif args.mode == 'color':
        result = gen.generate_color_fatigue(size=args.size)
    elif args.mode == 'scroll':
        result = gen.generate_scroll_hallucination(
            width=args.size,
            height=int(args.size * 0.75),
            speed=30 + args.intensity * 50
        )

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"🌀 Hypnosis attack generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Intensity: {args.intensity}")
    print(f"   ⚠️  WARNING: May cause visual discomfort")


if __name__ == '__main__':
    main()

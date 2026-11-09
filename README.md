# Ludo 3D Dice Roller (Android / Mobile-First PWA)

A mobile-first 3D dice rolling application designed for physical Ludo and board games when dice are lost, broken, or unavailable.

## Key Features & Highlights

1. **Mobile-First React Native Android UI/UX**:
   - Modern Material Design 3 tokens, floating cards, tactile buttons, and simulated Android status bar.
   - Screen Wake Lock API enabled to keep phone screen awake throughout board game sessions.
   - 100% immersive, distraction-free "Focus Mode" and native Fullscreen toggle.

2. **Realistic 3D Physics Simulation (Three.js)**:
   - High-definition 3D dice with beveled edges, realistic pips, and glossy materials.
   - Luxury mahogany wooden tray with deep emerald felt bottom and soft shadows.
   - Real-time tumbling, bounce restitution, wall collisions, and settling physics.
   - Randomized suspenseful roll durations for curiosity and genuine board game vibe.

3. **Authentic Procedural Audio Engine (Web Audio API - 100% Offline)**:
   - Zero external audio files or network dependencies needed!
   - Rhythmic "kadh-kadh-kadh" dice cup shaking sound when tapping/holding the screen.
   - Dynamic impact clacks on tray floor and walls scaled to bounce intensity.
   - Triumphant celebration fanfares on rolling 6s and double-six rerolls.
   - Full mute toggle and volume control slider.

4. **Ludo Rules & Turn Rotation**:
   - 1 Player (Solo / Pass & play), 2 Players, 3 Players, 4 Players, or up to 6 Players.
   - Classic Ludo token colors (Red, Green, Yellow, Blue, Orange, Purple) with customizable names.
   - **Double-Six Rule (2 Dice)**: Rolling two 6s grants an immediate bonus turn ("Reroll Again!").
   - **Single-Six Rule (1 Die)**: Rolling a 6 grants a bonus reroll.
   - Consecutive history log tracking every roll and reroll.

5. **Multi-Phone Wireless Play (WebRTC & QR Code)**:
   - One phone acts as the central board/tray (Host).
   - Other players scan the QR code using their own phone cameras to join as wireless controllers.
   - Each player can tap to roll from their own seat with live turn synchronization!

6. **Hidden & Secret Cheat Feature (Discreetly Engineered)**:
   - In the top-right corner, a tiny cosmetic status dot indicates the target angle:
     - **Red Dot**: 45° angle (Top-Right corner)
     - **Green Dot**: 135° angle (Top-Left corner)
     - **Blue Dot**: 225° angle (Bottom-Left corner)
     - **Yellow Dot**: 315° angle (Bottom-Right corner)
   - **How to activate**:
     1. Tap/press and hold anywhere on the screen for about 1.2 to 2 seconds.
     2. While holding, the realistic "kadh-kadh-kadh" dice cup shaking sound plays continuously.
     3. From the initial touch point, drag your finger/cursor toward the corner matching the indicator color.
     4. A discreet silent haptic vibration alerts you that the cheat is armed.
     5. Release your finger to roll: you are guaranteed to roll ALL SIXES (e.g. `[6, 6]` on 2 dice, `[6]` on 1 die)!
     6. Because the game follows official Ludo rules, rolling double-sixes triggers an immediate legitimate bonus reroll!

## How to Install on Android
1. Open `index.html` (or `ludo_dice_app.html`) in Google Chrome on your Android phone.
2. Tap the Chrome menu (three dots in top right) -> **"Add to Home screen"** or **"Install app"**.
3. The app will install with a native app icon and run full screen without address bar distractions!

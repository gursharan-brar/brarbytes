"""Synthesize the brag soundtrack: 120 BPM, A minor, everything on one beat grid from t=0.

Writes mix.wav (44.1 kHz stereo, 20 s). The voice is the real intro line from episodes/2026-11-03.mp3.
"""
import wave
import numpy as np

SR = 44100
DUR = 20.0
BEAT = 0.5
N = int(SR * DUR)
t_all = np.arange(N) / SR
rng = np.random.default_rng(7)


def hz(midi):
    return 440.0 * 2 ** ((midi - 69) / 12)


def onepole_lp(x, cutoff):
    """One-pole low-pass; cutoff may be a scalar or a per-sample array."""
    cutoff = np.broadcast_to(np.asarray(cutoff, dtype=np.float64), x.shape)
    a = 1 - np.exp(-2 * np.pi * cutoff / SR)
    y = np.empty_like(x)
    acc = 0.0
    for i in range(len(x)):
        acc += a[i] * (x[i] - acc)
        y[i] = acc
    return y


def env_ad(n, attack, decay):
    t = np.arange(n) / SR
    e = np.minimum(1, t / max(attack, 1e-4)) * np.exp(-t / decay)
    return e


def place(buf, sig, at, gain=1.0):
    i = int(round(at * SR))
    if i >= len(buf):
        return
    j = min(len(buf), i + len(sig))
    buf[i:j] += sig[: j - i] * gain


# chord timeline: (start, end, root midi, chord tones as semitone offsets)
AM, F, C, G = (57, (0, 3, 7)), (53, (0, 4, 7)), (48, (0, 4, 7)), (55, (0, 4, 7))
CHORDS = [(0, 5, AM), (5, 7, F), (7, 9, C), (9, 11, G), (11, 13, AM), (13, 15, F), (15, 17, C), (17, 19, G), (19, 20, AM)]


def chord_at(t):
    for s, e, c in CHORDS:
        if s <= t < e:
            return c
    return AM


L = np.zeros(N)
R = np.zeros(N)
music = np.zeros(N)  # mono bus for drums/bass, panned centre


# ---- pad: detuned saws per chord segment, filtered; opens up at 3.0
def saw(freq, n, phase=0.0):
    ph = (phase + freq * np.arange(n) / SR) % 1.0
    return 2 * ph - 1


pad_L = np.zeros(N)
pad_R = np.zeros(N)
for s, e, (root, tones) in CHORDS:
    n = int((e - s) * SR)
    seg_L = np.zeros(n)
    seg_R = np.zeros(n)
    for k, off in enumerate(tones + (12,)):
        f = hz(root + 12 + off)
        seg_L += saw(f * 1.003, n, 0.1 * k)
        seg_R += saw(f * 0.997, n, 0.37 * k)
    fade = np.minimum(1, np.arange(n) / (0.02 * SR)) * np.minimum(1, (n - np.arange(n)) / (0.02 * SR))
    i = int(s * SR)
    pad_L[i : i + n] += seg_L * fade
    pad_R[i : i + n] += seg_R * fade
cut = np.where(t_all < 3, 400 + 1400 * (t_all / 3) ** 2, 2200)
cut = np.where((t_all >= 7) & (t_all < 11), 1200, cut)
cut = np.where(t_all >= 19, 2200 * np.exp(-(t_all - 19) * 1.2), cut)
pad_L = onepole_lp(onepole_lp(pad_L, cut), cut)
pad_R = onepole_lp(onepole_lp(pad_R, cut), cut)
pad_gain = np.where(t_all < 3, 0.10, 0.05) * np.minimum(1, t_all / 0.3)
L += pad_L * pad_gain
R += pad_R * pad_gain

# ---- kick: four on the floor 3.0-7.0, 11.0-19.0, and a final hit at 19.0
def kick():
    n = int(0.35 * SR)
    tt = np.arange(n) / SR
    f = 45 + 95 * np.exp(-tt / 0.03)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-tt / 0.12)


K = kick()
kick_times = [b * BEAT for b in range(6, 14)] + [b * BEAT for b in range(22, 38)] + [19.0]
for kt in kick_times:
    place(music, K, kt, 0.42)
# light kick only on the downbeat of each bar under the voice
for kt in (7.0, 9.0):
    place(music, K, kt, 0.25)


# ---- clap on beats 2 and 4 of each bar (odd beats) in the full sections
def clap():
    n = int(0.18 * SR)
    noise = rng.standard_normal(n)
    hp = noise - onepole_lp(noise, 900)
    return onepole_lp(hp, 6000) * env_ad(n, 0.002, 0.05)


CL = clap()
for b in list(range(7, 14, 2)) + list(range(23, 38, 2)):
    place(music, CL, b * BEAT, 0.28)


# ---- closed hats on 8th offbeats from 0.5 s
def hat():
    n = int(0.06 * SR)
    noise = rng.standard_normal(n)
    return (noise - onepole_lp(noise, 7000)) * env_ad(n, 0.001, 0.018)


H = hat()
for k in range(2, 80):
    ht = k * 0.25
    if ht >= 19.0:
        break
    if k % 2 == 1:  # offbeat 8ths
        g = 0.17 if ht < 3 else 0.14
        if 7 <= ht < 11:
            g = 0.08
        place(music, H, ht, g)

# ---- bass: root 8ths, sidechain-shaped, in the full sections
for k in range(12, 76):
    bt = k * 0.25
    if 7 <= bt < 11 or bt >= 19:
        continue
    root, _ = chord_at(bt)
    f = hz(root - 12)
    n = int(0.23 * SR)
    tt = np.arange(n) / SR
    sig = np.tanh(1.6 * np.sin(2 * np.pi * f * tt)) * env_ad(n, 0.004, 0.16)
    place(music, sig, bt, 0.16 if k % 2 else 0.08)


# ---- pluck arpeggio, 16ths, sections 11-19
def pluck(freq, dur=0.22):
    n = int(dur * SR)
    tt = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * tt) + 0.3 * np.sin(4 * np.pi * freq * tt)
    return s * env_ad(n, 0.002, 0.07)


pattern = [0, 1, 2, 3, 2, 1, 2, 3]
for k in list(range(0, 24)) + list(range(88, 152)):
    at = k * 0.125
    root, tones = chord_at(at)
    seq = [root + 24 + o for o in tones] + [root + 36]
    note = seq[pattern[k % 8] % len(seq)]
    sig = pluck(hz(note))
    if at < 3:
        sig = sig * (1.6 + 0.6 * at / 3)
    pan = 0.35 if k % 2 else -0.35
    L[int(at * SR) : int(at * SR) + len(sig)] += sig[: max(0, min(len(sig), N - int(at * SR)))] * 0.035 * (1 - pan)
    R[int(at * SR) : int(at * SR) + len(sig)] += sig[: max(0, min(len(sig), N - int(at * SR)))] * 0.035 * (1 + pan)

# ---- sfx, tuned to A minor and placed on the grid
# riser into 3.0
n = int(1.5 * SR)
noise = rng.standard_normal(n)
ramp = np.linspace(0, 1, n)
riser = onepole_lp(noise, 300 + 5000 * ramp ** 2) * ramp ** 2.5
place(music, riser, 1.5, 0.12)


def soft_hit(dur=1.2, lp=2500):
    n = int(dur * SR)
    noise = rng.standard_normal(n)
    return onepole_lp(noise, lp) * env_ad(n, 0.003, 0.25)


place(music, soft_hit(), 3.0, 0.14)
# card blips: A5 C6 E6 A6
for at, m in zip((3.25, 3.5, 3.75, 4.0), (81, 84, 88, 93)):
    sig = pluck(hz(m), 0.3)
    place(L, sig, at, 0.05)
    place(R, sig, at, 0.05)
# player pop at 11.0: E5 + A5
for m in (76, 81):
    sig = pluck(hz(m), 0.4)
    place(L, sig, 11.0, 0.05)
    place(R, sig, 11.0, 0.05)
# outro impact at 15.0: low A boom + soft noise
n = int(2.0 * SR)
tt = np.arange(n) / SR
boom = np.sin(2 * np.pi * hz(33) * tt) * np.exp(-tt / 0.6)
place(music, boom, 15.0, 0.35)
place(music, soft_hit(2.0, 1800), 15.0, 0.12)
# final chord sting at 19.0: A minor pluck chord
for m in (69, 72, 76, 81):
    sig = pluck(hz(m), 1.0)
    place(L, sig, 19.0, 0.04)
    place(R, sig, 19.0, 0.04)

L += music
R += music

# ---- duck the music under the voice (7.1-10.9) and add the voice
duck = np.ones(N)
for i0, i1, a, b in ((7.0, 7.2, 1, 0.32), (7.2, 10.8, 0.32, 0.32), (10.8, 11.0, 0.32, 1)):
    sl = (t_all >= i0) & (t_all < i1)
    duck[sl] = a + (b - a) * (t_all[sl] - i0) / (i1 - i0)
L *= duck
R *= duck

with wave.open("voice.wav") as w:
    v = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float64) / 32768
v *= 1.0 / np.max(np.abs(v))
v[-int(0.05 * SR):] *= np.linspace(1, 0, int(0.05 * SR))
place(L, v, 7.25, 1.0)  # clip starts 0.30 s into the episode; speech runs ~7.29-10.77, matching the typing
place(R, v, 7.25, 1.0)

# ---- master: gentle glue, tail fade, peak at -1 dBFS
mix = np.stack([L, R], 1)
mix = np.tanh(mix * 1.2) / 1.2
tail = np.ones(N)
tail[t_all > 19.6] = np.linspace(1, 0, np.sum(t_all > 19.6))
mix *= tail[:, None]
mix *= 10 ** (-1 / 20) / np.max(np.abs(mix))
pcm = (mix * 32767).astype(np.int16)
with wave.open("mix.wav", "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("wrote mix.wav", pcm.shape[0] / SR, "s")

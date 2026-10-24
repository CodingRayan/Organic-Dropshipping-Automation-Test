import React from 'react';
import '@fontsource/tiktok-sans/700.css';
import {EmojiText} from './EmojiText';
import {AbsoluteFill, Audio, OffthreadVideo, Img, Sequence, staticFile, useCurrentFrame, interpolate} from 'remotion';

// One scene = one clip (or still image) with optional trim, zoom, caption and sound effects.
export type Caption = {text: string; from?: number; to?: number; style?: 'hook' | 'big' | 'cta'; top?: number};
export type Sfx = {file: string; at: number; volume?: number};
export type Scene = {
  src: string;            // file in public/clips (mp4 or image)
  start?: number;         // seconds to skip at the start of the clip
  duration: number;       // seconds to show
  volume?: number;        // clip's own audio (talking, reactions); omit = muted
  zoom?: number;          // 1 = none, 1.3 = 130%
  zoomOriginY?: string;   // e.g. '80%' to zoom toward the bottom
  blurs?: {x: number; y: number; w: number; h: number}[]; // % boxes to blur (e.g. gibberish TV text)
  captions?: Caption[];   // times relative to the scene, in seconds
  sfx?: Sfx[];            // times relative to the scene, in seconds
};
// music.dropAt = second in the song where the beat drops; music.popAt = second in the video where it should land.
export type AdProps = {fps: number; scenes: Scene[]; music?: {file: string; volume?: number; dropVolume?: number; start?: number; dropAt?: number; popAt?: number}};

export const totalFrames = (p: AdProps) => p.scenes.reduce((n, s) => n + Math.round(s.duration * p.fps), 0);

const CaptionView: React.FC<{c: Caption}> = ({c}) => {
  const f = useCurrentFrame();
  const scale = interpolate(f, [0, 5], [0.85, 1], {extrapolateRight: 'clamp'});
  const big = c.style === 'big';
  const cta = c.style === 'cta';
  const size = big ? 280 : cta ? 72 : 86;
  return (
    <AbsoluteFill style={{justifyContent: big ? 'center' : cta ? 'flex-end' : 'flex-start', alignItems: 'center',
      paddingTop: big || cta ? 0 : (c.top ?? 540), paddingBottom: cta ? 520 : 0}}>
      <div style={{transform: `scale(${scale})`, color: 'white', fontSize: size, fontWeight: 700,
        fontFamily: "'TikTok Sans', Arial, sans-serif", textAlign: 'center', padding: '0 80px', lineHeight: 1.2,
        WebkitTextStroke: big ? '8px black' : '5px black', paintOrder: 'stroke fill', textShadow: '0 2px 6px rgba(0,0,0,0.35)'}}><EmojiText text={c.text} size={size} /></div>
    </AbsoluteFill>
  );
};

const SceneView: React.FC<{s: Scene; fps: number}> = ({s, fps}) => {
  const isImg = /\.(png|jpe?g|webp)$/i.test(s.src);
  const z = s.zoom ?? 1;
  const media = isImg
    ? <Img src={staticFile('clips/' + s.src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    : <OffthreadVideo src={staticFile('clips/' + s.src)} startFrom={Math.round((s.start ?? 0) * fps)} muted={!s.volume} volume={s.volume ?? 0}
        style={{width: '100%', height: '100%', objectFit: 'cover'}} />;
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{transform: `scale(${z})`, transformOrigin: `50% ${s.zoomOriginY ?? '50%'}`}}>{media}
        {(s.blurs ?? []).map((b, i) => <div key={'b' + i} style={{position: 'absolute', left: b.x + '%', top: b.y + '%', width: b.w + '%', height: b.h + '%', backdropFilter: 'blur(10px)', WebkitBackdropFilter: 'blur(10px)', maskImage: 'radial-gradient(ellipse at center, black 55%, transparent 100%)', WebkitMaskImage: 'radial-gradient(ellipse at center, black 55%, transparent 100%)'}} />)}
      </AbsoluteFill>
      {(s.captions ?? []).map((c, i) => {
        const from = Math.round((c.from ?? 0) * fps);
        const to = Math.round((c.to ?? s.duration) * fps);
        return <Sequence key={i} from={from} durationInFrames={Math.max(1, to - from)}><CaptionView c={c} /></Sequence>;
      })}
      {(s.sfx ?? []).map((x, i) => (
        <Sequence key={'s' + i} from={Math.round(x.at * fps)}><Audio src={staticFile('sfx/' + x.file)} volume={x.volume ?? 0.6} /></Sequence>
      ))}
    </AbsoluteFill>
  );
};

export const Ad: React.FC<AdProps> = (p) => {
  let cursor = 0;
  return (
    <AbsoluteFill style={{backgroundColor: 'black'}}>
      {p.scenes.map((s, i) => {
        const len = Math.round(s.duration * p.fps);
        const el = <Sequence key={i} from={cursor} durationInFrames={len}><SceneView s={s} fps={p.fps} /></Sequence>;
        cursor += len;
        return el;
      })}
      {p.music ? (() => {
        const m = p.music!;
        const start = m.dropAt !== undefined && m.popAt !== undefined ? Math.max(0, m.dropAt - m.popAt) : (m.start ?? 0);
        const total = totalFrames(p);
        return <Audio src={staticFile('audio/' + m.file)} startFrom={Math.round(start * p.fps)}
          volume={(f) => {
            const pop = m.popAt !== undefined ? Math.round(m.popAt * p.fps) : 0;
            const base = f < pop ? (m.volume ?? 1) : (m.dropVolume ?? m.volume ?? 1);
            return base * interpolate(f, [total - 15, total], [1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
          }} />;
      })() : null}
    </AbsoluteFill>
  );
};

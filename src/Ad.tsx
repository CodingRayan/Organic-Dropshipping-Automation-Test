import React from 'react';
import {AbsoluteFill, Audio, OffthreadVideo, Img, Sequence, staticFile, useCurrentFrame, interpolate} from 'remotion';

// One scene = one clip (or still image) with optional trim, zoom, caption and sound effects.
export type Caption = {text: string; from?: number; to?: number; style?: 'hook' | 'big'};
export type Sfx = {file: string; at: number; volume?: number};
export type Scene = {
  src: string;            // file in public/clips (mp4 or image)
  start?: number;         // seconds to skip at the start of the clip
  duration: number;       // seconds to show
  zoom?: number;          // 1 = none, 1.3 = 130%
  zoomOriginY?: string;   // e.g. '80%' to zoom toward the bottom
  captions?: Caption[];   // times relative to the scene, in seconds
  sfx?: Sfx[];            // times relative to the scene, in seconds
};
export type AdProps = {fps: number; scenes: Scene[]; music?: {file: string; volume?: number; start?: number}};

export const totalFrames = (p: AdProps) => p.scenes.reduce((n, s) => n + Math.round(s.duration * p.fps), 0);

const CaptionView: React.FC<{c: Caption}> = ({c}) => {
  const f = useCurrentFrame();
  const scale = interpolate(f, [0, 5], [0.85, 1], {extrapolateRight: 'clamp'});
  const big = c.style === 'big';
  return (
    <AbsoluteFill style={{justifyContent: big ? 'center' : 'flex-start', alignItems: 'center', paddingTop: big ? 0 : 330}}>
      <div style={{transform: `scale(${scale})`, color: 'white', fontSize: big ? 260 : 74, fontWeight: 800,
        fontFamily: 'Arial, Helvetica, sans-serif', textAlign: 'center', padding: '0 70px', lineHeight: 1.15,
        WebkitTextStroke: big ? '8px black' : '4px black', paintOrder: 'stroke fill'}}>{c.text}</div>
    </AbsoluteFill>
  );
};

const SceneView: React.FC<{s: Scene; fps: number}> = ({s, fps}) => {
  const isImg = /\.(png|jpe?g|webp)$/i.test(s.src);
  const z = s.zoom ?? 1;
  const media = isImg
    ? <Img src={staticFile('clips/' + s.src)} style={{width: '100%', height: '100%', objectFit: 'cover'}} />
    : <OffthreadVideo src={staticFile('clips/' + s.src)} startFrom={Math.round((s.start ?? 0) * fps)} muted
        style={{width: '100%', height: '100%', objectFit: 'cover'}} />;
  return (
    <AbsoluteFill>
      <AbsoluteFill style={{transform: `scale(${z})`, transformOrigin: `50% ${s.zoomOriginY ?? '50%'}`}}>{media}</AbsoluteFill>
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
      {p.music ? <Audio src={staticFile('audio/' + p.music.file)} volume={p.music.volume ?? 1}
        startFrom={Math.round((p.music.start ?? 0) * p.fps)} /> : null}
    </AbsoluteFill>
  );
};

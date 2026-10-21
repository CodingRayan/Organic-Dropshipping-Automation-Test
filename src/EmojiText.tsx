import React from 'react';
import {Img, staticFile} from 'remotion';

// Renders text with Apple-style emoji images (from emoji-datasource-apple, copied to public/emoji).
const emojiRe = /\p{Extended_Pictographic}(️|‍\p{Extended_Pictographic}|[\u{1F3FB}-\u{1F3FF}])*/gu;

const fileFor = (e: string) =>
  [...e].map((c) => c.codePointAt(0)!.toString(16)).filter((h) => h !== 'fe0f').join('-') + '.png';

export const EmojiText: React.FC<{text: string; size: number}> = ({text, size}) => {
  const parts: React.ReactNode[] = [];
  let last = 0;
  for (const m of text.matchAll(emojiRe)) {
    if (m.index! > last) parts.push(text.slice(last, m.index));
    parts.push(
      <Img key={m.index} src={staticFile('emoji/' + fileFor(m[0]))}
        style={{width: size * 1.05, height: size * 1.05, verticalAlign: '-0.18em', margin: '0 0.08em'}} />
    );
    last = m.index! + m[0].length;
  }
  if (last < text.length) parts.push(text.slice(last));
  return <>{parts}</>;
};

import React from 'react';
import {Composition} from 'remotion';
import {Ad, AdProps, totalFrames} from './Ad';

const defaultProps: AdProps = {fps: 30, scenes: [], music: undefined};

export const Root: React.FC = () => (
  <Composition
    id="Ad"
    component={Ad}
    fps={30}
    width={1080}
    height={1920}
    durationInFrames={30}
    defaultProps={defaultProps}
    calculateMetadata={({props}) => ({durationInFrames: Math.max(1, totalFrames(props))})}
  />
);

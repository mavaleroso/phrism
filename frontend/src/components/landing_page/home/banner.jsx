import * as React from "react";
import { Parallax, Background } from 'react-parallax';

const Banner = () => (
    <React.Fragment>
      <Parallax strength={300} style={{ height: '70vh' }}>
          <Background >
              <img src="/static/images/auth.jpeg" alt="fill murray" />
          </Background>
      </Parallax>
    </React.Fragment>
)

export default Banner;

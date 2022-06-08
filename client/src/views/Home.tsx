import { ReactElement, useEffect, useRef, useState } from "react";
import {
  faJs,
  faReact,
  faPython,
  faVuejs,
  faSass,
  faPhp,
} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { MultipleIconSet } from "../types";
import { Box, Container, Fade, Typography } from "@mui/material";

// @ts-ignore ts(7016)
import NET from 'vanta/dist/vanta.net.min.js';

const ICONS: MultipleIconSet = {
  faJs: {
    icon: faJs,
    color: '#F0DB4F'
  },
  faReact: {
    icon: faReact,
    color: '#61DBFB'
  },
  faVuejs: {
    icon: faVuejs,
    color: '#42B883'
  },
  faPython: {
    icon: faPython,
    color: '#4B8BBE'
  },
  faPhp: {
    icon: faPhp,
    color: '#B0B3D6'
  },
  faSass: {
    icon: faSass,
    color: '#CC6699'
  },
}

const Home = (): ReactElement => {
  const [vantaEffect, setVantaEffect] = useState(false);
  const vantaRef = useRef(null);

  useEffect(() => {
    if (!vantaEffect) {
      setVantaEffect(NET({
        el: vantaRef.current,
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        color: "#3b7b6f",
        backgroundColor: "#35495e",
        points: Math.random() * 7 + 4,
        maxDistance: 10.00,
        spacing: 6.00
      }));
    }

    return () => {
      //@ts-ignore ts(2339)
      if (vantaEffect) vantaEffect.destroy()
    }
  }, [vantaEffect])

  return (
    <Container
      sx={{
        width: "100%",
        height: "100vh"
      }}
      maxWidth="xl"
      ref={vantaRef}
    >
      <Container maxWidth="xl">
        <Box
          sx={{
            width: "100%",
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            marginTop: 10,
          }}
        >
          <Fade
            in={true}
            timeout={1000}
            style={{ transitionDelay: "500ms" }}
          >
            <div>
              <Typography variant="h1" component="h2" color="primary" fontWeight={100}>
                Marek Smieja
              </Typography>
              <Typography variant="h3" component="h3" color="primary" fontWeight={200} marginBottom={7.5}>
                software engineer
              </Typography>
            </div>
          </Fade>
          <Fade
            in={true}
            timeout={1000}
            style={{ transitionDelay: "1000ms" }}
          >
            <div style={{
              width: "100%",
              maxWidth: 415,
              height: 1,
              borderBottom: "0.15rem solid primary",
              marginBottom: 25,
              backgroundColor: "#42b883",
            }}>
            </div>
          </Fade>
          <div>
            {Object.values(ICONS).map((icon, index) =>
              <Fade
                key={index}
                in={true}
                timeout={1000}
                style={{ transitionDelay: `${index * 100 + 1500}ms` }}
              >
                <div>
                  <FontAwesomeIcon
                    style={{
                      paddingRight: 10,
                    }}
                    icon={icon.icon}
                    color={icon.color}
                    pull="left"
                    size="3x"
                  />
                </div>
              </Fade>
            )}
          </div>
        </Box>
      </Container>
    </Container>
  );
};

export default Home;
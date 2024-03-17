import { ButtonGroup, Button, Container, Typography, Fade } from "@mui/material";
import { ReactElement } from "react";
import { Link } from "react-router-dom";
import {
  faJs,
  faReact,
  faPython,
  faVuejs,
  faSass,
  faPhp
} from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { MultipleIconSet } from "../types";
import AOS from "aos";
import 'aos/dist/aos.css';

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

const About = (): ReactElement => {
  AOS.init();

  return (
    <>
      <Container
        sx={{
          width: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          paddingTop: "50px",
        }}
        maxWidth="xl"
      >
        <ButtonGroup variant="contained" style={{ maxHeight: 50 }}>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/"
          >
            <Button
              style={{
                borderTopRightRadius: 0,
                borderBottomRightRadius: 0,
              }}
            >
              Home
            </Button>
          </Link>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
              display: "none",
            }}
            to="/projects"
          >
            <Button
              style={{
                borderRadius: 0,
              }}
            >
              Projects
            </Button>
          </Link>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/about"
          >
            <Button
              style={{
                borderTopLeftRadius: 0,
                borderBottomLeftRadius: 0,
              }}
            >
              About
            </Button>
          </Link>
        </ButtonGroup>
        <Container
          sx={{
            width: "100%",
            marginTop: "50px",
            marginBottom: "50px",
            paddingTop: "12px",
            paddingBottom: "12px",
          }}
        >
          <div
            data-aos="fade-up"
            data-aos-easing="ease-out-cubic"
            data-aos-duration="2000"
            style={{ display: "flex", flexDirection: "column", margin: "0 0 50px 0" }}
          >
            <Typography variant="h5" component="p" color="primary" fontWeight={300} sx={{ margin: "7px 0" }}>
              Hello! I'm Marek, a software engineer, with more than two years of professional experience, based in Japan.
            </Typography>
            <Typography variant="h5" component="p" color="primary" fontWeight={300} sx={{ margin: "7px 0" }}>
              Active on both, front-end and back-end fields. Always eager to learn new technologies, code for fun after work.
            </Typography>
            <Typography variant="h5" component="p" color="primary" fontWeight={300} sx={{ margin: "7px 0 75px 0" }}>
              My free time: cooking, gaming and watching history documentaries.
            </Typography>
            <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center" }}>
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
          </div>
        </Container>
      </Container>
      <div style={{ margin: "auto 0px -3px", position: "relative", display: "inline-block" }}>
        <div style={{
          position: "absolute",
          left: 0,
          top: 0,
          width: "100%",
          height: "100%",
          display: "inline-block",
          background: "linear-gradient(to bottom, rgba(53,73,94,1) 0%,rgba(53,73,94,0) 100%)", /* W3C */
        }}></div>
        <img style={{ width: "100%" }} src="/assets/bg.jpeg" />
      </div>
    </>
  )
}

export default About;
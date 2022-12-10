import { ButtonGroup, Button, Container, Typography } from "@mui/material";
import { ReactElement } from "react";
import { Link } from "react-router-dom";
import {
  faJs,
  faReact,
  faPython,
  faVuejs,
  faSass,
  faPhp,
  faNpm,
  faGitAlt,
  faCss3Alt,
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
  faNpm: {
    icon: faNpm,
    'color': '#CB3837'
  },
  faGitAlt: {
    icon: faGitAlt,
    'color': '#F34F29'
  },
  faCss3Alt: {
    icon: faCss3Alt,
    'color': '#2965F1'
  },
}

const About = (): ReactElement => {
  AOS.init();

  return (
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
          }}
          to="/notes"
        >
          <Button
            style={{
              borderRadius: 0,
            }}
          >
            Notes
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
          style={{ display: "flex", flexDirection: "column", margin: "0 0 150px 0" }}
        >
          <Typography variant="h3" component="p" color="primary" fontWeight={100} sx={{ margin: "10px auto 25px" }}>
            in few words:
          </Typography>
          <Typography variant="h5" component="p" color="primary" fontWeight={300} sx={{ margin: "10px 10px" }}>
            i am a software developer
          </Typography>
          <Typography variant="h5" component="p" color="primary" fontWeight={300} sx={{ margin: "10px auto" }}>
            i like to code casually, started from front-end, now full-stack
          </Typography>
          <Typography variant="h5" component="p" color="primary" fontWeight={300} sx={{ margin: "10px 0 10px auto" }}>
            my free time: cooking, gaming and watching history documentaries
          </Typography>
        </div>
        <Typography
          data-aos="fade-up-left"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          variant="h3"
          component="h3"
          color="primary"
          fontWeight={100}
          sx={{ marginBottom: 1 }}
        >
          #software_developer
        </Typography>
        <Typography
          data-aos="fade-up-right"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          variant="h3"
          component="h3"
          align="right"
          color="primary"
          fontWeight={100}
          sx={{ marginBottom: 1 }}
        >
          #web_dev
        </Typography>
        <div
          data-aos="fade-down"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          style={{ display: "flex", justifyContent: "space-evenly", margin: "75px 0" }}
        >
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faJs.icon}
            color={ICONS.faJs.color}
            size="4x"
          />
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faReact.icon}
            color={ICONS.faReact.color}
            size="4x"
          />
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faVuejs.icon}
            color={ICONS.faVuejs.color}
            size="4x"
          />
        </div>
        <Typography
          data-aos="zoom-in"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          variant="h3"
          component="h3"
          align="center"
          color="primary"
          fontWeight={100}
          sx={{ marginBottom: 1 }}
        >
          #casual_gamer
        </Typography>
        <Typography
          data-aos="fade-up-left"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          variant="h3"
          component="h3"
          color="primary"
          fontWeight={100}
          sx={{ marginBottom: 1 }}
        >
          #cooking
        </Typography>
        <div
          data-aos="fade-down"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          style={{ display: "flex", justifyContent: "space-evenly", margin: "75px 0" }}
        >
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faPython.icon}
            color={ICONS.faPython.color}
            size="4x"
          />
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faPhp.icon}
            color={ICONS.faPhp.color}
            size="4x"
          />
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faNpm.icon}
            color={ICONS.faNpm.color}
            size="4x"
          />
        </div>
        <Typography
          data-aos="fade-up-right"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          variant="h3"
          component="h3"
          align="right"
          color="primary"
          fontWeight={100}
          sx={{ marginBottom: 1 }}
        >
          #full_stack
        </Typography>
        <Typography
          data-aos="zoom-in"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          variant="h3"
          component="h3"
          align="center"
          color="primary"
          fontWeight={100}
          sx={{ marginBottom: 1 }}
        >
          #polish_english_japanese
        </Typography>
        <div
          data-aos="fade-down"
          data-aos-easing="ease-out-cubic"
          data-aos-duration="2000"
          data-aos-delay="500"
          data-aos-anchor-placement="center-bottom"
          style={{ display: "flex", justifyContent: "space-evenly", margin: "75px 0" }}
        >
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faCss3Alt.icon}
            color={ICONS.faCss3Alt.color}
            size="4x"
          />
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faSass.icon}
            color={ICONS.faSass.color}
            size="4x"
          />
          <FontAwesomeIcon
            style={{
              padding: "0 20px",
            }}
            icon={ICONS.faGitAlt.icon}
            color={ICONS.faGitAlt.color}
            size="4x"
          />
        </div>
      </Container>
    </Container>
  )
}

export default About;
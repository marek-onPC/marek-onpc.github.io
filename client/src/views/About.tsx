import { ButtonGroup, Button, Container } from "@mui/material";
import { ReactElement } from "react";
import { Link } from "react-router-dom";

const About = (): ReactElement => {
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
        <Button>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/"
          >
            Home
          </Link>
        </Button>
        <Button>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/notes"
          >
            Notes
          </Link>
        </Button>
        <Button>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/about"
          >
            About
          </Link>
        </Button>
        <Button>
          <Link
            style={{
              color: "inherit",
              textDecoration: "none",
            }}
            to="/project"
          >
            Project
          </Link>
        </Button>
      </ButtonGroup>
      <Container
        sx={{
          width: "100%",
          marginTop: "50px",
          paddingTop: "50px",
          paddingBottom: "50px",
          background: "white",
          borderRadius: 2.5
        }}
        maxWidth="md"
      >
        <p>Hi! I am Marek, a Frontend Developer interested in web dev technologies, mainly in practical use of JavaScript with JS frameworks, and some back-end dev with PHP.</p>
        <p>This website is my side project to collect useful information with which I came across during my personal and commercial work, and save it in a form of easily accessible notes.</p>
        <p>My main project though, on which I am mainly working during my spare time, is a WordPress Gutenberg extension plugin called Gutenberg Plus, which allows user to use new useful blocks in WordPress main content editor – Gutenberg.
          Plugin is created by using JSX syntax known from React, with an environment based on NPM and Gulp toolkit.</p>
      </Container>
    </Container>
  )
}

export default About;
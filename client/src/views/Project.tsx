import { ButtonGroup, Button, Container } from "@mui/material";
import { ReactElement } from "react";
import { Link } from "react-router-dom";

const Project = (): ReactElement => {
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
              borderRadius: 0,
            }}
          >
            About
          </Button>
        </Link>
        <Link
          style={{
            color: "inherit",
            textDecoration: "none",
          }}
          to="/project"
        >
          <Button
            style={{
              borderTopLeftRadius: 0,
              borderBottomLeftRadius: 0,
            }}
          >
            Project
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
          background: "white",
          borderRadius: 2.5,
          lineHeight: "26px",
        }}
        maxWidth="md"
      >
        <h1>blocksplus</h1>
        <p>BlocksPlus is a WordPress extension plugin for Gutenberg editor. It is my main project to have something fun to do with code when I’m getting bored.</p>
        <h3>Why WordPress and Gutenberg?</h3>
        <p>WordPress, because with releasing a plugin to the wider audience, I can run a small scale project on my own, where the end-user experience plays the crucial role in development process.</p>
        <p>Gutenberg, because this content editor is built with React.js, and its API is heavily based on this JS library. With this, I can work in an environment I like, yet it is not 100% React, and that forces me to look for new solutions and trying different things.</p>
        <h3>Technologies</h3>
        <p>Project built with:</p>
        <ul>
          <li>JavaScript (with JSX syntax)</li>
          <li>PHP</li>
          <li>NMP</li>
          <li>Gulp</li>
          <li>Maybe some of (beloved) TypeScript in future? Who knows...</li>
        </ul>
        <h3>Development process</h3>
        <ul>
          <li>Checking which future could be created/fixed/adjusted (currently based mostly on my own experience with content management)</li>
          <li>Looking for affordable way of implementing it, with keeping the backwards compatibility</li>
          <li>Coding, coding, coding</li>
          <li>Testing the feature on different WP instances</li>
          <li>Release</li>
        </ul>
      </Container>
    </Container >
  )
}

export default Project;
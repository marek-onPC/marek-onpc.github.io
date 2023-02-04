import { ButtonGroup, Button, Container, Box, LinearProgress, Typography, Chip, Stack } from "@mui/material";
import { ReactElement, useCallback, useEffect, useLayoutEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchClientGetWithoutToken } from "../helpers/fetchClient";
import { NoteType } from "../types";
import Prism from "prismjs";
import "prismjs/components/prism-markup-templating";
import "prismjs/components/prism-sql";
import "prismjs/components/prism-javascript";
import "prismjs/components/prism-typescript";
import "prismjs/components/prism-jsx";
import "prismjs/components/prism-tsx";
import "prismjs/components/prism-php";
import "prismjs/components/prism-python";
import "prismjs/components/prism-css";
import "prismjs/components/prism-scss";
import "prismjs/themes/prism-tomorrow.css";
import GoToTop from "../components/GoToTop";
import DynamicTOC from "../components/DynamicTOC";

const PublicNote = (): ReactElement => {
  const [note, setNote] = useState<NoteType | null>(null);
  const [isGoToTopVisible, setIsGoToTopVisible] = useState<boolean>(false);

  const getNoteIdFromParam = (): string | null => {
    const [_, query] = window.location.href.split('#')[1].split('?')
    const params = new URLSearchParams(query)

    if (params) {
      return params.get("id");
    }
    return null;
  };

  const createHeadingsId = (content: string): string => {
    if (content.match('<h2>')) {
      content = content.replace('<h2>', `<h2 id="id-${(Math.random() * 100)}">`)
      return createHeadingsId(content);
    }
    return content;
  }

  const getNote = useCallback(async (): Promise<void> => {
    const noteId = getNoteIdFromParam();
    if (!noteId) {
      return;
    }

    try {
      const note = await fetchClientGetWithoutToken(
        `/note/${noteId}`
      );
      const noteData = JSON.parse(note.data) as NoteType;
      noteData.content = createHeadingsId(noteData.content)
      setNote(noteData);
    }
    catch (error) {
      console.log(error);
    }
  }, []);

  const onScrollCallback = () => {
    if (window.scrollY > 250) {
      setIsGoToTopVisible(true);
    } else {
      setIsGoToTopVisible(false);
    }
  }

  useLayoutEffect(() => {
    Prism.highlightAll();
  }, [note])

  useEffect(() => {
    if (getNoteIdFromParam() !== "") {
      getNote();
    } else {
      setNote({
        id: "",
        title: "",
        categories: [""],
        content: ""
      })
    }
  }, [getNote]);

  useEffect(() => {
    window.addEventListener("scroll", onScrollCallback);

    return () => {
      window.removeEventListener("scroll", onScrollCallback);
    }
  }, []);

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
      {note ?
        <>
          <Typography
            variant="h2"
            component="h1"
            color="primary"
            fontWeight={400}
            style={{ marginTop: "45px", textAlign: "center" }}
          >
            {note.title}
          </Typography>
          <Stack direction="row" spacing={1} style={{ marginTop: "20px" }}>
            {note.categories.map((category, index) =>
              <Chip key={index} label={category} variant="outlined" color="primary" />
            )}
          </Stack>

          <Container
            sx={{
              width: "100%",
              marginTop: "30px",
              marginBottom: "50px",
              paddingTop: "12px",
              paddingBottom: "12px",
              background: "white",
              borderRadius: 1.75,
              lineHeight: "26px",
            }}
            className="content-body"
            maxWidth="md"
            dangerouslySetInnerHTML={{ __html: note.content }}
          >
          </Container>
        </>
        : <Box sx={{ maxWidth: "500px", width: '100%', marginTop: "50px" }}>
          <LinearProgress />
        </Box>
      }
      <DynamicTOC />
      <GoToTop isVisible={isGoToTopVisible} />
    </Container>
  )
}

export default PublicNote;
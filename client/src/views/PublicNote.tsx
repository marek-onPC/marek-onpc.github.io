import { ButtonGroup, Button, Container, Box, LinearProgress, Typography, Chip, Stack } from "@mui/material";
import { ReactElement, useCallback, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { fetchClientGetWithoutToken } from "../helpers/fetchClient";
import { NoteType } from "../types";

const PublicNote = (): ReactElement => {
  const [note, setNote] = useState<NoteType | null>(null);

  const getNoteIdFromParam = (): string | null => {
    const params = new URLSearchParams(window.location.search)

    if (params) {
      return params.get("id");
    }
    return null;
  };

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
      setNote(noteData);
    }
    catch (error) {
      console.log(error);
    }
  }, []);

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
    </Container>
  )
}

export default PublicNote;
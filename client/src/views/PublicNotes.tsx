import { Box, LinearProgress, ButtonGroup, Button, Container } from "@mui/material";
import { ReactElement, useCallback, useEffect, useState } from "react";
import NoteCard from "../components/NoteCard";
import { fetchClientGetWithoutToken } from "../helpers/fetchClient";
import { NoteCardType } from "../types";
import { Link } from "react-router-dom";

const PublicNotes = (): ReactElement => {
  const [notes, setNotes] = useState<Array<NoteCardType> | null>(null);

  const getNotes = useCallback(async (): Promise<void> => {
    try {
      const notes = await fetchClientGetWithoutToken(
        "/notes",
      );
      setNotes(JSON.parse(notes.data));
    }
    catch (error) {
      console.log(error);
    }
  }, [])

  useEffect(() => {
    getNotes();
  }, [getNotes]);

  return (
    <Container
      sx={{
        width: "100%",
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
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
      <Box
        sx={{
          width: "100%",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          paddingTop: "50px",
        }}
      >
        <Box
          component="div"
          sx={{
            width: "100%",
            display: "flex",
            flexWrap: "wrap",
            justifyContent: "center",
          }}
        >
          {notes
            ? <>
              {notes.map((note, index) =>
                <NoteCard key={index} id={note.id} title={note.title} categories={note.categories} isDashboard={false} />
              )}
            </>
            : <Box sx={{ maxWidth: "500px", width: '100%', marginTop: "50px" }}>
              <LinearProgress />
            </Box>
          }
        </Box>
      </Box>
    </Container>
  )
}

export default PublicNotes;
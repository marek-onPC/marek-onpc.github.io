import { Box, LinearProgress } from "@mui/material";
import { ReactElement, useCallback, useContext, useEffect, useState } from "react";
import NoteCard from "../../components/NoteCard";
import { fetchClientGet } from "../../helpers/fetchClient";
import { NoteCardType } from "../../types";
import { AuthContext } from "../../utils/AuthContext";

const Notes = (): ReactElement => {
  const [notes, setNotes] = useState<Array<NoteCardType> | null>(null);
  const token: string = useContext(AuthContext);

  const getNotes = useCallback(async (): Promise<void> => {
    try {
      const notes = await fetchClientGet(
        "/notes",
        token
      );
      setNotes(JSON.parse(notes.data));
    }
    catch (error) {
      console.log(error);
    }
  }, [token])

  useEffect(() => {
    getNotes();
  }, [getNotes]);

  return (
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
          <NoteCard _id="" title="Add new note" categories={["and assign category"]} isGreen={true} isDashboard={true} />
          {notes.map((note, index) =>
            <NoteCard key={index} _id={note._id} title={note.title} categories={note.categories} isDashboard={true} />
          )}
        </>
        : <Box sx={{ maxWidth: "500px", width: '100%', marginTop: "50px" }}>
          <LinearProgress />
        </Box>
      }
    </Box>
  )
}

export default Notes;
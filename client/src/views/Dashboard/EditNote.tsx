import { Box, LinearProgress } from "@mui/material";
import { ReactElement, useContext, useEffect, useState } from "react";
import { fetchClientGet } from "../../helpers/fetchClient";
import { NoteCardType } from "../../types";
import { AuthContext } from "../../utils/AuthContext";

const EditNote = (): ReactElement => {
  const [note, setNote] = useState<NoteCardType | null>(null);
  const token: string = useContext(AuthContext);

  const getNoteIdFromParam = (): string | null => {
    const params = new URLSearchParams(window.location.search)

    if (params) {
      return params.get("id");
    }
    return null;
  };

  const getNote = async (): Promise<void> => {
    const noteId = getNoteIdFromParam();
    if (!noteId) {
      return;
    }

    try {
      const note = await fetchClientGet(
        `/note/${noteId}`,
        token
      );
      setNote(JSON.parse(note.data));
    }
    catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    getNote();
  }, [getNote]);

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
      {note
        ? <Box sx={{ maxWidth: "500px", width: '100%', marginTop: "50px" }}>
          Content
          <LinearProgress />
        </Box>
        : <Box sx={{ maxWidth: "500px", width: '100%', marginTop: "50px" }}>
          <LinearProgress />
        </Box>
      }
    </Box>
  )
}

export default EditNote;
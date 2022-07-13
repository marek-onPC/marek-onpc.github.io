import { Box, LinearProgress, TextField } from "@mui/material";
import { KeyboardEventHandler, ReactElement, useCallback, useContext, useEffect, useRef, useState } from "react";
import { fetchClientGet } from "../../helpers/fetchClient";
import { NoteType } from "../../types";
import { AuthContext } from "../../utils/AuthContext";
import { Editor } from '@tinymce/tinymce-react';

const EditNote = (): ReactElement => {
  const [note, setNote] = useState<NoteType | null>(null);
  const token: string = useContext(AuthContext);
  const tinyMceKey = process.env.REACT_APP_TINY_MCE_KEY as string;
  const editorRef = useRef(null);

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
      const note = await fetchClientGet(
        `/note/${noteId}`,
        token
      );
      const noteData = JSON.parse(note.data) as NoteType;
      setNote(noteData);
    }
    catch (error) {
      console.log(error);
    }
  }, []);

  const updateTitle = (newValue: string) => {
    setNote((prevState) => prevState ? { ...prevState, title: newValue } : prevState)
  }

  const updateContent = () => {
    if (editorRef.current) {
      setNote((prevState) => prevState ?
        {
          ...prevState,
          // @ts-ignore
          content: editorRef.current.getContent()
        }
        : prevState
      )
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
        ? <Box sx={{ maxWidth: "768px", width: '100%', marginTop: "50px" }}>
          <Box
            component="form"
            sx={{
              width: "100%",
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
            }}
          >
            <TextField
              sx={{
                width: "100%",
                backgroundColor: "#fff",
                borderRadius: 1,
                marginBottom: "25px"
              }}
              name="noteTitle"
              variant="filled"
              label="Note title"
              value={note.title}
              onChange={event => updateTitle(event.target.value)}
            />
            <>
              <Editor
                apiKey={tinyMceKey}
                // @ts-ignore
                onInit={(evt, editor) => editorRef.current = editor}
                initialValue={note.content}
                init={{
                  height: 500,
                  menubar: false,
                  plugins: [
                    'advlist', 'autolink', 'lists', 'link', 'image', 'charmap', 'preview',
                    'anchor', 'searchreplace', 'visualblocks', 'code', 'fullscreen',
                    'insertdatetime', 'media', 'table', 'code', 'help', 'wordcount'
                  ],
                  toolbar: 'undo redo | blocks | ' +
                    'bold italic forecolor | alignleft aligncenter ' +
                    'alignright alignjustify | bullist numlist outdent indent | ' +
                    'removeformat | help',
                  content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
                }}
              />
            </>
            <a onClick={updateContent}>Log editor content</a>

          </Box>
        </Box>
        : <Box sx={{ maxWidth: "500px", width: '100%', marginTop: "50px" }}>
          <LinearProgress />
        </Box>
      }
    </Box>
  )
}

export default EditNote;
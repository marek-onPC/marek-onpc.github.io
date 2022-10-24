import { Alert, Box, LinearProgress, TextField } from "@mui/material";
import { LoadingButton } from "@mui/lab";
import { ReactElement, useCallback, useContext, useEffect, useRef, useState } from "react";
import { fetchClientGet, fetchClientPost } from "../../helpers/fetchClient";
import { NoteType } from "../../types";
import { AuthContext } from "../../utils/AuthContext";
import { Editor } from '@tinymce/tinymce-react';

const EditNote = (): ReactElement => {
  const [note, setNote] = useState<NoteType | null>(null);
  const [isNoteSaving, setIsNoteSaving] = useState<boolean>(false);
  const [isSavingError, setIsSavingError] = useState<boolean>(false);
  const token: string = useContext(AuthContext);
  const tinyMceKey = process.env.REACT_APP_TINY_MCE_KEY as string;
  const editorRef = useRef(null);

  const getNoteIdFromParam = (): string | null => {
    const [_, query] = window.location.href.split('#')[1].split('?')
    const params = new URLSearchParams(query)

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
  }, [token]);

  const updateTitle = (newValue: string) => {
    setNote((prevState) => prevState ? { ...prevState, title: newValue } : prevState)
  }

  const updateCategories = (newValue: string) => {
    const newCategories = newValue.split(",");
    setNote((prevState) => prevState ? { ...prevState, categories: newCategories } : prevState)
  }

  const updateContent = () => {
    if (editorRef.current) {
      setNote((prevState) => prevState ?
        {
          ...prevState,
          // @ts-ignore
          content: editorRef.current.getContent()
        }
        : note
      )
    }
  };

  const saveNote = async () => {
    if (!!note) {
      try {
        setIsNoteSaving(true);
        setIsSavingError(false)

        await fetchClientPost(
          `/note`,
          token,
          note,
        );
      } catch (error) {
        setIsSavingError(true)
      }
      setIsNoteSaving(false)
    } else {
      console.log("Note not yet loaded")
    }
  };

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
            {isSavingError
              ? <Alert
                sx={{
                  width: "100%",
                  maxWidth: 250,
                  margin: "0px auto 50px"
                }}
                severity="error"
              >
                Error occurred on saving, try again.
              </Alert>
              : null}
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
            <TextField
              sx={{
                width: "100%",
                backgroundColor: "#fff",
                borderRadius: 1,
                marginBottom: "25px"
              }}
              name="categories"
              variant="filled"
              label="Categories (separate with , only and no spaces)"
              value={note.categories.toString()}
              onChange={event => updateCategories(event.target.value)}
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
                  toolbar: 'undo redo | blocks | code | link | ' +
                    'bold italic forecolor | alignleft aligncenter ' +
                    'alignright alignjustify | bullist numlist outdent indent | ' +
                    'removeformat | help',
                  content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
                }}
                onBlur={updateContent}
              />
            </>
            <LoadingButton
              sx={{
                width: "max-content",
                marginTop: "25px",
                marginBottom: "25px"
              }}
              variant="contained"
              onClick={saveNote}
              loading={isNoteSaving}
            >
              Save
            </LoadingButton>
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
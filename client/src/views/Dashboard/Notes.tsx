import { ReactElement, useContext, useEffect, useState } from "react";
import { fetchClientGet } from "../../helpers/fetchClient";
import { AuthContext } from "../../utils/AuthContext";

const Notes = (): ReactElement => {
  const [notes, setNotes] = useState<Array<unknown> | null>(null);
  const token: string = useContext(AuthContext);

  const getNotes = async (): Promise<void> => {
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
  }

  useEffect(() => {
    getNotes();
  });

  return (
    <div>
      {notes
        ? notes.map(note => 
          // prepare type for note object
        <p>{note.title}</p>)
        : <>Loading...</>
      }
    </div>
  )
}

export default Notes;
import { render, screen } from "@testing-library/react"
import {
  BrowserRouter as Router,
} from "react-router-dom";
import { DUMMY_NOTES } from "../setupTests";
import PublicNotes from "./PublicNotes";

describe("Dashboard's Notes page", () => {
  it.each(DUMMY_NOTES)("shows Notes page in Dashboard", async (note) => {
    render(
      <Router>
          <PublicNotes />
      </Router>
    );

    const noteTitle = await screen.findByText(note.title);
    expect(noteTitle).toBeInTheDocument();
  })
});
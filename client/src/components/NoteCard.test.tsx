import { render, screen, waitFor } from "@testing-library/react"
import userEvent from "@testing-library/user-event";
import {
  BrowserRouter as Router,
} from "react-router-dom";
import { NoteCardType } from "../types";
import NoteCard from "./NoteCard";

describe("NoteCard component", () => {
  const DUMMY_NOTE: NoteCardType = {
    _id: "idString",
    title: "Note title",
    categories: ["categoryOne, categoryTwo"]
  }

  it("shows note card", async () => {
    const redirectionUriToBeExpected = `http://localhost/note?id=${DUMMY_NOTE._id}`;

    render(
      <Router>
        <NoteCard _id={DUMMY_NOTE._id} title={DUMMY_NOTE.title} categories={DUMMY_NOTE.categories} />
      </Router>
    );

    const title = screen.getByText(/note title/i);
    const categories = screen.getByText(/categoryOne, categoryTwo/i);

    expect(title).toBeInTheDocument();
    expect(categories).toBeInTheDocument();
    userEvent.click(title);

    await waitFor(() => {
      expect(window.location.href).toEqual(redirectionUriToBeExpected);
    });
  })
});
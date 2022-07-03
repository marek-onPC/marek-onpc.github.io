import { render, screen } from "@testing-library/react"
import {
  BrowserRouter as Router,
} from "react-router-dom";
import { DUMMY_NOTES } from "../../setupTests";
import Dashboard from "./Dashboard";
import Notes from "./Notes";

describe("Dashboard's Notes page", () => {
  it.each(DUMMY_NOTES)("shows Notes page in Dashboard", async (note) => {
    render(
      <Router>
        <Dashboard>
          <Notes />
        </Dashboard>
      </Router>
    );

    const title = await screen.findByText(note.title);
    expect(title).toBeInTheDocument();
    expect
  })
});
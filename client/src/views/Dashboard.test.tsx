import { render, screen, waitFor } from "@testing-library/react"
import userEvent from "@testing-library/user-event";
import {
  BrowserRouter as Router,
} from "react-router-dom";
import Dashboard from "./Dashboard"

describe("Dashboard page (to manage notes)", () => {
  it("shows dashboard page", () => {
    render(
      <Router>
        <Dashboard>
          <h1>dashboard</h1>
        </Dashboard>
      </Router>
    );

    const notesButton = screen.getByText(/notes/i);
    const categoriesButton = screen.getByText(/categories/i);

    expect(notesButton).toBeInTheDocument();
    expect(categoriesButton).toBeInTheDocument();
  })

  it("goes to notes page if Notes button is clicked", async () => {
    const redirectionUriToBeExpected = "http://localhost/dashboard/notes";
    render(
      <Router>
        <Dashboard>
          <h1>dashboard</h1>
        </Dashboard>
      </Router>
    );

    const notesButton = screen.getByText(/notes/i);
    expect(notesButton).toBeInTheDocument();
    userEvent.click(notesButton);

    await waitFor(() => {
      expect(window.location.href).toEqual(redirectionUriToBeExpected);
    });
  });

  it("goes to categories page if Categories button is clicked", async () => {
    const redirectionUriToBeExpected = "http://localhost/dashboard/categories";
    render(
      <Router>
        <Dashboard>
          <h1>dashboard</h1>
        </Dashboard>
      </Router>
    );

    const categoriesButton = screen.getByText(/categories/i);
    expect(categoriesButton).toBeInTheDocument();
    userEvent.click(categoriesButton);

    await waitFor(() => {
      expect(window.location.href).toEqual(redirectionUriToBeExpected);
    });
  });
});